def insertion_sort(a):
    N = len(a)
    for i in range(N - 1):
        j = i + 1
        key = a[j]
        while j >= 1 and key < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
        a[j] = key

    return a
