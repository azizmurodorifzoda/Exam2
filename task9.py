list1=input().split()
n=len(list1)
for i in range(0,len(list1)-1):
    list1[i+1]=list1[i]
print(list1)
