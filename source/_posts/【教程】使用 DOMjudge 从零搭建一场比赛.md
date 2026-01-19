---
title: "【教程】使用 DOMjudge 从零搭建一场比赛"
sticky: 100
math: true
index_img: "https://pic.rmb.bdstatic.com/bjh/503fc6d6b075e49bf015e7cbc5553685.jpeg"
tags:
  - XCPC
  - Note
  - DOMjudge
categories:
  - Competitive Programming
  - Note
abbrlink: 4cf2169a
date: 2024-11-20 21:00:00
updated: 2024-11-20 21:00:00
---


本文使用的环境：全新 Ubuntu24.04 LTS。

Domjudge 版本：8.3.1。

本文主要参考了：

[Vingying | 关于搭建 domjudge 还有其他一些 ICPC Tool 之类的事](https://vingying.github.io/2024/09/04/domjudge-icpctool/)

[HeRaNO | 计算机 · DOMjudge Docker 配置](https://zhuanlan.zhihu.com/p/258024151)

文中的所有流程经过了从头验证，十分感谢 vy 和 hrdg 的耐心指导QAQ。

### 1. 安装 DOMjudge 和相关依赖


```bash
sudo apt-get update
sudo apt-get upgrade
```


```bash
sudo apt install acl zip unzip mariadb-server nginx \
        php-fpm php-gd php-cli php-intl php-mbstring php-mysql \
        php-curl php-json php-xml php-zip composer ntp

sudo apt install make gcc g++ debootstrap libcgroup-dev lsof \
        procps libcurl4-gnutls-dev libjsoncpp-dev libmagic-dev
```


```bash
cd /opt/
sudo wget https://www.domjudge.org/releases/domjudge-8.3.1.tar.gz
sudo tar -zxvf domjudge-8.3.1.tar.gz
```


如果 `wget` 太慢可以点链接进去下再 `sudo mv ./domjudge-8.3.1.tar.gz /opt/`。

### 2. 编译 DOMjudge，配置数据库和 web 服务器


```bash
cd /opt/domjudge-8.3.1
sudo ./configure --prefix=/opt/domjudge --with-domjudge-user=root --with-baseurl=127.0.0.1
```


这一步如果警告缺少 `pkg-config` 就 `sudo apt install pkg-config`。


```bash
sudo make domserver
```


这一步会弹出一个询问，直接 `yes`。


```bash
sudo make install-domserver
cd /opt/domjudge/domserver
sudo bin/dj_setup_database -s install
sudo ln -s /opt/domjudge/domserver/etc/nginx-conf /etc/nginx/sites-enabled/domjudge
sudo ln -s /opt/domjudge/domserver/etc/domjudge-fpm.conf /etc/php/8.3/fpm/pool.d/domjudge.conf
sudo service php8.3-fpm reload
```


最后两句 php 要换成对应的版本，我这里是 php8.3。

最后一句如果警告说要 `systemctl daemon-reload`，按它说的执行就行。


```bash
cd /etc/nginx/sites-enabled
sudo rm default
sudo service nginx reload
cd /opt/domjudge/domserver
sudo chown www-data:www-data -R webapp/public/*
```


接着访问 `127.0.0.1/domjudge` 就有 web 界面了（云服务器就换成公网地址）。

[![](https://kisuraop.github.io/image/academic/d1.png)](https://kisuraop.github.io/image/academic/d1.png)

如果没按前两句把 `default` 删掉你就会收获 404 的好结果。

如果还没有 web 界面就看看服务器 80 端口有没有打开。

接着在网页里 login，账号填 admin，密码通过以下命令获取：


```bash
sudo cat /opt/domjudge/domserver/etc/initial_admin_password.secret
```

### 3. 配置 php 和 mysql


```bash
cd /etc/php/8.3/fpm/pool.d
sudo vim domjudge.conf
```


如果提示没有 vim，就 `sudo apt install vim`。

打开配置文件后找到 `php_admin_value[memory_limit]` 一栏，改成：


```bash
php_admin_value[memory_limit] = 1024M
```


再找到 `php_admin_value[date.timezone]` 一栏，改成：


```bash
php_admin_value[date.timezone] = Asia/Shanghai
```


保存退出。


```bash
sudo service php8.3-fpm reload
sudo vim /etc/mysql/conf.d/mysql.cnf
```


你会看到一行 `[mysql]`，删掉。接着粘贴以下内容：


```bash
[mysqld]
max_connections = 1000
max_allowed_packet = 512MB
innodb_log_file_size = 2560MB
```


这只是示例，实际 `max_allowed_packet` 要改成两倍于题目测试数据文件的大小；`innodb_log_file_size` 要改成十倍于题目测试数据文件的大小。

保存退出。


```bash
sudo vim /etc/mysql/mariadb.conf.d/50-server.cnf
```


找到 `max_allowed_packet = 1G`，取消这一行的注释。

保存退出。


```bash
sudo systemctl restart mysql
```

如果一切正常，刷新 DOMjudge 的 web 页面，点进 config checker，你会看到：

[![](https://kisuraop.github.io/image/academic/d2.png)](https://kisuraop.github.io/image/academic/d2.png)

[![](https://kisuraop.github.io/image/academic/d3.png)](https://kisuraop.github.io/image/academic/d3.png)

### 4. 配置 judgehost (docker)

首先要下载 docker，如果是云服务器，可以找到对应的文档。

我则是查阅了一些博客和文章，以下命令可能有不妥之处。


```bash
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
```


这里可能会提示 `密钥存储在过时的 trusted.gpg 密钥环中`，我的解决方法是：


```bash
cd /etc/apt
sudo cp trusted.gpg trusted.gpg.d
sudo apt-get update
```


然后就可以安装 docker 了。


```bash
sudo apt-get install docker-ce
cd /etc/docker
sudo touch daemon.json
sudo vim daemon.json
```


粘贴以下内容：


```bash
{
    "registry-mirrors": ["https://docker.1ms.run"]
}
```


其中国内镜像源是我从 [Link](https://cloud.tencent.com/developer/article/2454486) 里面找的。

保存退出。


```bash
sudo service docker restart
```


接着设置 cgroups。


```bash
sudo vim /etc/default/grub
```


找到 `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"` 一行（引号里可能初始是空），改成：


```bash
GRUB_CMDLINE_LINUX_DEFAULT="quiet cgroup_enable=memory swapaccount=1 systemd.unified_cgroup_hierarchy=0"
```


保存退出。


```bash
sudo update-grub
sudo reboot
```


```bash
sudo docker run -d -it --privileged -v /sys/fs/cgroup:/sys/fs/cgroup --name judgehost-new0 --hostname localhost --network="host" -e DAEMON_ID=0 -e CONTAINER_TIMEZONE=Asia/Shanghai -e JUDGEDAEMON_PASSWORD=<domserver password> -e DOMSERVER_BASEURL=http://localhost/domjudge/ domjudge/judgehost:8.3.1
BASH
```


其中 `<domserver password>` 通过以下命令获取：


```bash
sudo cat /opt/domjudge/domserver/etc/restapi.secret
```

如果一切正常，那么：

[![](https://kisuraop.github.io/image/academic/d4.png)](https://kisuraop.github.io/image/academic/d4.png)

[![](https://kisuraop.github.io/image/academic/d5.png)](https://kisuraop.github.io/image/academic/d5.png)

如果起多个 judgehost，需要修改 `--name` 参数和 `DAEMON_ID` 参数。后者是核编号，不能超过机子的核心数。

例如起第 2 个 judgehost 的话，命令得是：


```bash
sudo docker run -d -it --privileged -v /sys/fs/cgroup:/sys/fs/cgroup --name judgehost-new1 --hostname localhost --network="host" -e DAEMON_ID=1 -e CONTAINER_TIMEZONE=Asia/Shanghai -e JUDGEDAEMON_PASSWORD=<domserver password> -e DOMSERVER_BASEURL=http://localhost/domjudge/ domjudge/judgehost:8.3.1
```


起第 3 个的话，得是：


```bash
sudo docker run -d -it --privileged -v /sys/fs/cgroup:/sys/fs/cgroup --name judgehost-new2 --hostname localhost --network="host" -e DAEMON_ID=2 -e CONTAINER_TIMEZONE=Asia/Shanghai -e JUDGEDAEMON_PASSWORD=<domserver password> -e DOMSERVER_BASEURL=http://localhost/domjudge/ domjudge/judgehost:8.3.1
```

### 5. 配置比赛

从这里开始就看个人喜好了。

以下配置均以 UESTC 第十五届趣味程序设计竞赛为例。

Configuration settings $\to$ External systems $\to$ configuration data external。

Configuration settings $\to$ Scoring $\to$ Results remap: 将 `output-limit` 和 `no-output` 定向为 `wrong-answer`。

save 之后如果提示你 Recalculate caches now，就点进去，之后同理。

Configuration settings $\to$ Judging $\to$ Enable parallel judging 关闭。

Configuration settings $\to$ Display $\to$ Show flags 关闭。

Configuration settings $\to$ Display $\to$ Allow team submission download 开启。

Configuration settings $\to$ Display $\to$ Show language versions 开启。

回到主页，进 Team Categories。

把 visible 的三个组别的 external ID 改成 `beginner`，`advanced` 和 `observer`，代表零基础组，有基础组，和打星组。然后把这三个组的 SortOrder 改成同一个数字（这样榜单上才不会割裂显示）。

接着导入队伍，依据 [Link](https://www.domjudge.org/docs/manual/8.3/import.html#importing-team-affiliations) 完成 accounts.yaml，teams.json 和 organizations.json。

* teams.json 中 display_name 虽然是 [option]，但如果不写这一项会默认设成空串，很神秘，所以还是加上。

以下是我用到的脚本：


```python
# gen_accounts.py
import random
import string

# 生成账号的数量
account_number = 452


def generate_team_data():
    data_list = []
    for i in range(1, account_number + 1):
        team_id = f"team{i:03d}"
        id = f"account{i:03d}"
        username = team_id
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        data_list.append(f"- id: {id}\n  username: {username}\n  password: {password}\n  type: team\n  team_id: '{team_id}'\n\n")
    return data_list


team_data = generate_team_data()

with open('accounts.yaml', 'w') as file:
    file.writelines(team_data)
```


```python
# gen_organizations.py
import pandas as pd
import json

# 读取表格第 10 列的内容（学校名称）
df = pd.read_excel('name.xlsx', usecols=[9], skiprows=1)

# 去重
universities = df.iloc[:, 0].dropna().unique()

organizations = [{"id": str(i + 1), "name": university, "formal_name": university, "country": "CHN"} for i, university in enumerate(universities) if university]

# 本校
organizations.append({"id": '100', "name": '电子科技大学', "formal_name": '电子科技大学', "country": "CHN"})

# 没填学校名字的
organizations.append({"id": '101', "name": '未填写', "formal_name": '未填写', "country": "CHN"})

with open('organizations.json', 'w', encoding='utf-8') as f:
    json.dump(organizations, f, ensure_ascii=False, indent=4)
PYTHON
```


```python
# gen_teams.py
import json
import pandas as pd

def generate_data():
    excel_data = pd.read_excel("name.xlsx", sheet_name=0)
    organizations = {}

    with open("organizations.json", "r", encoding="utf-8") as f:
        organizations = json.load(f)

    result = []
    id_counter = 1

    for _, row in excel_data.iterrows():
        if pd.isna(row[1]):
            break

        # row[2]: 是否为本校选手
        # row[5]: 是否正式参赛
        # row[6]: 年级
        # row[8]: 是否有信息竞赛基础
        # row[9]: 学校（外校）
        if row[2] == "否" or row[5] == "否（不参与评奖）":
            X = "observer"
        else:
            if row[6] == "大一" and row[8] == "否":
                X = "beginner"
            else:
                X = "advanced"

        if row[2] == "否":
            S = row[9]
            org_id = next((org["id"] for org in organizations if org["name"] == S), None)
            if not org_id:
                org_id = 101
                # raise ValueError(f"组织名称 '{S}' 未在 organizations.json 中找到！")
        else:
            org_id = 100

        item = {
            "id": f"team{id_counter:03d}",
            "group_ids": [str(X)],
            "name": row[1],
            "display_name": row[1],
            "organization_id": str(org_id)
        }
        result.append(item)

        id_counter += 1

    with open("teams.json", "w", encoding="utf-8") as outfile:
        json.dump(result, outfile, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    generate_data()
PYTHON
```


生成完毕后回到主页，点进 import / export，找到 Teams & groups $\to$ Import JSON / YAML。

将上述三个文件按 organizations.json，teams.json，accounts.yaml 的顺序传上去（务必注意顺序，Type 也要随着改动）。

不同大学的校徽可以在 [Link](https://github.com/CSGrandeur/CCPCOJ/tree/master/ojweb/public/static/image/school_badge) 或 [Link](https://www.urongda.com/logos) 里下载，再到主页进 Team Affiliations 里编辑上传。

接着建立 Contests。回到主页点进 Contests，demo 删掉，Add new contest，External ID 随便填一个，剩下的选项都有注释，不再赘述。

* 注意时间格式的 `timezone` 应该填 `Asia/Shanghai` 而不是 `UTC+8`。

可以利用 Problemset document 选项上传题面，在 Polygon 导出 Chinese 题面 PDF 的方法：
* 右边栏 Properties/File，找到 statements.ftl，Edit。

* 开头粘贴 `\usepackage {CJK}`，`\begin{document}` 之后粘贴 `\begin{CJK}{UTF8}{gbsn}`，结尾 `\end{document}` 前粘贴 `\end {CJK}`。

接着上传题目。需要借助 [Link](https://github.com/cn-xcpc-tools/Polygon2DOMjudge/blob/master/README.cn.md)。

Polygon 点进 Contest，右边栏找到 Build full packages (+verify)，点 (+verify)，之后点进每个题目的 Package 界面下载 Linux 版本的 package。


```bash
sudo apt install pipx
pipx install p2d
pipx ensurepath
```


关掉这个终端，重新开一个。

对每一题执行以下命令：


```bash
p2d --code A --color "#FF0000" -o /path/to/domjudge-package.zip /path/to/polygon-package.zip
```


其中 code 是题目的 short name，color 是题目在 DOMjudge 中的颜色，更多设置项可以点进链接里试。

* `--external-id` 也建议设置成 ABCD。

得到的 domjudge-package.zip 就可以在 Import and export $\to$ Problems 里上传了。

补一个邮件收集脚本：


```python
import pandas as pd
import yaml

def load_accounts_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        accounts = yaml.safe_load(file)
    if isinstance(accounts, list):
        accounts_dict = {item['username']: item for item in accounts}
    else:
        accounts_dict = accounts
    return accounts_dict

def create_mail_xlsx(name_file, accounts_yaml):
    df = pd.read_excel(name_file)
    accounts = load_accounts_yaml(accounts_yaml)

    data = []

    for i, row in df.iterrows():
        if pd.isna(row[1]):
            break

        name = row[1]
        if row[2] == '是':
            id = int(row[4])
            email = str(id) + "@std.uestc.edu.cn"
            email2 = ""
        else:
            email = str(row[10])
            if pd.isna(row[11]):
                email2 = ""
            else:
                email2 = str(row[11])
        username = f"team{i + 1:03d}"
        password = accounts.get(username, {}).get('password', '')

        if row[2] == "否" or row[5] == "否（不参与评奖）":
            user_type = "打星组"
        else:
            if row[6] == "大一" and row[8] == "否":
                user_type = "初学组"
            else:
                user_type = "进阶组"

        data.append([name, email, email2, username, password, user_type])

    mail_df = pd.DataFrame(data, columns=["姓名", "邮箱1", "邮箱2", "username", "password", "组别"])
    mail_df.to_excel('mail.xlsx', index=False)

if __name__ == "__main__":
    create_mail_xlsx('name.xlsx', 'accounts.yaml')
```

### 6. 比赛结束后

结束的时候马上点进 Contest 界面把 Allow submit 选项关掉。

接着导出榜单和提交。

榜单直接在浏览器界面右键打印，选择打印到 PDF。如果预览出来是黑白的，就在更多设置里面找到 "背景图形" 打上勾。

导出提交需要用到 [Link](https://github.com/HeRaNO/ChickenRibs/blob/master/ICPCToy/DOMjudge/dj_download_submissions.py)。命令如下：


```bash
py dj_download_submissions.py http://localhost/domjudge/ <contest-external-id>
```


其中 `<contest-external-id>` 是 contest 页面的 external ID。

