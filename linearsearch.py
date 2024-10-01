def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 4, 6, 8, 10]
x = 6
result = linear_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
