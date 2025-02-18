import requests
from bs4 import BeautifulSoup
import pandas as pd
url="http://tianqi.2345.com/Pc/GetHistory"

hearders = {
   "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36""",
    "Referer": """http://tianqi.2345.com/beijing/54511.htm""",
    "cookies":"""Hm_lvt_a3f2879f6b3620a363bec646b7a8bcdd=1739843798; Hm_lpvt_a3f2879f6b3620a363bec646b7a8bcdd=1739843798; HMACCOUNT=4B3EB197CC1A01F8; lastCountyId=54511; lastCountyTime=1739843827; lastCountyPinyin=beijing; lastProvinceId=12; lastCityId=54511"""
}
def craw_table(year,month):
    params = {
    "areaInfo[areaId]": 54511,
    "areaInfo[areaType]": 2,
    "date[year]": year,
    "date[month]": month,
    }
    resp  = requests.get(url,headers=hearders,params=params)
    print(resp.status_code)
    data = resp.json()["data"]
    df=pd.read_html(data)[0]
    return df
df_list = []
for year in range(2014,2015):
    for month in range(1,13):
        print("爬去：",year,month)
        df=craw_table(year,month)
        df_list.append(df)
pd.concat(df_list).to_excel("beijing_weather.xlsx",index=False)
