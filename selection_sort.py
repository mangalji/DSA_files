def selection_sort(A):
	n = len(A)
	for i in range(n):
		mini = i
		for k in range(i+1,n):
			if A[k] < A[mini]:
				mini = k
		A[mini], A[i] = A[i], A[mini]
		# swap(A,mini,i)

# def swap(A,x,y):
# 	temp = A[x]
# 	A[x] = A[y]
# 	A[y] = temp


A = [54,26,93,17,77,31,44,55,20]
selection_sort(A)
print(A)