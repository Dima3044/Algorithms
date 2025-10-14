import matplotlib.pyplot as plt
from random import randint, seed
import time
from sorts.bubble_sort import *
from sorts.bubble_sort_optim import *
from sorts.selection_sort import *
from sorts.insertion_sort import *


def generate_array(N):
    seed(123)
    arr = [randint(1, N * 2) for _ in range(N)]

    return arr


def test_sort(N, func):
    test_arr = generate_array(N)

    start = time.time()
    result = func(test_arr)
    end = time.time()

    time_to_sort_unsorted = round(end - start, 4)

    print('Время на сортировку:', time_to_sort_unsorted)

    start = time.time()
    sort_sorted = func(result)
    end = time.time()

    time_to_sort_sorted = round(end - start, 4)
    print('Время на сортировку отсортированного:', time_to_sort_sorted)
    print('-' * 20)

    return time_to_sort_unsorted


# N = 30000
# print(N, 'элементов')
# print('-' * 20)

# print('\tПузырьковая сортировка')
# test_sort(N, bubble_sort)

# print('\tПузырьковая сортировка с оптимизацией')
# test_sort(N, bubble_sort_optim)

# print('\tСортировка вставками')
# test_sort(N, insertion_sort)

# print('\tСортировка выбором')
# test_sort(N, selection_sort)