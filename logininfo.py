import json
import time
import requests
from config import headers


# 获取登录的信息
def get_login_info():
    url = "https://zhidao.baidu.com/api/loginInfo?t={}".format(
        int(time.time()))
    h = headers.copy()

    h["Referer"] = 'https://zhidao.baidu.com'
    resp = requests.get(url, headers=h)

    resp.encoding = resp.apparent_encoding
    if not resp.ok:
        return {}

    try:
        data = json.loads(resp.text)
        return data
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    print(get_login_info())
