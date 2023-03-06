#Inicializacion de un array

mi_array = [
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5],
  [1, 2, 3, 4, 5]
]


#Asignacion de un array o matriz
# print(mi_array[2][3])
# mi_array[2][3] = 100
# print(mi_array[2][3])

#Escritura
# for i in mi_array:
#   print (i)
  

# print(mi_array[0][4])
# mi_array[0][4] = int(input("Ingrese el valor de la posicion 0,4: "))
# print(mi_array[0][4])
# print(mi_array)

#Recorrido secuencial por filas

ma = [
  [1, 2, 5],
  [3, 4, 6],
  [7, 8, 9]
]

#Recorrido secuencial por filas
for i in range(3):
  for j in range (3):
    print(ma[i][j], end="\n")
print()

#Recorrido secuencial por columnas
for i in range(3):
  for j in range (3):
    print(ma[j][i], end="\n")
print()






