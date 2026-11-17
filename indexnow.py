#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IndexNow 提交脚本 —— 把新增/修改的网址主动推给 Bing / Yandex / Naver 等

用法（在博客根目录 E:\\Blog 下运行）:

    python indexnow.py --all          # 提交 sitemap.xml 里的全部 URL（首次用一次即可）
    python indexnow.py --posts        # 只提交 sitemap 里的文章 URL
    python indexnow.py --changed      # 提交上一次 git 提交里改动的文章/页面
    python indexnow.py URL [URL...]   # 提交你手动指定的 URL
    python indexnow.py --all --dry-run   # 只打印要提交什么，不真的发请求

流程：先 hexo g / hexo d 部署，确认 key 文件已上线（脚本会自动检查，并重试等待 Pages 发布），再运行本脚本。
deploy.py 已经自动调用 `--changed`，日常发布一条 `python deploy.py` 就够了；
第一次（key 文件还没上线过）发布时，建议等 Pages 发布完后手动再跑一次 `python indexnow.py --posts`。
"""

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# IndexNow 的 key：必须和站点根目录下的 <key>.txt 内容一致
KEY = "7be62dc50c074ef894922261b6dd0814"

ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_URLS_PER_REQUEST = 10000  # IndexNow 单次请求上限


def site_base() -> str:
    """从 _config.yml 的 url 读取站点根地址，避免以后改域名时忘了同步。"""
    cfg = (ROOT / "_config.yml").read_text(encoding="utf-8")
    m = re.search(r"(?m)^url:\s*(\S+)\s*$", cfg)
    if not m:
        sys.exit("无法从 _config.yml 读取 url，请手动检查配置")
    return m.group(1).rstrip("/")


BASE = site_base()
HOST = urllib.parse.urlparse(BASE).netloc
KEY_LOCATION = f"{BASE}/{KEY}.txt"


def sitemap_urls() -> list[str]:
    p = ROOT / "public" / "sitemap.xml"
    if not p.exists():
        sys.exit("找不到 public/sitemap.xml，请先运行 hexo g 生成站点")
    return re.findall(r"<loc>([^<]+)</loc>", p.read_text(encoding="utf-8"))


def url_from_source(rel_path: str) -> str | None:
    """把 source/ 下的源文件路径换算成站点 URL。"""
    p = ROOT / rel_path
    if rel_path.startswith("source/_posts/") and rel_path.endswith(".md"):
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"(?m)^abbrlink:\s*([0-9A-Za-z]+)\s*$", text)
        if not m:
            print(f"  ! 跳过（front-matter 里没有 abbrlink）: {rel_path}")
            return None
        return f"{BASE}/posts/{m.group(1)}.html"
    if rel_path.endswith("/index.md") and rel_path.startswith("source/"):
        rel = rel_path[len("source/"):-len("index.md")]
        return f"{BASE}/{rel}"
    if rel_path == "source/index.md":
        return f"{BASE}/"
    return None


def changed_urls(since: str) -> list[str]:
    """git diff 指定提交到 HEAD 之间改动的文章 / 页面。"""
    out = subprocess.run(
        # core.quotepath=false 防止中文文件名被转义成 "\346\226..." 这种形式
        ["git", "-c", "core.quotepath=false", "diff", "--name-only", since, "HEAD"],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
    )
    if out.returncode != 0:
        sys.exit(f"git diff 失败: {out.stderr.strip()}")
    urls: list[str] = []
    for line in out.stdout.splitlines():
        line = line.strip()
        if not line.startswith("source/"):
            continue
        url = url_from_source(line)
        if url and url not in urls:
            urls.append(url)
    return urls


def key_is_live(retries: int = 4, delay: int = 15) -> bool:
    """检查 key 文件是否已上线；刚部署完 Pages 可能要等几十秒，所以会重试几次。"""
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(KEY_LOCATION, headers={"User-Agent": "indexnow-check/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                body = r.read().decode("utf-8", "replace").strip()
                if r.status == 200 and body == KEY:
                    return True
                print(f"  ! key 文件内容不匹配（第 {attempt} 次）：{body[:80]!r}")
        except Exception as e:  # noqa: BLE001
            print(f"  ! 访问 key 文件失败（第 {attempt} 次）：{e}")
        if attempt < retries:
            print(f"  ... GitHub Pages 可能还没发布完，{delay}s 后重试")
            time.sleep(delay)
    return False


def submit(urls: list[str]) -> None:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "kisuraop-blog-indexnow/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow 返回: HTTP {r.status} {r.reason}")
            body = r.read().decode("utf-8", "replace").strip()
            if body:
                print(body[:1000])
    except urllib.error.HTTPError as e:
        print(f"IndexNow 返回: HTTP {e.code} {e.reason}")
        print(e.read().decode("utf-8", "replace")[:1000])
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"请求失败: {e}")
        sys.exit(1)


def main() -> None:
    ap = argparse.ArgumentParser(description="通过 IndexNow 提交博客 URL")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--all", action="store_true", help="提交 sitemap.xml 中的全部 URL")
    g.add_argument("--posts", action="store_true", help="只提交 sitemap.xml 中的文章 URL")
    g.add_argument("--changed", action="store_true", help="提交最近一次 git 提交中改动的文章/页面")
    ap.add_argument("--since", default=None, help="配合 --changed，指定起始提交（默认 HEAD^）")
    ap.add_argument("--dry-run", action="store_true", help="只打印，不发送请求")
    ap.add_argument("--skip-key-check", action="store_true", help="跳过 key 文件在线检查")
    ap.add_argument("urls", nargs="*", help="手动指定的 URL")
    args = ap.parse_args()

    if args.all:
        urls = sitemap_urls()
    elif args.posts:
        urls = [u for u in sitemap_urls() if "/posts/" in u]
    elif args.changed:
        urls = changed_urls(args.since or "HEAD^")
    elif args.urls:
        urls = args.urls
    else:
        ap.print_help()
        sys.exit(1)

    urls = [u for u in dict.fromkeys(urls) if u.startswith(BASE)]
    if not urls:
        print("没有需要提交的 URL。")
        sys.exit(0)

    print(f"站点: {BASE}")
    print(f"待提交 {len(urls)} 个 URL:")
    for u in urls:
        print(f"  - {u}")

    if args.dry_run:
        print("\n[dry-run] 未发送任何请求。")
        return

    if not args.skip_key_check:
        print(f"\n检查 key 文件: {KEY_LOCATION}")
        if not key_is_live():
            sys.exit(
                "key 文件还没上线。请先运行 hexo g && hexo d 部署，"
                "确认上面的地址能访问到后再提交（或加 --skip-key-check 强行提交）。"
            )
        print("key 文件 OK")

    submit(urls[:MAX_URLS_PER_REQUEST])


if __name__ == "__main__":
    main()
