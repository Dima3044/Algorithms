import time
from random import randint, seed


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


def selection_sort(a):
    N = len(a)
    for count in range(N):
        min_index = count
        for i in range(count + 1, N):
            if a[min_index] > a[i]:
                min_index = i
        a[count], a[min_index] = a[min_index], a[count]

    return a


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


def merge(l1, l2):
    N1 = len(l1)
    N2 = len(l2)
    N3 = N1 + N2
    l3 = [0] * N3
    c_1 = c_2 = 0

    for i in range(N3):
        if c_2 == N2:
            l3[i] = l1[c_1]
            c_1 += 1
        elif c_1 == N1:
            l3[i] = l2[c_2]
            c_2 += 1

        elif l1[c_1] > l2[c_2]:
            l3[i] = l2[c_2]
            c_2 += 1
        else:
            l3[i] = l1[c_1]
            c_1 += 1
    return l3


def merge_sort(l):
    N = len(l)
    if N == 1:
        return l
    else:
        H = N // 2
        l1 = [0] * H
        l2 = [0] * (N - H)
        for i in range(H):
            l1[i] = l[i]
        for i in range(H, N):
            l2[i - H] = l[i]
        return merge(merge_sort(l1), merge_sort(l2))


seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
test_bubble = bubble_sort(test)
end = time.time()
bubble_time = round(end - start, 4)

seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
test_bubble_optim = bubble_sort_optim(test)
end = time.time()
bubble_optim_time = round(end - start, 4)

seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
test_selection = selection_sort(test)
end = time.time()
selection_time = round(end - start, 4)

seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
test_insertion = insertion_sort(test)
end = time.time()
insertion_time = round(end - start, 4)

seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
test_merge = merge_sort(test)
end = time.time()
merge_time = round(end - start, 4)

seed(42)
test = [randint(1, 50000) for i in range(20000)]
start = time.time()
reference = sorted(test)
end = time.time()
python_time = round(end - start, 4)

print(
    f"Пузырьковая сортировка. Время: {bubble_time}. Результат: {test_bubble == reference}"
)
print(
    f"Пузырьковая сортировка c оптимизацией. Время: {bubble_optim_time}. Результат: {test_bubble_optim == reference}"
)
print(
    f"Сортировка вставками. Время: {insertion_time}. Результат: {test_insertion == reference}"
)
print(
    f"Сортировка выбором. Время: {selection_time}. Результат: {test_selection == reference}"
)
print(
    f"Сортировка слиянием. Время: {merge_time}. Результат: {test_merge == reference}"
)
print(
    f"Встроенная сортировка. Время: {merge_time}"
)
