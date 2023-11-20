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
            temp.color_name() + "\n") """


""" import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

print(df.name == "김병철")

temp = df[df.postcode > 70000]
print(temp)

res = df[df.color == "Beige"].head(1)
print(res)

res2 = df[df.postcode > 70000][["name", "postcode"]]
print(res2)
print(res2.count())

temp2 = df.postcode.mean()
print(temp2)

temp3 = df[df.color == 'Ivory'].postcode.mean()
print(temp3)

temp4 = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
print(temp4) """


""" import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

temp = df.company.isnull()
for el in temp:
    if el == True:
        print(el)
#print(temp)

temp2 = df[df.company.isnull()][["name","postcode"]]
print(temp2) """

""" import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

temp = df[(df.color == "Beige")]
print(temp)

temp2 =df[~(df.color == "Beige")][["name"]]
#print(temp2.color.count())
print(temp2)

temp3 = df[(df.color == "Beige") & (df.postcode > 70000)]
print(temp3)

temp4 = df[(df.color == "Beige") | (df.postcode > 70000)][["name"]]
print(temp4)

#temp5 = df.sort_values("postcode")
temp5 = df.sort_values("name", ascending=False)
print(temp5) """


import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)

#print(df.pivot(index='Machine',columns='Country',values='Price'))
print(df.pivot(index='Brand',columns='Machine',values='Price'))
