""" import pandas as pd

df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print("\n----------------\n")

print(df[1])
print("\n----------------\n")

print(df[1][1]) """




""" import pandas as pd
data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print("\n----------------\n")

print(fr["x"])
print("\n----------------\n")

print(fr.x)
print("\n----------------\n")

print(fr.iloc[2])
print("\n----------------\n")

print(fr.loc["y축"])
print("\n----------------\n")

frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
print(frs)
print("\n----------------\n")

frs["t"] = [60, 120, 180]
print(frs)
print("\n----------------\n")

frs.loc["t축"] = [100, 200, 300, 400]
print(frs)
print("\n----------------\n")

frs.loc["t축"] = [500, 600, 700, 800]
print(frs)
print("\n----------------\n")

frs.drop("x", axis=1, inplace=True)
print(frs)
print("\n----------------\n")

frs.drop("x축", inplace=True)
print(frs)
 """
 
""" 
import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
print("\n----------------\n")

print(df["x"])
print("\n----------------\n")

print(df.loc["x축"])
print("\n----------------\n")

print (df["col1"])
print("\n----------------\n")

print(df+1)
print("\n----------------\n")

print(df.div(100))
print("\n----------------\n")

print(df/100)
print("\n----------------\n")

print(df.mul(100))

dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])
print(df2)
print("\n----------------\n")

print(df.div(df2))
print("\n----------------\n")

print(df.div(df2,fill_value=0))
 """


""" import pandas as pd

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["col1","col2","col3"]
idx = ["삼성","현대","LG"]

df = pd.DataFrame(data=dt,index=idx,columns=col)

print(df)
print("\n----------------\n")

print(df["col1"])
print("\n----------------\n")

print(df.loc["현대"])
print("\n----------------\n")

print (df["col1"])
print("\n----------------\n")

print(df+1)
print("\n----------------\n")

print(df.div(100))
print("\n----------------\n")

print(df/100)
print("\n----------------\n")

print(df.mul(100))
print("\n----------------\n")

dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["삼성","현대","LG"],columns=["col2"])
print(df2)
print("\n----------------\n")

print(df.div(df2))
print("\n----------------\n")

print(df.div(df2,fill_value=100)) """


""" import pandas as pd

idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)
print("\n----------------\n")

print(df.loc["row1"])
print("\n----------------\n")

print(df.iloc[0])
print("\n----------------\n")

print(df.loc[("row2", "val3")])
print("\n----------------\n")

print(df.loc[("row3", "val3"), "col1"]) """


""" import numpy as np
import pandas as pd

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

print(df)
print("\n----------------\n")

print(df[2])
print("\n----------------\n")

print(df.loc[2])
print("\n----------------\n")

print(df.loc[3][1])
print("\n----------------\n")

print(df.head(2))
print("\n----------------\n")

print(df.tail(3))
print("\n----------------\n")

print(df.sample(2)) 
"""

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

import pandas as pd
folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)
#print(df.values[0])

print(df.head())
print("\n----------------\n")

print(df.head(3))
print("\n----------------\n")

print(df.tail())
print("\n----------------\n")

print(df.tail(3))
print("\n----------------\n")

print(df.sample())
print("\n----------------\n")

print(df.sample(4))
print("\n----------------\n")

print(df.index)

print(df.dtypes)
print(type(df))

print(df.values)
print(df.values[1])

for el in df.values[0] :
    print(el)
    
print(df.info())

print(df.values)

print(df.isnull())

print(df.isnull().sum())

print(df.name)

print(df.postcode)

print(df.color)

print(df.id)

print(df["name"])

print(df["color"])

print(df[["name", "id"]])

print(df[["name", "address", "postcode"]])

print(df.postcode.describe())
print(df.color.describe())

print(df.color.count())
print(df.color.value_counts())

temp= df.postcode.sum() / df.name.count()
print(temp)

print(df.name == "김병철")
print(df[df.color == "Beige"].head(1))
print(temp)







