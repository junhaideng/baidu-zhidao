import re
import requests
from bs4 import BeautifulSoup
from config import headers


def get_total_page():
    """获取总页数
    源代码中有一个 
      F.context('questionListInfo', {
          totalCount: '760',
          pn: '',
          rn: '',
          isexp:'1'
      });
    获取 totalCount 即可
    """
    url = "https://zhidao.baidu.com/list"
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding

    if not resp.ok:
        print("获取源码失败")
        return 0

    pattern = re.compile(r"totalCount: '(\d+?)'")
    matches = pattern.findall(resp.text)
    if len(matches) == 0:
        print("没有找到对应的值，登录之后才能发现问题")
        return 0
    return int(matches[0])


def get_questions(max_page=30):
    url = "https://zhidao.baidu.com/list?pn={}&ie=utf8&_pjax=#j-question-list-pjax-container"
    res = []

    total = get_total_page()
    if total == 0:
        return res

    # 总页数
    pages = total / 40
    if total % 40 != 0:
        pages += 1

    if max_page < pages:
        pages = max_page

    page = 0
    while page < pages:
        print("正在获取第 {} 页的问题 id".format(page + 1))
        # 构造每一页
        resp = requests.get(url.format(page * 40), headers=headers)
        if not resp.ok:
            continue
        resp.encoding = resp.apparent_encoding

        # 查找问题链接
        soup = BeautifulSoup(resp.text, 'lxml')
        questions = soup.find_all("li", {"class", "question-list-item"})

        # 保存问题的id
        for question in questions:
            link = question.find("a", {"class": "title-link"})
            res.append({
                "qid": question.attrs['data-qid'],
                "desc": link.text.strip()
            })

        page += 1
    return res


if __name__ == '__main__':
    print(get_questions())
