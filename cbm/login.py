"""
-*- coding: utf-8 -*-
@File: main.py
@author: WangZixu
"""

from fake_useragent import UserAgent
import requests
import json

headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "User-Agent": UserAgent().random,
}


def login_user(phone: str, password: str):
    response = requests.post(
        url="https://api.codemao.cn/tiger/v3/web/accounts/login",
        json={"pid": "65edCTyg", "identity": phone, "password": password},
        headers=headers,
    )
    if response.status_code == 200:
        return (
            True,
            str(json.loads(response.text).get("user_info", {}).get("nickname")),
            str(json.loads(response.text).get("auth", {}).get("token")),
            str(json.loads(response.text).get("user_info", {}).get("id"))
        )
    else:
        return False, str(response.status_code), str(response.text)


def logout_user(token: str):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": UserAgent().random,
        "authorization": f"Bearer {token}",
    }
    requests.post(
        url="https://api.codemao.cn/tiger/v3/web/accounts/logout",
        json={},
        headers=headers,
    )
    return True
