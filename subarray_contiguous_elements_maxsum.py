from array import array
import sys

def sum_subarray(array):
    max = -1*sys.maxsize
    count = 0

    for i in range(len(array)):
        count+=array[i]
        if(count>max):
            max = count

        if(count<0):
            count=0
    
    return max


n = int(input("Enter number of elements:"))
array = []
for i in range(n):
    array.append(int(input()))

print(sum_subarray(array))