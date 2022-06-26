def countZeroes(x):
    ones = 0
    for i in x:
        if(i==1):
            ones+=1
    print(len(x)-ones)

n = int(input("Enter number of elements:"))
x = []
for i in range(n):
    x.append(int(input()))
countZeroes(x)