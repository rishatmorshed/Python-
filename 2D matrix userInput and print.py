matrix = []
col = 3
rows = 3
for i in range(col):
    row = []
    for j in range(rows):
        val = int(input(f"Enter value for position[{i}][{j}]: "))
        row.append(val)
    matrix.append(row)
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()
