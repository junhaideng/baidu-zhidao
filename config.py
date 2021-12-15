import json
import os
import sys

if not os.path.exists("config.json"):
    print("config.json not exist")
    sys.exit(-1)

with open("config.json", 'r') as f:
    data = json.load(f)

if data.get('cookie') is None:
    print("can not find parameter `cookie`")
    sys.exit(-1)

if data.get("anonymous") is None:
    print("can not find parameter `anonymous`")
    sys.exit(-1)

# cookie 手动登录之后会生成，复制到这里，一定不能为空
headers = {
    "Cookie": data.get("cookie"),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53",
}

anonymous = data.get("anonymous")  # 1 表示匿名，0 表示不匿名回答
