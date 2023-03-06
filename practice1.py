#Inicializacion del array.

mi_array = [
    [1, 3 , 4],
    [3, 4, 6],
    [7, 8, 9]
]


#Ejemplo de asignacion
mi_array[1][1] = 10
print(mi_array)


#ejemplo de escritura y lectura con matrices
mi_array[0][0] = int(input("Ingrese el valor de la posicion 0,0: "))
print(mi_array[0][0])
print(mi_array)



#Ejemplo con instruccion de repeticion.
mi_matriz = []
for i in range(3):
        list = [int(input(f"Ingresa los valores de la fila {i}: ")) for j in range(3)]
        mi_matriz.append(list)
   
print(mi_matriz)
    

