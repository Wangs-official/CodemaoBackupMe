from function import log, loading, header
from rich.console import Console
import requests
import json
import math

def backup(token: str, id: str, path: str):
    console = Console()
    now = 0
    fanslist = []
    followlist = []
    headers = header(token)
    logger = log()

    details_url = "https://api.codemao.cn/web/users/details"
    info_url = "https://api.codemao.cn/api/user/info"
    honor_url = (
        f"https://api.codemao.cn/creation-tools/v1/user/center/honor?user_id={id}"
    )
    worklist_url = f"https://api.codemao.cn/creation-tools/v1/user/center/work-list?user_id={id}&offset=1&limit=200"
    collectlist_url = f"https://api.codemao.cn/creation-tools/v1/user/center/collect/list?user_id={id}&offset=1&limit=200"
    followlist_url = f"https://api.codemao.cn/creation-tools/v1/user/followers?user_id={id}&offset=1&limit=10"  # 取total值再发
    fanslist_url = f"https://api.codemao.cn/creation-tools/v1/user/fans?user_id={id}&offset=1&limit=10"  # 取total值再发
    urls = [
        details_url,
        info_url,
        honor_url,
        worklist_url,
        collectlist_url,
        followlist_url,
        fanslist_url,
    ]
    filename = [
        "details.json",
        "info.json",
        "honor.json",
        "work-list.json",
        "collect-list.json",
        "followers-list.json",
        "fan-list.json",
    ]
    for i in urls:
        now += 1
        logger.info(f"正在请求API: {i} | 第{now}个")
        loading(now, 7, i)
        if now == 6:  # 取关注列表total
            total_num = json.loads(requests.get(url=i, headers=headers).text).get(
                "total"
            )
            page_num = math.ceil(total_num / 200)
            logger.info(f"关注列表共{total_num}个，正在分{page_num}页处理")
            console.print(f"关注列表共{total_num}个，正在分{page_num}页处理")
            for n in range(0, page_num):
                console.print(
                    f"[blue bold]{n}/{page_num}[/blue bold] 正在获取关注列表 [yellow]此步骤时间较长[/yellow] 根据关注数量决定最终请求时长",
                    end="\r",
                )
                response = requests.get(
                    url=f"https://api.codemao.cn/creation-tools/v1/user/followers?user_id={id}&offset={n}&limit=200"
                )
                if response.status_code == 200:
                    logger.info("请求成功，组合信息中")
                    followlist.extend(response.json()["items"])
                else:
                    logger.error(
                        f"请求{i}时发生错误：{response.status_code} {response.text}"
                    )
                    print(f"[red]请求发生错误，请检查日志![/red] {i}")
            logger.info(f"请求成功，将返回信息写入到{path}/info/{filename[now - 1]}中")
            with open(f"{path}/info/{filename[now - 1]}", "w", encoding="utf-8") as f:
                json.dump(followlist, f, ensure_ascii=False, indent=2)
                f.close()
                logger.info("写入完成")
        elif now == 7:  # 取粉丝列表total
            total_num = json.loads(requests.get(url=i, headers=headers).text).get(
                "total"
            )
            page_num = math.ceil(total_num / 200)
            logger.info(f"粉丝列表共{total_num}个，正在分{page_num}页处理")
            console.print()
            for n in range(0, page_num):
                console.print(
                    f"[blue bold]{n}/{page_num}[/blue bold] 正在获取粉丝列表 [yellow]此步骤时间较长[/yellow] 根据粉丝数量决定最终请求时长",
                    end="\r",
                )
                response = requests.get(
                    url=f"https://api.codemao.cn/creation-tools/v1/user/fans?user_id={id}&offset={n}&limit=200"
                )
                if response.status_code == 200:
                    logger.info(f"请求成功，组合信息中，第{n}页")
                    fanslist.extend(response.json()["items"])
                else:
                    logger.error(
                        f"请求{i}时发生错误：{response.status_code} {response.text}"
                    )
                    print(f"[red]请求发生错误，请检查日志![/red] {i}")
            logger.info(f"请求成功，将返回信息写入到{path}/info/{filename[now - 1]}中")
            with open(f"{path}/info/{filename[now - 1]}", "w", encoding="utf-8") as f:
                json.dump(fanslist, f, ensure_ascii=False, indent=2)
                f.close()
                logger.info("写入完成")
        else:
            response = requests.get(url=i, headers=headers)
            if response.status_code == 200:
                logger.info(
                    f"请求成功，将返回信息写入到{path}/info/{filename[now - 1]}中"
                )
                with open(
                    f"{path}/info/{filename[now - 1]}", "w", encoding="utf-8"
                ) as f:
                    f.write(str(response.text))
                    f.close()
                    logger.info("写入完成")
            else:
                logger.error(
                    f"请求{i}时发生错误：{response.status_code} {response.text}"
                )
                print(f"[red]请求发生错误，请检查日志![/red] {i}")

    return True
