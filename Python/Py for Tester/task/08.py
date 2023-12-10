

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
def transpose(matrix):
    spam = []
    for i in range(len(matrix[0])):
        spam.append([])
        for j in range(len(matrix)):
            spam[i].append(matrix[j][i])
    return spam


print(transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
