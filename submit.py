import json
import requests
from config import headers
from logininfo import get_login_info


def submit(question_id, content, token, anoy=1):
    """回答问题
        question_id (str): 问题id
        content (str): 回答的内容
        token (str): 头部的token，通过 login info 获取
        anoy (int): 是否匿名， 0 非匿名. Defaults to 1.
    """
    data = "cm=100009&qid={}&title=&answerfr=&feedback=0&entry=list_default_all&co={}&cite=&rich=1&edit=new&anoy={" \
           "}&utdata=16,53,14,16,15,16,14,16,14,16,15,16,14,16,15,16,14,16,15,16,14,53,13,8,8,13,12,15,53,13,9,12,12," \
           "16,13,12,12,12,16373760660601".format(
               question_id, content, anoy)
    header = headers.copy()

    header["X-ik-token"] = token
    header["Content-Type"] = 'application/x-www-form-urlencoded'

    resp = requests.post(url="https://zhidao.baidu.com/submit/ajax/",
                         headers=header, data=data.encode("utf-8"))

    resp.encoding = resp.apparent_encoding

    if not resp.ok:
        print("提交失败", resp.text)
    try:
        data = json.loads(resp.text)
        # 成功提交问题
        if data['errorNo'] == "0":
            return True
        else:
            print("回答失败: ", data.get("data").get("info"))
    except Exception as e:
        print("回答失败：", e)
    return False


if __name__ == '__main__':
    info = get_login_info()
    submit("1375299619230464579", "简单的测试一下", info.get("stoken"))
