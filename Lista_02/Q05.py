#Create a function that multiplies two matrix.

def multiply_matrix(mtx1, mtx2):
    rows = len(mtx1)
    columns = len(mtx2[0])
    result = [([0]*columns) for i in range(rows)]
    print(result)
    for i in range(len(mtx1)):
        for j in range(len(mtx2[0])):
            for k in range(len(mtx2)):
                result[i][j] += mtx1[i][k]*mtx2[k][j]
    return result


X = [[3, 5, 8], [7, 1, 0], [6, 7, 9]]
Y = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
result = multiply_matrix(X, Y)
for r in result:
    print(r)