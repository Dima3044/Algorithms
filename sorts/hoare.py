def hoare_partition(a, left, right):
    pivot = a[left]
    i = left - 1
    j = right + 1

    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        
        j -= 1
        while a[j] > pivot:
            j -= 1
        
        if i >= j:
            return j
        
        a[i], a[j] = a[j], a[i]

def quick_sort_hoare(a, left=0, right=None):
    if right is None:
        right = len(a) - 1
    if left < right:
        pivot_index = hoare_partition(a, left, right)
        quick_sort_hoare(a, left, pivot_index)
        quick_sort_hoare(a, pivot_index + 1, right)
