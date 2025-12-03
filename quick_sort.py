import random

def quick_sort(A,low,high):
	if low < high:
		pivot = Partition(A,low,high)
		quick_sort(A,low,pivot-1)
		quick_sort(A,pivot + 1,high)

def Partition(A, low, high):
	pivot = low
	# A[pivot], A[high] = A[high], A[pivot]
	swap(A,pivot,high)
	for i in range(low, high):
		if A[i] <= A[high]:
			swap(A,i,low)
			low += 1

	swap(A,low,high)
	return low

def swap(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

A = [534,246,933,127,277,321,454,565,220]
quick_sort(A,0,len(A)-1)
print(A)


