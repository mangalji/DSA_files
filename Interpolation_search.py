def InterPolation_search(A,x):
	low = 0
	high = len(A) - 1
	while A[low] <= x and A[high] >= x:
		mid = (low+((x-A[low])*(high-low))//(A[mid] - A[low]))
		if A[mid] > x:
			low = mid + 1
		elif A[mid] < x:
			high = mid - 1
		else:
			return mid 
	if A[low] == x:
		return low
	return None

InterPolation_search()