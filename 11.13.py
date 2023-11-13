""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt,'html.parser')
item = item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")

print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(item.get_text())

goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_text()) """

""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://news.daum.net/"
res=rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

iss= res_html.select("a,wrap_thumb")
print(iss)
print("\n----------------------------\n")

print("\n----------------------------\n")
ct = res_html.select("a.wrap_thumb")
for j in ct:
    c = j.attrs["data-tiara-custom"]
    c = j.attrs["data-tiara-id6k "]
    print(c+"\n") """
    
""" from bs4 import BeautifulSoup as bs
import requests as rq
import os
from urllib.request import urlretrieve as rl

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt,'html.parser')
imgs = res_html.select("img")
print(imgs)

linkimgs =[]

for i in imgs:
    irs = i.attrs["src"]
    print(irs + "\n")
    linkimgs.append(irs)
    
folder = "imgs/"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
i =0
for ln in linkimgs:
    if str(ln).find("//t") == False:
        print(ln)
        continue
    else:
        pass
    
    i +=1
    rl(ln, folder + f"{i}.jpg") """
    
    

""" from pandas import Series as sr
data = [10, 20,30, 40]
sdata = sr(data)
print (sdata)

import numpy as np
data = np.arange(1, 5)
sdata = sr(data)
print(sdata) """

""" from pandas import Series as sr
data = [10,20,30,40]
sdata = sr(data)
print(sdata.index)
print(sdata.index.to_list())"""

""" from pandas import Series as sr

data = [10, 20,30, 40]
sdata = sr(data)
print(sdata)
idx = ["a", "b", "c", "d"]
print("\n----------------\n")

sdata = sr(data, idx)
print(sdata) """

""" from pandas import Series as sr
dt = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]
sdata = sr(data=idx, index=dt)
print(sdata) """

""" from pandas import Series as sr
data = [10, 20,30, 40]
idx = ["a", "b", "c", "d"]

sdata = sr(data, idx)

sd = sdata.reindex(["a","j","c"])
#print(sd)

sd = sdata.reindex(["b"])
print(sdata["a"])
print(sdata.lioc[0])
print(sdata.loc["a"])

print(sd)
print(sdata["b"])
print(sdata.iloc[0]) """


""" from pandas import Series as sr

dt = ["alpha","beta","charlie","delta"]
idx = ["ab","bc","cd","de"]

sdata = sr(data=dt, index=idx)
print(sdata.loc["bc":"cd"])
print(sdata.loc["bc":])
print(sdata.loc[:"bc"])
 """
 
""" from pandas import Series as sr

dt = ["alpha","beta","charlie","delta"]
idx = ["ab","bc","cd","de"]

sdata = sr(data=dt, index=idx)
print(sdata.iloc[1:2])
print(sdata.iloc[2:])
print(sdata.iloc[:2]) """

""" from pandas import Series as sr

dt = ["alpha","beta","charlie","delta"]
idx = ["ab","bc","cd","de"]

sdata = sr(data=dt, index=idx)
sdata.loc["cd"] = "echo"
print(sdata)
 
sdata.iloc[1] ="fox"
print(sdata)

sdata.loc["ef"] = "golf"
print(sdata)

print(sdata.drop("bc"))
print(sdata.drop("cd"))
print(sdata) """

""" from pandas import Series as sr

s1 = sr([100, 200, 300], index=["a", "b", "c"])
s2 = sr([100, 200, 300], index=["b", "c", "a"])

sum = s1 + s2
print(sum)
print(sum.max())
print(sum.mean())
print(sum.min())

sub = s1 - s2
print(sub)
print(sub.max())
print(sub.mean())
print(sub.min())

mul = s1 * s2
print(mul)
print(mul.max())
print(mul.mean())
print(mul.min())

div = s1 / s2
print(div) """

""" from pandas import Series as sr

data = {
    "삼성전자": "전기,전자",
    "LG전자": "전기,전자",
    "현대차": "운수장비",
    "NAVER": "서비스업",
    "카카오": "서비스업"
}

sdata = sr(data)
uniq = sdata.unique()
print(uniq)

sc =sdata.count()
print(sc)
sv =sdata.value_counts()
print(sv) """


""" from pandas import Series as sr

idx = ["a", "b", "c", "d", "e"]
s1 = sr([1100, 270, 30, 450, 50], index=idx)
s2 = sr([150, 740, 810, 40, 25], index=idx)

fil = s1 > 300
print(fil)
print(s1[fil])
fil1 = s2 > s1
print(fil1)
print(s2[fil])
print(s2[s2 > s1].index)
 """


from pandas import Series as sr
idx = ["a", "b", "c", "d", "e"]
dt = [1100, 270, 30, 450, 50]
s1 = sr(data=dt, index=idx)
sv = s1.sort_values()
print(sv)
sv1 = s1.sort_values(ascending = False)
print(sv1)

