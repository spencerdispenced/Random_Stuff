# [2,7,12,15,10]    9

# given array and target, find indexes that return target


def find_indexes(arr, target):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []


arr1 = [10, 7, 2, 15, 1]


print(find_indexes(arr1, 25))
print(find_indexes(arr1, 17))
print(find_indexes(arr1, 9))
print(find_indexes(arr1, 16))
print(find_indexes(arr1, 100))
