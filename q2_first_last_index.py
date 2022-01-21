arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]

target = 9
# invalid_result = -1, -1
# count_target = 0
#
# if target in arr:
#     for i in range(0, len(arr)):
#         if target == arr[i]:
#             first_index = arr.index(target)
#             count_target += 1
#
#     last_index = (first_index + count_target) - 1
#     correct_result = first_index, last_index
#     print(correct_result)
# else:
#     print(invalid_result)


def first_and_last(arr1, target1):
    count = 0
    if target1 in arr1:
        for i in range(len(arr1)):
            if target1 == arr1[i]:
                count += 1
    else:
        return -1, -1
    return arr1.index(target1), (arr1.index(target1) + count) - 1


result = first_and_last(arr, target)
print(result)