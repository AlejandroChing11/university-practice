from random import randint

A = [[randint(1, 10) for n in range(4)] for x in range(4)]
B = [[randint(1, 10) for n in range(4)] for x in range(4)]
C = [[0 for n in range(4)] for x in range(4)]
D = [[0 for n in range(4)] for x in range(4)]
E = [[0 for n in range(4)] for x in range(4)]


for i in range(4):
    for j in range(4):
        a = A[i][j]
        b = B[i][j]
        C[i][j] = a + b
        D[i][j] = a - b
        E[i][j] = a * b

print("> A:", A)
print("> B:", B)
print("> C:", C)
print("> D: ", D)
print("> E: ", E)