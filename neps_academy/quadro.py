# NAO FINALIZADO

# n_rows = int(input())
n_sequence = 4
rows = []
columns = []
diagonals = []

for r in range(n_sequence):
    rows.append([int(x) for x in input().split(" ")])

for u in range(n_sequence):
    columns.append([rows[i][u] for i in range(n_sequence)])

diagonals.append([rows[i][i] for i in range(n_sequence)])
diagonals.append([rows[i][-i-1] for i in range(n_sequence)])

def sumInline(line):
    theSum = 0
    for term in line:
        theSum += term
    return theSum


# print(rows)
# print(columns)
# print(diagonals)