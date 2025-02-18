import requests
from bs4 import BeautifulSoup
import pandas as pd

page_index = range(0, 250, 25)
headers = {
    
    "Referer": "https://movie.douban.com/top250",
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0""",
    "cookies": """ll="118172"; bid=0yj3q6XEIuE; __utmc=30149280; __utmz=30149280.1739797990.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="287076254:xO8j3S5SVLc"; ck=eNNM; __utmc=223695111; __utmz=223695111.1739798059.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=72d9be8dbb2a785e.1739798059.; __yadk_uid=6T5f1yXjfrqoxruRXJi221fDeBLSL2iU; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D594C3C12969D6CA74BA32819DC29163A|a6e89fbad367219d6251b1817aa088b4; __utma=30149280.418562719.1739797990.1739797990.1739802627.2; __utma=223695111.1081733987.1739798059.1739798059.1739802627.2; __utmb=223695111.0.10.1739802627; __utmt_t1=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1739802627%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1; __utmb=30149280.9.8.1739802802621; RT=s=1739802818077&r=https%3A%2F%2Fmovie.douban.com%2Ftop250"""
}

def download_all_htmls():
    htmls = []
    for idx in page_index:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("crawling html:", url)
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(r.status_code)
            break
        r.encoding = 'utf-8'  # 手动设置编码
        htmls.append(r.text)
    return htmls

def parse_single_html(html):
    soup = BeautifulSoup(html, "html.parser")
    article_items = (
        soup.find("div", class_="article")
        .find("ol", class_="grid_view")
        .find_all("div", class_="item")
    )
    datas = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_="hd").find("span", class_="title").get_text()
        stars = info.find("div", class_="bd").find("div", class_="star").find_all("span")
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()
        datas.append({
            "rank": rank,
            "title": title,
            "rating_star": rating_star.replace("rating", "").replace("-t", ""),
            "rating_num": rating_num,
            "comments": comments.replace("人评价", "")
        })
    return datas

htmls = download_all_htmls()
all_datas = []
for html in htmls:
    all_datas.extend(parse_single_html(html))
df = pd.DataFrame(all_datas)
df.to_excel("douban_top250.xlsx", index=False)