arr = [64,34,55,44,12,22,11,9,8]
n = len(arr)

for i in range(n):
	# print(i)
	for j in range(0,n-i-1):
		# print(j)
		if arr[j]>arr[j+1]:
			# print(arr[j])
			# print(arr[j+1])
			# print("--")
			arr[j],arr[j+1] = arr[j+1],arr[j]
			# temp=arr[j]
			# arr[j]=arr[j+1]
			# arr[j+1]=temp
print("sorted array: ",arr)

'''def bubble_sort(A):
	for i in range(len(A)):
		for k in range(len(A)-1,i,-1):
			if (A[k] < A[k-1]):
				swap(A,k,k-1)

def swap(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

A = [534,246,933, 127,277,321,454,565,220]
bubble_sort(A)
print(A)'''