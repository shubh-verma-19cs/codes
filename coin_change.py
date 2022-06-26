def count(S, m, n):
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
    return table[n]

m = int(input("Enter number of elements:"))
arr = []
for i in range(m):
    arr.append(int(input()))

i = len(arr)
n = int(input("Enter value of N:"))
x = count(arr, i, n)
print (x)