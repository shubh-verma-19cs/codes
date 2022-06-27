'''
i is beginning, j is ending
minPalPartition(str,i,j) = 0 if i>=j
minPalPartition(str,i,j) = 0 if str[i..j] is palindrome

minPalPartition(str,i,j) = Min{minPalPartition(str,i,k) + 1 + minPalPartition(str,k+1,j)} where k varies from i to j-1
'''

import sys #sys.maxsize

def isPalindrome(str):
    return (str == str[::-1])

def minPalPartition(str,i,j):
    if i>=j or isPalindrome(str[i:j+1]):
        return 0
    min_cuts = sys.maxsize
    for k in range(i,j):
        no = (minPalPartition(str,i,k) + 1 + minPalPartition(str,k+1,j))
        min_cuts = min(min_cuts,no)

    return min_cuts

str = "geek"
print(minPalPartition(str,0,len(str)-1))
