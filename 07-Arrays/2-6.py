matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(0,len(matrix)):
    matrix[i][i] = 1

for i in range(0,len(matrix)):
    print(*matrix[i])