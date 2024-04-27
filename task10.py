list1=[(2, 7), (2, 6), (1, 8), (4, 9)]
for i in range(0, len(list1)):
    list1[i]=list1[i][0]*list1[i][1]
a=max(list1)
b=min(list1)
print(a,b)