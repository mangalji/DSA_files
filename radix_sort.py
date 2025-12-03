def radix_sort(A):

	Rad = 0
	maxlength = False
	tmp, placement = -1, 1
	while not maxlength:
		maxlength = True
		buckets = [list() for _ in range(Rad)]
		print(buckets)
		# break
		for i in A:
			tmp = i//placement
			buckets[tmp % Rad].append(i)
			if maxlength and tmp > 0:
				maxlength = False
		a = 0
		for b in range(Rad):
			buck = buckets[b]
			for i in buck:
				A[a] = i
				a += 1
		#move to next digit
		placement *= Rad

A = [54,26,93,17,77,31,44,55,20]
print(radix_sort(A))