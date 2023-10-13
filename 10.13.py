# 미니 프로젝트들 중 한 문제를 시험문제로 출제
""" 
#1-1
for i in range (1, 6):
    print("*"*(6-i))
#for i in range(5,0,-1):
#    print("*"*i)

#1-2
for i in range (1, 6):
    print("*"*i)

#1-3  
for i in range (1,6):
    spaces = " "*(6-i)
    stars = "*"*(2*i-1)
    print(spaces + stars)
    
#1-4
for i in range(6,0,-1):
    spaces = " "*(6-i)
    stars = "*"*(2*i-1)
    print(spaces + stars)
     """
""" #2-1
num=0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line =[]
    
#2-2
n=0
line = []
for i in range(1,6):
    for j in range(1,6):
        n = ((j-1)*5)+i
        line.append(n)
    print (line)
    line=[]
    
#2-3
n=26
line=[]
for i in range(5):
    for j in range(5):
        n -= 1
        line.append(n)
    print(line)
    line =[]
"""
 
""" #3
import random

def get_computer_choice():
    choices = ['1','2','3']
    return random.choice(choices)

def determine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum:
        print("무승부")
        return
    elif (
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return
    
print("1 : 가위")
print("2 : 바위")
print("3 : 보")
print("1~3 숫자를 입력하세요!")
chnum = input()

determine_winner(chnum) """

""" file = open("temp.txt", "w")
file.close()
file = open("temp.txt", "r")
file.close()
file = open("temp.txt", "a")
file.close()
file = open("temp.txt", "r+")
file.close() """

""" file = open("temp.txt", "w")
file.write("hello")
file.write("world")
file.close() """

""" file = open("temp.txt", "w")
file.write("hello\n")
file.write("world")
file.close() """


""" f = open ("C:\\Users\\foryo\\temp.txt", "w")
for i in range(100):
    f.write(f"{i}\n")
f.close() """

""" f = open ("C:\\Users\\foryo\\temp.txt", "a")
f.write("hello\n")
f.write("world")
f.close() """

""" file = open("temp.txt", "r")
res = file.readline()
print(res)
file.close() """

""" file = open("C:\\Users\\foryo\\temp.txt", "r")
res = file.read()
print(res)
file.close() """

""" file = open("C:\\Users\\foryo\\temp.txt", "r")
for i in range(110):
    res = file.readline()
    print(res)
file.close() """

""" file = open("C:\\Users\\foryo\\temp.txt", "r")
res = file.readlines()
print(res)
file.close() """

""" file = open("C:\\Users\\foryo\\temp.txt", "r")
line = file.readlines()
for i in line:
    print(i)
file.close() """

file = open("C:\\Users\\foryo\\temp.txt", "r")
for line in file:
    print(line)
file.close()


