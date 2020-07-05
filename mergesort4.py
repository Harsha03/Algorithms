def chubby(nice):
    if len(nice) > 1:
        w = len(nice) // 2
        left = nice[:w]
        right = nice[w:]
        chubby(left)
        chubby(right)

        a = 0
        b = 0
        c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                nice[c] = left[a]
                a = a + 1
            else:
                nice[c] = right[b]
                b = b + 1
            c = c + 1

        while a < len(left):
            nice[c] = left[a]
            a = a + 1
            c = c + 1
            print(a,c)

        while b < len(right):
            nice[c] = right[b]
            b = b + 1
            c = c + 1
            print(b, c)





nice = [6, 4, 5, 2, 3, 1]
chubby(nice)
print(nice)





