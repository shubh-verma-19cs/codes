
def highest_element(arr):
    n = len(arr)
    highest = arr[0]
    for i in range(n):
        if highest<arr[i]:
            highest = arr[i]
    
    return highest

n = int(input("Enter no. of elements of array 1:"))
arr = []
for i in range(n):
    arr.append(int(input()))

print("\n",highest_element(arr))