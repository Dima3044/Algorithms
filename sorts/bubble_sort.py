def bubble_sort(a):
    N = len(a)
    flag = True
    while flag:
        flag = False
        for i in range(N - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
    return a
