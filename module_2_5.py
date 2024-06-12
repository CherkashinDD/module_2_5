def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result_1 = get_matrix(2, 2, 5)
result_2 = get_matrix(5, 2, 15)
result_3 = get_matrix(3, 5, 44)

print(*result_1, sep='\n')  
print()
print(*result_2, sep='\n')
print()
print(*result_3, sep='\n')
