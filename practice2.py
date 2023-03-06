#Inicializacion de un array
mi_array = [
    [1, 2, 3],
    [1, 45, 6],
    [0, 0, 0]
]

#Ejemplo de asignacion de un array

mi_array[2][2] = 10
print(mi_array[2][2])
print(mi_array)

#Ejmplo de escritura y lectura con matrices
mi_array[0][0] = int(input("Ingrese el valor de la posisicon 0,0: "))
print(mi_array[0][0])
print(mi_array)


#Ejemplo con instruccion de repeticion
mi_matriz = []
for i in range(3):
    list = [int(input(f"Ingrese los valores de la fila {i}: ")) for j in range(3)]
    mi_matriz.append(list) #Agregar elementos a la matriz

print(mi_matriz)



