def bubble_sort_optim(a):
    N = len(a)
    flag = True
    count = 1
    while flag:
        flag = False
        for i in range(N - count):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        count += 1
    return a
