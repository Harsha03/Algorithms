def matrixm(a,b):
    ans = [[0, 0],
           [0, 0]]
    for x in range(0,2):
        for y in range(0,2):
            for z in range(0,2):
                ans[x][y] = ans[x][y] + a[x][z] * b[z][y]

    for x in range(0, 2):
        for y in range(0, 2):

            print(ans[x][y], end=" ")
        print("\n", end="")


a = [[1, 2],
     [3, 4]]
b = [[5, 6],
     [7, 8]]
matrixm(a,b)

