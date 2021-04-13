def largestNumber (a):
    index = 0
    for i in range(1, len(a)):

        temp = a[0]
        if a[i - 1] < a[i]:
            temp = a[i]
            index = i
    print(index)