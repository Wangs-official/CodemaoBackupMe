"""
-*- coding: utf-8 -*-
@File: main.py
@author: WangZixu
"""
# other lib

from rich import print
import getpass
import time

# cbm lib
from cbm.login import login_user, logout_user
from cbm.setup import init_folder, del_folder
from cbm.info import backup as info_backup

# function lib
from function import clear_screen
from function import log

# welcome
clear_screen()
print("[green]欢迎使用CodemaoBackupMe! By WangZixu_旭[/green] 继续使用则默认为你已同意用户协议")
input("按下空格继续...")

logger = log()

# login
clear_screen()
print("[bold]登录编程猫账号[/bold]")
phone_code = input("输入手机号/邮箱/用户名: ")
password = getpass.getpass("输入密码（已隐藏，输入后回车）: ")
logger.info("已发起登录请求")
login = login_user(phone_code, password)
if login[0]:
    clear_screen()
    logger.info(f"已完成登录，用户名{login[1]} ({login[3]})")
    nickname = login[1]
    token = login[2]
    uid = login[3]
else:
    clear_screen
    logger.error(f"登录失败，状态码:{login[1]}，返回文本{login[2]}")
    print(f"[red]请求失败：{login[1]}[/red] {login[2]}")
    exit()

# menu
print(f"[green]{nickname} ({uid})[/green] 欢迎回来！请选择要备份的内容~")
print("[bold]1. 完全备份[/bold]")
print("[bold]2. 仅备份个人信息[/bold]")
print("[bold]3. 仅备份作品源文件/互动信息[/bold]")
print("[bold]4. 仅备份论坛发帖/回复[/bold]")
print("[bold]5. 仅备份图书馆信息[/bold]")
print("[bold]6. 吊销Token并退出[/bold]")
while True:
    choose = input("输入数字以选择：")
    try:
        choose = int(choose)
        if 1 <= choose <= 6:
            break
        else:
            print("[red]请输入1~6之间的数字[/red]")
    except ValueError:
        print("[red]输入的不是数字[/red]")

match choose:
    case 1:
        logger.info("已选择选项1，开始完全备份")
    case 2:
        clear_screen()
        logger.info("已选择选项2，开始备份个人信息")
        print("[blue]创建目录中[/blue] 稍作等待，请勿关闭/选中窗口...")
        folder_path = "backup/" + init_folder()[1]
        print(f"[green]备份目录已创建[/green] {folder_path}")
        time.sleep(1)
        print("[blue]正在备份个人信息[/blue] 稍作等待，请勿关闭/选中窗口...")
        if info_backup(token, uid, folder_path):
            clear_screen()
        print("[blue]正在清除空文件夹[/blue] 稍作等待，请勿关闭/选中窗口")
        time.sleep(1)
        if del_folder(folder_path):
            clear_screen()
        logger.info("备份流程结束")
        if logout_user(token):
            logger.info("吊销成功")
        print("[green]备份全部完成[/green] 感谢使用此工具！你的Token已被吊销，程序退出")
        exit()
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        logger.info("已选择选项6，正在退出账号")
        if logout_user(token):
            logger.info("吊销成功")
            clear_screen()
            print("[green]操作已完成[/green] Token已成功吊销，欢迎下次使用")
            exit()