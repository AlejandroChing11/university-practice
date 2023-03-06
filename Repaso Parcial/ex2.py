from random import randint

A=[[randint(0, 21) for i in range (3)]for j in range (3)]
x=False
for i in range(3):
    for j in range(3):
        if A[i][j]==12:
            x=True
            print(f"El numero se encuentra en la posición {i}, {j} de la matriz A")

if x==False:
    print("El numero no se encuentra en la matriz")
