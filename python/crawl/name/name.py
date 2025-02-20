import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urlencode
import time

url = "https://life.httpcn.com/xingming.asp"

def get_score(xing, ming):
    data = {
        "isbz": 1,
        "xing": xing.encode("gb2312",errors='ignore'),
        "ming": ming.encode("gb2312",errors='ignore'),
        "sex": 1,
        "data_type": 0,
        "year": 1980,
        "month": 2,
        "day": 20,
        "hour": 20,
        "minute": 10,
        "pid": "北京".encode("gb2312"),
        "cid": "北京".encode("gb2312"),
        "wxxy": 0,
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "check_agree": "agree",
        "act": "submit"
    }

    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://life.httpcn.com/xingming.asp",
        "cookie": """Hm_lvt_668a2b1ccec82d575177212da2570e5d=1740019131,1740054294; HMACCOUNT=F0D2ED9610372EC8; ASPSESSIONIDQWDRDCBD=DNKEEFBDOOGPCIHAOPFODOBF; input%5FRenYue=; input%5Fsex=1; input%5Fday=20; input%5Fdata%5Ftype=0; iscookies=yes; input%5Fzty=; input%5Fmonth=2; input%5Fyear=1980; input%5Fhour=20; input%5Fxing=%D2%A6; input%5Fminute=10; input%5Fname=%D2%A6%B4%F3; input%5Fpid=%B1%B1%BE%A9; input%5Fcid=%B1%B1%BE%A9; input%5Fming=%B4%F3; Hm_lpvt_668a2b1ccec82d575177212da2570e5d=1740055783""",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
    }

    response = requests.post(url, data=urlencode(data), headers=headers)
    response.encoding = "gb2312"
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    divs = soup.find_all("div", class_="chaxun_b")
    bazi, wuge = 0, 0
    for div in divs:
        if "姓名五格评分" not in div.get_text():
            continue

        fonts = div.find_all("font")
        # print(fonts)
        wuge = fonts[0].get_text().replace("分", "").strip()
        bazi = fonts[1].get_text().replace("分", "").strip()
    return "%s%s" % (xing, ming), bazi, wuge

# print(get_score("李", "明"))
num=0
"""with open("input_name.txt", "r", encoding="utf-8") as fin, open("output_name.txt", "w", encoding="utf-8") as fout:
    for line in fin:
        num+=1
        line = line.strip()
        print(line)
        if len(line) == 2:
            xingming, bazi, wuge = get_score(line[0], line[1])
            print(bazi, wuge)
            fout.write("%s\t%s\t%s\n" % (xingming, bazi, wuge))
        else:
            xingming, bazi, wuge = get_score(line[0], line[1] + line[2])
            print(bazi, wuge)
            fout.write("%s\t%s\t%s\n" % (xingming, bazi, wuge))
        if(num==5):
            time.sleep(2)
            num=0"""
print(get_score("姚","济宇"))