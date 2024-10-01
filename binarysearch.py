def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [2, 4, 6, 8, 10]
x = 6
result = binary_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
