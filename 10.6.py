""" qlist = []

def enqueue(qlist,data):
    qlist.append(data)
    
def dequeue(qlist):
    data=qlist[0]
    del qlist[0]
    return data
enqueue(qlist,1)
print(qlist)

enqueue(qlist,2)
print(qlist)

enqueue(qlist,3)
print(qlist)

dequeue(qlist)
print(qlist)

dequeue(qlist)
print(qlist) """

""" #0(1)
arr=[1,2,3,4,5]
def ret_01(idx):
    return arr[idx]
print(ret_01(2)) """

""" #0(1)시간
import time
arr=[1,2,3,4,5]
def ret_01(idx):
    return arr[idx]
start = time.time()
print(ret_01(2))
end=time.time()
print(f"{end - start:5f}sec") """

""" #0(n)
arr=[1,2,3,4,5]
def print_elements(arr):
    for elem in arr:
        print(elem)
print_elements(arr)    """   

""" import time
arr=[1,2,3,4,5]
def print_elements(arr):
    for elem in arr:
        print(elem)
start = time.time()
print_elements(arr)    
end =time.time()
print(f"{end - start : 5f} sec") """


""" import time
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    print(left, right)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

my_list = [1, 2, 3, 4, 5]

start = time.time()
result = binary_search(my_list, 4)
end = time.time()
print(f"{end-start : 5f} sec")
if result != -1:
    print(f"요소가 {result}번째 인덱스에 있습니다.")
else:
    print("요소를 찾을 수 없습니다.") """
    
""" #0(n2)
def mul_for():
    for i in range(5):
        for j in range(5):
            print(i,j)
mul_for()
 """
""" import time
def mul_for():
    for i in range(5):
      for j in range(5):
            print(i,j)
start=time.time()
mul_for()
end=time.time()
print(f"{end-start:5f}sec") """

# 시험문제로 각 O() 그래프 중에 뭐가 더 빠르냐가 나올 수 있음. 
# 시험은 객곽식 문제가 꽤 많이 주관식이 3문제에서 5문제 정도. 
# 사이트에 적혀있는, 코딩했던 내용을 기반으로 나옴. 
# 객관식은 50문제 이상 나올 것 같음. 시험시간은 최대 2시간.

""" #버블
def bubble_sort(arr):
    N=len(arr)
    for i in range(N):
      for j in range(N-i-1):
         if arr[j] > arr[j+1]:
             arr[j],arr[j+1]=arr[j+1], arr[j]
         print(i,j,arr,arr[i],arr[j])
    return arr

lrr = [1,9,2,7,5]
print(bubble_sort(lrr)) """

#퀵
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left=[x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print("piv", pivot)
    print("left", left)
    print("mid",middle)
    print("rgt",right)
    
    return quick_sort(left)+middle + quick_sort(right)

my_list = [1,9,6,4,5,7,3,2]
print(len(my_list))
sorted_list=quick_sort(my_list)
print(sorted_list)