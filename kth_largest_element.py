arr = [4, 2, 9, 7, 5, 6, 7, 1, 3]
k = 4


# def kth_largest(arr1, k1):
#
#     sort_arr = sorted(arr1)
#     largest = sort_arr[len(arr1) - k1]
#     print(largest)

# or

def kth_largest(arr1, k1):
    for i in range(k - 1):
        arr1.remove(max(arr1))
    return max(arr1)


result = kth_largest(arr, k)
print(result)