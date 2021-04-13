def LongestArithmeticSubsequence (a):
    sequence=[]
    for i in range(0, len(a)):
        if(i==1):
            temp1 = a[i] - a[i - 1]
            temp2 = a[i] - a[i + 1]
            if(temp1+temp2==0):
                sequence.append(a[i])
                sequence.append(a[i - 1])
                sequence.append(a[i + 1])
        if(i>2):
            temp1 = a[i] - a[i - 1]
            temp2 = a[i - 1] - a[i - 2]
            if (temp1 == temp2):
                sequence.append(a[i])
                sequence.append(a[i - 1])
                sequence.append(a[i - 2])

    print(sequence)
    return sequence.__len__()

aay2 = [int(i) for i in input().split(',')]
print(LongestArithmeticSubsequence(aay2))