import matplotlib.pyplot as plt

""" 
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], ";"," ." , label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdot", label="PData(km)")
 """

""" # linestyle(0, (픽셀크기, 여백간격))
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (1, 0)), label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle=(0, (4, 2)), label="PData(km)")
 """
 
""" plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="r", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C1", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="C6", label="Value(m)")

plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="red", label="Value(m)")

plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#75FA8D", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], "-", color="#88FF44", label="Value(m)")
 """
 
""" 
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="round", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="solid", linewidth=10, solid_capstyle="butt", label="Value(m)")
plt.plot([1,3,5,7,9], [2,4,6,8,10], linestyle="dashed", linewidth=10, solid_capstyle="butt", label="Value(m)")
"""

"""                              	# c=cyan d=diamond
plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "k", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "y", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
 """
""" 
xdata = [2,3,6,7,10]
ydata = [1,4,5,8,9]
y1data = [2,4,6,8,10]

plt.plot(xdata,ydata)
plt.xlabel("x_data")
plt.ylabel("y_data")

plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)

plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
plt.fill_betweenx(ydata[0:4], xdata[1:3], alpha=0.3)

#plt.plot([1,3,5,7,9],[2,4,6,8,10])
plt.plot(xdata, ydata)
plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], alpha=0.5)
plt.fill_between(xdata[1:3], ydata[1:3], y1data[1:3], color ="C1")

plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)
plt.fill([1.9, 1.9, 3.1, 3.1], [0.5, 2.5, 2.5, 4.5], alpha=0.5)
 
plt.show()
 """

""" 
dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y2_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic1_val, label="value(m)")
plt.xlabel("x-data")
plt.ylabel("y-data") 
 
plt.grid()

# x축 그리드
plt.grid(axis="x")

# y축 그리드
plt.grid(axis="y")

# 색상 설정
plt.grid(axis="y", color="g")
plt.grid(axis="y", color="b")

# 투명도 설정
plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
plt.grid(axis="x", color="r", alpha=0.5, linestyle="--")
plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

plt.xticks()
plt.yticks()

# 임의 데이터 지정
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

# 라벨 지정
plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# 눈금 안쪽/바깥쪽 지정
plt.tick_params(axis="x", direction="in")
plt.tick_params(axis="x", direction="out")
plt.tick_params(axis="y", direction="in")
plt.tick_params(axis="y", direction="out")

plt.show() 
  """


x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

""" plt.bar(x_years, y_data)

plt.bar(x_years, y_data, color="g")
plt.bar(x_years, y_data, color="C7")
plt.bar(x_years, y_data, color="#88FF44")

clr=["C2","lime","r"]
plt.bar(x_years, y_data, color=clr)

plt.bar(x_years, y_data, color=clr, width=2)

plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
plt.bar(x_years, y_data, color=clr, align="center", width=0.5)

# 라인 색 선택
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)

# 테두리 라인 설정
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)


plt.xticks()
plt.yticks()
 """

plt.barh(x_years, y_data)

#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)


plt.show()


