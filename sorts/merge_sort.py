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
