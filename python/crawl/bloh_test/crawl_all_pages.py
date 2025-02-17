import sys
sys.path.append('./')
from utils import url_manager
import requests
from bs4 import BeautifulSoup
import re

root_url = "http://www.crazyant.net"

urls = url_manager.UrlManager()
urls.add_new_url(root_url)
fout = open("crawl_all_pagea.txt", "w",encoding="utf-8")
fout.flush()

while urls.has_new_url():
    curr_url = urls.get_new_url()
    try:
        r = requests.get(curr_url, timeout=3)
        r.raise_for_status()  # 检查请求是否成功
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        continue

    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string if soup.title else "No Title"
    fout.write("%s\t%s\n" % (curr_url, title))
    print(title)
    print("success: %s , %s ,%d" % (curr_url, title, len(urls.new_urls)))
    fout.flush()
    

    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href is None:
            continue
        if re.match(r'^http://www.crazyant.net/\d+.html$', href):
            urls.add_new_url(href)

fout.close()