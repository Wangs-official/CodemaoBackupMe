from function import log, header
from rich.console import Console
import requests
import json
import math
import os


def backup(token: str, id: str, path: str):
    console = Console()
    now = 0
    replylist = []
    createdlist = []
    headers = header(token)
    logger = log()

    # 获取完整的发帖ID列表
    logger.info("尝试获取完整的发帖ID列表")
    total_post_num = json.loads(
        requests.get(
            url="https://api.codemao.cn/web/forums/posts/mine/created?page=1&limit=5",
            headers=headers,
        ).text
    ).get("total")
    page_num = math.ceil(total_post_num / 30)
    logger.info(f"共发帖{total_post_num}个，正在分{page_num}页处理")
    console.print(f"共发帖{total_post_num}个，正在分{page_num}页处理")
    for n in range(0, page_num):
        console.print(
            f"[blue bold]{n}/{page_num}[/blue bold] 正在获取发帖ID列表 [yellow]此步骤时间较长[/yellow] 根据发帖数量决定最终请求时长",
            end="\r",
        )
        response = requests.get(
            url=f"https://api.codemao.cn/web/forums/posts/mine/created?page={n + 1}&limit=30",
            headers=headers,
        )
        if response.status_code == 200:
            logger.info(f"请求成功，组合信息中，第{n}页")
            ids = [item["id"] for item in response.json()["items"]]
            createdlist.extend(ids)
        else:
            logger.error(f"请求{n}时发生错误：{response.status_code} {response.text}")
            print(f"[red]请求发生错误，请检查日志![/red] {n}")
        logger.info(f"请求成功，已记录发帖ID")

    # 获取帖子源文件
    for postid in createdlist:
        now += 1
        console.print(
            f"[blue bold]{now}/{len(createdlist)}[/blue bold] 正在获取帖子: {postid}",
            end="\r",
        )
        info_response = requests.get(
            f"https://api.codemao.cn/web/forums/posts/{postid}/details", headers=headers
        )
        if info_response.status_code == 200:
            post_title = info_response.json().get("title")
            post_content = info_response.json().get("content")
            # replies = info_response.json().get("n_replies")
            logger.info(
                f"请求成功，将返回信息写入到{path}/forum/{postid}-{post_title}中"
            )
            os.makedirs(f"{path}/forum/{postid}-{post_title}", exist_ok=True)
            with open(
                f"{path}/forum/{postid}-{post_title}/post.html", "w", encoding="utf-8"
            ) as f:
                f.write(post_content)
                f.close()
                logger.info("写入HTML完成")
        else:
            logger.error(
                f"请求{postid}时发生错误：{response.status_code} {response.text}"
            )
            print(f"[red]请求发生错误，请检查日志![/red] {postid}")
    return True
