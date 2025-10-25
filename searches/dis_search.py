def prepare(arr):
    N = len(arr)
    max_val = min_val = arr[0]

    for i in range(1, N):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]

    D = max_val - min_val + 1
    a_inv = [-1] * D

    for i in range(N):
        n = arr[i] - min_val
        a_inv[n] = i

    return max_val, min_val, a_inv


def dis_search(arr, key):
    max_val, min_val, a_inv = prepare(arr)

    result = -1
    if min_val <= key and max_val >= key:
        result = a_inv[key - min_val]
    return result
