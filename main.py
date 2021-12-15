import sys
from logininfo import get_login_info
from question import get_questions
from submit import submit
from answer import get_answer
from config import anonymous

if __name__ == '__main__':
    questions = get_questions()

    # 获取用户的登录信息
    info = get_login_info()
    token = info.get("stoken")
    if token is None:
        print("获取用户登录信息失败，检查你的 cookie")
        sys.exit(-1)
    for question in questions:
        desc = question["desc"]
        qid = question['qid']

        # 回答问题的内容，不能少于一定字数，否则会失败
        # 可以调用 api 进行回答， 比如 https://ai.baidu.com/ai-doc/KG/6k8dhe8b5
        # 下面通过百度知道查询的结果作为提交的内容
        content = get_answer(desc)
        if content == "":
            # 跳过这个问题，不回答了
            print("跳过问题: https://zhidao.baidu.com/question/{}.html".format(qid))
            continue
        flag = submit(qid, content, token, anonymous)
        if flag:
            print("成功回答问题: https://zhidao.baidu.com/question/{}.html".format(qid))
        else:
            print("回答问题失败: https://zhidao.baidu.com/question/{}.html".format(qid))
