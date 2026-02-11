import random

n = int(input("N = "))


matrix = [n]


for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(1, 9))
    matrix.append(row)

print("Matrix: ")
for row in matrix:
    print(row)


border_sum = 0

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            border_sum += matrix[i][j]




