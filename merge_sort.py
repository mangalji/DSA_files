# def merge_sort(A):
# 	if len(A)>1:
# 		mid = len(A)//2
# 		left = A[:mid]
# 		right = A[mid:]
# 		merge_sort(left)
# 		merge_sort(right)
# 		i = j = k = 0
# 		while i < len(left) and j < len(right):
# 			if left[i] < right[j]:
# 				A[k] = left[i]
# 				i += 1
# 			else:
# 				A[k] = right[j]
# 				j += 1
# 			k += 1

# 		while i < len(left):
# 			A[k] = left[i]
# 			i += 1
# 			k += 1

# 		while j < len(right):
# 			A[k] = right[j]
# 			j += 1
# 			k += 1

# A = [534,246,933,127,277,321,454,565,220]
# merge_sort(A)
# print(A)




'''def merge_sort(arr):
	
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	print(mid)
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left,right)

def merge(left,right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		print(left[i])
		print(right[j])
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
			print("in if codition: ",result)
		else:
			result.append(right[j])
			j += 1
			print("in else condition: ",result)
	print(result)
	result.extend(left[i:])
	result.extend(right[j:])
	print(result)
	return result

numbers = [54,26,93,17,77,31,44,55,20]
print("sorted array by merge sort: ",merge_sort(numbers))'''




def mergeSort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	# print(mid)
	# left_array = arr[:mid]
	# right_array = arr[mid:]

	left = mergeSort(arr[:mid])
	# print(left)
	right = mergeSort(arr[mid:])
	# print(right)

	return merging(left,right)

def merging(left,right):
	# print(left)
	# print(right)
	sorted_array = []
	i = j = 0

	while i < len(left) and j < len(right):
		# print(i)
		# print(j)
		# print(left[i])
		# print(right[j])
		if left[i] <= right[j]:
			sorted_array.append(left[i])
			i += 1
			# print(sorted_array)
		else:
			sorted_array.append(right[j])
			j += 1
			# print(sorted_array)

	sorted_array.extend(left[i:])
	sorted_array.extend(right[j:])
	# print(sorted_array)
	return sorted_array

arr = [12,13,14,8,7,15,9,41,1]
print(mergeSort(arr))
# print(arr)

