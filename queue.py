import bisect

class OrderedList():

	def __init__(self):
		
		self.items = []

	def insert(self,new_element):
		position = bisect.bisect_left(self.items,new_element)
		self.items.insert(position,new_element)

	def delete(self,element):
		try:
			position = self.items.index(element)
			self.items.pop(position)
			return True
		except ValueError:
			return False

	def is_empty(self):
		return len(self.items) == 0

	def size(self):
		return len(self.items)

	def find(self,element):
		position = bisect.bisect_left(self.items,element)
		return position < len(self.items) and self.items[position] == element

	def merge(self,another_list):
		result = OrderedList()

		i=0
		j=0

		while i < len(self.items) and j < len(another_list.items):
			if self.items[i] <= another_list.items[j]:
				result.items.append(self.items[i])
				i += 1
			else:
				result.items.append(another_list.items[j])
				j += 1        

		result.items.extend(self.items[i:])
		result.items.extend(another_list.items[j:])
        
		return result

	def display(self):
		if self.is_empty():
			print("[empty]")
		else:
			print("[", end=" ")
			print(", ".join(str(x) for x in self.items), end=" ")
			print("]")

	def get_min_value_item(self):
		return self.items[0] if self.items else None

	def get_max_value_item(self):
		return self.items[-1] if self.items else None

	def split_at(self,position: int):
		if position < 0 or position >= len(self.items):
			raise ValueError(f"Position must be between 0 and {len(self.items)-1}")
		
		left = OrderedList()
		right = OrderedList()
		
		left.items = self.items[:position+1]
		right.items = self.items[position+1:]
		
		return left, right

	def clear(self):
		self.items.clear()

	def __str__(self):
		return str(self.items)

	def __len__(self):
		return len(self.items)

	def __contains__(self, item):
		return self.find(item)



# ────────────────────────────────────────────────
# Example usage
# ────────────────────────────────────────────────
if __name__ == "__main__":
	ol = OrderedList()
   
	print("Empty?", ol.is_empty())          # True
	ol.insert(50)
	ol.insert(20)
	ol.insert(80)
	ol.insert(35)
	ol.insert(10)
	ol.insert(60)
    
	print("After inserts:")
	ol.display()                            # [ 10, 20, 35, 50, 60, 80 ]
    
	print("Find 35?", ol.find(35))          # True
	print("Find 99?", ol.find(99))          # False
    
	print("Delete 20 →", ol.delete(20))     # True
	print("Delete 999 →", ol.delete(999))   # False
    
	ol.display()                            # [ 10, 35, 50, 60, 80 ]
    
	print("Min:", ol.get_min_value_item())             # 10
	print("Max:", ol.get_max_value_item())             # 80
    
    # Merge example
	ol2 = OrderedList()
	ol2.insert(15)
	ol2.insert(40)
	ol2.insert(70)
	print("after initilize 2nd list: ")
	ol2.display()
	merged = ol.merge(ol2)
	print("Merged:")
	merged.display()                        # [ 10, 15, 35, 40, 50, 60, 70, 80 ]
    
    # Split example
	print("After splitting between 2 list: ")
	left, right = merged.split_at(3)
	print("Left:")
	left.display()                          # [ 10, 15, 35, 40 ]
	print("Right:")
	right.display()                         # [ 50, 60, 70, 80 ]






# // ----------------------------------------------------------------------
# // ORDERED LIST (Sorted Array Implementation)
# // Elements are always kept in non-decreasing order
# // ----------------------------------------------------------------------

# // Type definition (conceptual)
# OrderedList:
#     items[]     // array of elements (can be int, string, etc.)
#     size        // current number of elements
#     capacity    // maximum size before resize (for dynamic version)

# // ──────────────────────────────────────────────────────────────────────
# // 1. Initialization / Create empty ordered list
# // ──────────────────────────────────────────────────────────────────────
# Initialize(OrderedList L):
#     L.size ← 0
#     L.capacity ← INITIAL_CAPACITY   // e.g. 10 or 16
#     allocate L.items[0..L.capacity-1]
#     // or in dynamic languages: L.items ← empty array


# // ──────────────────────────────────────────────────────────────────────
# // 2. isEmpty(list) → boolean
# // ──────────────────────────────────────────────────────────────────────
# isEmpty(OrderedList L) → boolean:
#     return L.size == 0


# // ──────────────────────────────────────────────────────────────────────
# // 3. isFull(list) → boolean
# //    (only meaningful in fixed-size version; often omitted in dynamic)
# // ──────────────────────────────────────────────────────────────────────
# isFull(OrderedList L) → boolean:
#     return L.size == L.capacity


# // ──────────────────────────────────────────────────────────────────────
# // 4. insert(list, newElement)
# //    Inserts newElement in correct sorted position
# // ──────────────────────────────────────────────────────────────────────
# insert(OrderedList L, newElement):
#     if isFull(L):
#         resize L to about 1.5× or 2× current capacity   // dynamic version
#         // or return error / overflow in fixed-size version

#     // Find the correct position using binary search
#     pos ← binarySearchForInsertionPosition(L, newElement)

#     // Shift all elements from pos to the right
#     for i ← L.size-1 down to pos:
#         L.items[i+1] ← L.items[i]

#     L.items[pos] ← newElement
#     L.size ← L.size + 1


# // Helper: Find where to insert (first position ≥ newElement)
# binarySearchForInsertionPosition(OrderedList L, key):
#     left ← 0
#     right ← L.size

#     while left < right:
#         mid ← (left + right) / 2
#         if L.items[mid] < key:
#             left ← mid + 1
#         else:
#             right ← mid

#     return left


# // ──────────────────────────────────────────────────────────────────────
# // 5. delete(list, elementToDelete)
# //    Removes first occurrence of elementToDelete
# //    Returns true if deleted, false if not found
# // ──────────────────────────────────────────────────────────────────────
# delete(OrderedList L, elementToDelete) → boolean:
#     pos ← binarySearch(L, elementToDelete)

#     if pos == -1 or L.items[pos] != elementToDelete:
#         return false

#     // Shift left to fill the gap
#     for i ← pos to L.size-2:
#         L.items[i] ← L.items[i+1]

#     L.size ← L.size - 1
#     return true


# // Helper: Standard binary search – returns index or -1
# binarySearch(OrderedList L, key) → integer:
#     left ← 0
#     right ← L.size - 1

#     while left <= right:
#         mid ← (left + right) / 2
#         if L.items[mid] == key:
#             return mid
#         else if L.items[mid] < key:
#             left ← mid + 1
#         else:
#             right ← mid - 1

#     return -1


# // ──────────────────────────────────────────────────────────────────────
# // 6. display(list)
# // ──────────────────────────────────────────────────────────────────────
# display(OrderedList L):
#     if isEmpty(L):
#         print "[empty]"
#         return

#     print "[ "
#     for i ← 0 to L.size-1:
#         print L.items[i]
#         if i < L.size-1: print ", "
#     print " ]"


# // ──────────────────────────────────────────────────────────────────────
# // 7. find(list, item) → boolean   (or position)
# // ──────────────────────────────────────────────────────────────────────
# find(OrderedList L, item) → boolean:
#     return binarySearch(L, item) != -1


# // ──────────────────────────────────────────────────────────────────────
# // 8. merge(list1, list2) → new ordered list
# //    Merges two already sorted lists into one sorted list
# // ──────────────────────────────────────────────────────────────────────
# merge(OrderedList L1, OrderedList L2) → OrderedList:
#     result ← new OrderedList

#     i ← 0    // index in L1
#     j ← 0    // index in L2

#     while i < L1.size and j < L2.size:
#         if L1.items[i] <= L2.items[j]:
#             insert(result, L1.items[i])   // or append & increment i
#             i ← i + 1
#         else:
#             insert(result, L2.items[j])
#             j ← j + 1

#     // Copy remaining elements
#     while i < L1.size:
#         insert(result, L1.items[i])
#         i ← i + 1

#     while j < L2.size:
#         insert(result, L2.items[j])
#         j ← j + 1

#     return result


# // ──────────────────────────────────────────────────────────────────────
# // 9. splitList(list, position) → two ordered lists
# //    Splits after position k (0-based)
# // ──────────────────────────────────────────────────────────────────────
# splitList(OrderedList L, k) → (OrderedList left, OrderedList right):
#     left ← new OrderedList
#     right ← new OrderedList

#     if k < 0 or k >= L.size:
#         // error handling
#         return (empty, copy of L)   // or throw error

#     for i ← 0 to k:
#         insert(left, L.items[i])    // or just copy

#     for i ← k+1 to L.size-1:
#         insert(right, L.items[i])

#     return (left, right)