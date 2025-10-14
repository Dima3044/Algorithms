def selection_sort(a):
    N = len(a)
    for count in range(N):
        min_index = count
        for i in range(count + 1, N):
            if a[min_index] > a[i]:
                min_index = i
        a[count], a[min_index] = a[min_index], a[count]

    return a
