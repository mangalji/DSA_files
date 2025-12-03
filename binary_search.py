def binary_search(A,x):
	n = len(A)
	low = 0
	high = n-1

	while low <= high:
		mid = (low + high)//2

		if x == A[mid]:
			return mid

		elif x > A[mid]:
			low = mid + 1

		else:
			high = mid - 1

A = [5,12,15,20,25,30,50]
x = 25
print(binary_search(A,x))
