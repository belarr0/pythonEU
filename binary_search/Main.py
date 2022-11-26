import random

x = int(input("Enter num: "))

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i] #міняємо місцями
                swapped = True #для наступної ітерації

num_list = random.sample(range(-50, 101), 100)
print("Before: ", num_list)
bubble_sort(num_list)
print("After: ", num_list)

def binary_search(num_list, x):
	low = 0
	high = len(num_list) - 1
	mid = 0
	while low <= high:
		mid = (high + low) // 2
		if num_list[mid] < x:
			low = mid + 1
		elif num_list[mid] > x:
			high = mid - 1
		else:
			return mid

	return -1

#x = 85

result = binary_search(num_list, x)

if result != -1:
	print("Element at index", str(result))
else:
	print("Element is not in array")
