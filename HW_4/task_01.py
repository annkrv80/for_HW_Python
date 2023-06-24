#Напишите функцию для транспонирования матрицы

def transport_matrix(matrix: list):
    n_rows = len(matrix)
    m_colum = len(matrix[0])
    result =[[ 0 for _ in range(n_rows)] for _ in range(m_colum)]

    for i in range(n_rows):
        for j in range(m_colum):
            result[j][i] = matrix[i][j]
    return result

def trasport_mat(matrix: list):
    return [list(i) for i in zip(*matrix)]

mat = [[10, 20, 30, 40 ], [11, 12, 13, 14], [22, 33, 44, 55]]

print('Исходная матрица')
print(*mat, sep='\n')

mat_t = transport_matrix(mat)
print('Транспорированная матрица')
print(*mat_t, sep='\n')

mat_t_2 = trasport_mat(mat)
print(*mat_t_2, sep='\n')