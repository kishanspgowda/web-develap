import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
def bubblesort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j]<a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                print(a)
a=[]
s=int(input("Enter the array size:"))
while True:
    if len(a)<s:
        arr=int(input("enter the array element:"))
        a.append(arr)
    else:
        break
    print("bifore sorting:",a)
else:
    print("after sortin:",a)
x=list(range(1,1000))
plt.plot(x,[y*y for y in x])
plt.title("bubblesort time complexity is O(n\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
