""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "data/"
if not os. path.isdir(folder):
    os.mkdir(folder)

with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
        f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
 """
  

import pandas as pd

target = "./data/apt.csv"
df =pd.read_csv(target, encoding="CP949")
df.to_csv("./data/apttt.csv", encoding="utf8")

print(df.head())


import pandas as pd

df = pd.read_csv("./data/apttt.csv", index_col=0)
print(df.head())

df = df.rename(columns={"분양가격(제곱미터)":"분양가"})
print(df) 


""" res = df.sort_values(by="지역명")
#res = df.sort_values("지역명")
#res = df.sort_values(by="지역명", ascending = False)
#res = df.sort_values(by="지역명", ascending = True)
print(res.head(10))
#print(res.head())
 """
 
""" #res = df.sort_values(by="연도")
#res = df.sort_values(by="분양가")
res = df.sort_values(by="연도")[:5]
#print(res)
print(res.head()) 
"""

""" 
#res = df["지역명"][:5]
#res = df[["지역명", "연도"]]
#res = df.loc[:, ["지역명", "연도","분양가"]]
res = df.loc[:, ["지역명", "연도","분양가"]][:7]
#res = df[["지역명", "연도"]][:5]
#print(res)
 """

""" #res = df.loc[:,["지역명", "연도"]][:5]
#res = df.loc[:][:5]
#res = df.loc[:][:]
res = df.iloc[1]
print(res)
 """
 
""" 
#res = df.loc[:6,["지역명","연도"]]
#res = df.loc[:6,["지역명","연도"]][3:]
#res = df.loc[:6,["지역명","연도"]][:3]
res = df.loc[:6,["지역명","연도"]][:7]
print(res)
 """


""" #res = df.loc[df["지역명"]=="강원"]
#res = df.loc[df["연도"] > 2020]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]]
#res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][:10]
res = df.loc[df["지역명"]=="서울",["지역명", "연도", "분양가"]][-10:]
print(res)
"""
 
df0 = df.copy()

res = df.iloc[2]
res = df.iloc[2][2]
print(res)

res = df[df.index > 3560]
print(res)

#res = df[df.연도 == 2023]
res = df[df.월 ==3]
#print(res)

#df[(df.연도 == 2023) & (df.지역명 == "서울")]
##df[(df.연도 == 2023) & (df.지역명 == "서울")]
#df[(df.연도 == 2023) & (df.지역명 == "서울") & (df.월 == 6)]
#print(res)

#columns = list(df.columns)
#print(columns+"컬럼")

#df1 = df.reindex(index=df.index[:7], columns=list(df.columns) + ["extra"])
df1 = df.reindex(columns=list(df.columns) + ["extra"])
#print(df)
#print(df1)

#df1.loc[:6,"extra"] = "0"
df1.loc[:4,"extra"] = False
print(df1)

df2 = df1.copy()

#res = df2.dropna(how="any")
#res = df2.fillna(value="text")
#res= df2.fillna(value="1234")
#res= df2.fillna(value="1234", implace=True)
#print(df2)

#res = df2.dropna(how="any", inplace=True)
#print(res)
#print(df2)

#res = pd.isna(df1)
#res = pd.isna(df)
#res = pd.isna(df0)
#res = pd.isna(df2)
#print(res)


""" 
res = df["연도"].value_counts()
res = df["지역명"].value_counts()
res = df["월"].value_counts()
res = df.월.value_counts()
print(res)
 """

res = df.groupby(["지역명", "연도", "월"]).sum()
res = df.groupby(["지역명", "연도", "월"]).all()
print(res)

res = df.groupby(["지역명", "연도", "월"])["분양가"].agg("sum")
print(res)









