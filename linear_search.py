def linear_search(A,x):
	
	found = False
	n = len(A)

	for i in range(n):
		if x == A[i]:
			print(f"Element found at index {i}.")
			found = True
			break

	if found != True:
		print("Element not found..")

A = [2,3,5,8,12,34,3,16]
x = 8
linear_search(A,x)
