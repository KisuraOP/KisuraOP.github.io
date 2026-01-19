import os

def run(cmd):
    print(f"Executing: {cmd}")
    os.system(cmd)

if __name__ == "__main__":
    # 1. 清理并生成静态页面
    run("hexo clean")
    run("hexo g")
    # 2. 部署静态页面到 main 分支
    run("hexo d")
    # 3. 备份源码到 hexo-source 分支
    run("git add .")
    run('git commit -m "update blog"')
    run("git push origin hexo-source")
    print("All done! 博客已更新并备份。")