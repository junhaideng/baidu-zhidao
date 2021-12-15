import requests
from bs4 import BeautifulSoup
from config import headers


def get_question_answer(url):
    """从百度知道问题中获取到最好的回答

    Args:
        url (str): 问题链接
    """
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding

    if not resp.ok:
        return ""

    soup = BeautifulSoup(resp.text, 'lxml')
    # 最好的回答
    anwser = soup.find("div", {"class": "best-text mb-10"})

    if anwser is None:
        return ""
    # 删除多余的一部分内容，以去掉其中的文字
    mask = anwser.find("div", {"class": "wgt-best-mask"})
    if mask is not None:
        mask.clear()

    return anwser.text.strip()


def get_answer(question):
    """通过百度搜索获取答案

    Args:
        question (str): 问题的内容
    """
    url = "https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&dyTabStr=null&word={}".format(
        question)
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding

    if not resp.ok:
        return ""

    # 找到第一个符合的
    soup = BeautifulSoup(resp.text, 'lxml')
    answer = soup.find("a", {"class": "ti"})
    href = answer.attrs["href"]
    return get_question_answer(href)


if __name__ == '__main__':
    print(get_answer("刚出满月的猫可以吃麦德氏汪喵双利益生菌吗"))
