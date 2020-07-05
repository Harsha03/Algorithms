def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x -1)


x = (input("Enter the number"))
m = int(x)
k = factorial(m)

print(k)