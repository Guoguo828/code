import requests
from bs4 import BeautifulSoup
import os

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0""",
    "cookie": """cf_clearance=Nb4xt67WqcfOzIfqBXNR9MIq3lNmMbLbzJGDeQ8tTPM-1739969394-1.2.1.1-k2jjVsjYi1_L33FFT6HbD8.RZ9qr9HQWs.Z3A1PC8gZc_4we6VKCv.H8kRBMflG1is5ytmlbk8FQ3qFe5Eg49wd3pHhW75rpIbeJ1HDk9_W5Vb.68TJOn2Zb3Tb81HfYEQA.4GRPVTF.6_Ww_99EGpxewh0bx_4IfmGjmea6S5lXnzHPGKeO7N9wc2JaqeD45G0sK6IPPrWVeZxHV4T65xdfGEzgjc2C3NVzWpEDTyDRRep.tHuGzynV5enZWZB_DjQTrNvqv0ghvgFOeDZ8ep.r7fyLYFaCn_HfdvvaZ6OqDGR2JkTtEkquCkJjlzPwbZJXCE6330kv5oWtjsJ0rw; zkhanecookieclassrecord=%2C54%2C"""
}

def craw_html(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "gbk"
    print(resp.status_code)
    html = resp.text
    return html

def parse_and_download(html):
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    
    if not os.path.exists("美女图片"):
        os.makedirs("美女图片")
    
    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"http://pic.netbian.com{src}"
        print(src)
        filename = os.path.basename(src)
        with open(f"美女图片/{filename}", "wb") as f:
            f.write(requests.get(src).content)
           # print(requests.get(src).content)
            print(f"{filename}下载成功")

urls = [f"http://pic.netbian.com/4kmeinv/index_{i}.html" for i in range(2, 6)]
for url in urls:
    html = craw_html(url)
    parse_and_download(html)