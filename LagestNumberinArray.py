#a = [2, 6, 1, 4, 5, 8, 4]
a = [1,2,3,2,1]
#a=list(input())
index=0
for i in range(1, len(a)):
    temp = a[0]
    if a[i-1] < a[i]:
        temp = a[i]
        index =i
print(index)



