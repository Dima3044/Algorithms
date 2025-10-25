def binary_search(arr, key, start=0, end=None):
    N = len(arr)
    if N == 1 and arr[0] != key:
        return -1

    if end is None:
        end = N

    index = N // 2

    if arr[index] == key:
        return index + start
    elif key > arr[index]:
        tmp_arr = [arr[i] for i in range(index + 1, end)]
        start += index + 1
    else:
        tmp_arr = [arr[i] for i in range(index)]

    return binary_search(tmp_arr, key, start)
