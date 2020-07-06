def matrixm(a,b):
    ans = [[0, 0],
           [0, 0]]
    for x in range(len(a)):
        for y in range(len(b[0])):
            for z in range(len(b)):
                ans[x][y] = ans[x][y] + a[x][z] * b[z][y]
    return ans

a =[[1, 2],
    [3, 4]]
b = [[5, 6],
     [7, 8]]
c = matrixm(a,b)
for x in range(0, 2):
    for y in range(0, 2):
        print(c[x][y], end=" ")
        print("\n", end="")

