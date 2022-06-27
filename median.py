def getMedian(ar1, ar2, n, m) :

	i = 0 
	j = 0 
	m1, m2 = -1, -1

	if((m + n) % 2 == 1) :	
		for count in range(((n + m) // 2) + 1) :		
			if(i != n and j != m) :			
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1			
			elif(i < n) :			
				m1 = ar1[i]
				i += 1
		
			else :			
				m1 = ar2[j]
				j += 1		
		return m1
	
	else :
		for count in range(((n + m) // 2) + 1) :		
			m2 = m1
			if(i != n and j != m) :		
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1			
			elif(i < n) :			
				m1 = ar1[i]
				i += 1
			
			else :			
				m1 = ar2[j]
				j += 1		
		return (m1 + m2)//2

n = int(input("Enter no. of elements of array 1:"))
arr1 = []
for i in range(n):
    arr1.append(int(input()))

m = int(input("Enter no. of elements of array 2:"))
arr2 = []
for i in range(m):
    arr2.append(int(input()))

print(arr1,arr2)
# ar1 = [900]
# ar2 = [5, 8, 10, 20]
# n1 = len(ar1)
# n2 = len(ar2)
print(getMedian(arr1, arr2, n, m))
