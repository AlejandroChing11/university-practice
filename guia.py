#Matrices

#Repaso de Listas en Python
#La lista esta definida o rodeada por corchetes
#Para definir una lista debemos utilizar corchetes EJ [1, 2, 3, 4]
#Dentro de los corchetes sus elementos, cada elemento separado por comas EJ ["a", "b", "c", "d"]
#Las listas son una secuencia ordenada porque sus elementos estan en un indice especifico
#cada elemento tiene su propio lugar en la secuencia
# ["a", "b", "c", "d"]
#  [0]  [1]  [2]  [3]
#Es mutable. Puede ser modificada

#Array o arreglo unidimensional 
letras = ["a", "b", "c", "d"]
print(letras)
print(letras[0])

#Más sobre listas https://docs.python.org/es/3/tutorial/datastructures.html

#Declaración matriz bidimensional
#Matriz 3 x 3

m=[ [1,3,4],[7,10,2],[9,0,5] ]
print(m)

m2=[ [0,0,0],[0,0,0],[0,0,0] ]
print(m2)

#Operaciones con matrices
#Asignación: Consiste en asignar directamente un valor a cualquier elemento de la matriz.

m2[0][0] = 5
print(m2)

#Lectura/escritura: Normalmente se realiza con estructuras de repetición. 
#Pero una instrucción simple de lectura/escritura podría ser:

print(m2)
print(m2[0][0])
m2[1][1] = input("Digita el valor de la matriz")
m2[1][1] = int(input("Digita el valor de la matriz: "))