from math import ceil


def insert_shift_array(arr, val):
    mid_index = ceil(len(arr) / 2)
    next = val
    for i in range(mid_index, len(arr)):
        temp = arr[i]
        arr[i] = next
        next = temp
    arr.append(next)
    return arr
