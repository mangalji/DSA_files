# def insertion_sort(arr):
# 	n = len(arr)

# 	for i in range(1,n):	
# 		key = arr[i]
# 		j = i-1

# 		while j>=0 and key < arr[j]:
# 			arr[j+1] = arr[j]
# 			j -= 1
# 		arr[j+1] = key

# arr = [40,30,20,10]
# insertion_sort(arr)
# print("sorted_array: ",arr)

def insertion(A):
	n = len(A)
	for i in range(1,n):
		temp = A[i]
		k = i
		while k > 0 and temp < A[k-1]:
			A[k] = A[k-1]
			k -= 1
		A[k] = temp


A= [54,26,93,17,77,3 ,44,55,20] 
insertion(A)
print(A)