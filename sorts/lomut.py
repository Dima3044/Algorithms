def lomut_partition(a, left, right):
    pivot = a[right]
    i = left

    for j in range(left, right):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[right] = a[right], a[i]
    return i


def quick_sort_lomut(a, left=0, right=None):
    if right is None:
        right = len(a) - 1
    if left < right:
        pivot_index = lomut_partition(a, left, right)
        quick_sort_lomut(a, left, pivot_index - 1)
        quick_sort_lomut(a, pivot_index + 1, right)
