def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[0:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)

        a = 0
        b = 0
        c = 0


        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                lst[c] = left[a]
                a = a + 1
            else:
                lst[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            lst[c] = left[a]
            a = a + 1
            c = c + 1

        while b < len(right):
            lst[c] = right[b]
            b = b + 1
            c = c + 1
    return lst


bob = [1, 5, 6, 8, 3, 4, 9, 2, 7]
mergesort(bob)
print(bob)
