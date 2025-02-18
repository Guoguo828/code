import requests
from bs4 import BeautifulSoup
import pandas as pd
def get_novel_chapters():
     root_url = "https://www.bi03.cc/read/44107/"
     r=requests.get(root_url)
     r.encoding="utf-8"
     soup=BeautifulSoup(r.text,"html.parser")
     data=[]
     for dd in soup.find_all("dd"):
          
          link=dd.find("a")
          if not link:
                continue
          data.append(("https://www.bi03.cc%s"%link.get("href"),link.get_text()))
     return data
def get_chapter_content(url):
      r=requests.get(url)
      r.encoding="utf-8"
      soup=BeautifulSoup(r.text,"html.parser")
      content=soup.find("div",id="chaptercontent").get_text()
      return content
num=0
novel_chapters = get_novel_chapters()
total = len(novel_chapters)
title_list = []
for chapter in get_novel_chapters():
      url,title = chapter
      if(num>12):
             break
      num+=1
      title_list.append({title,url})
     
      print(num,total)
      print(url)
      if url=="https://www.bi03.ccjavascript:dd_show()":
                  continue
      with open("%s.txt"%title,"w") as fout:  
            fout.write(get_chapter_content(url))
df = pd.DataFrame(title_list)
df.to_excel("novel.xlsx",index=False)