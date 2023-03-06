mi_matriz = []

f = 6
c = 6
cont = 1

for i in range(f):
  mi_matriz.append([])
  for j in range(c):
    mi_matriz[i].append(cont)
    cont = cont + 1
    
  
for i in mi_matriz:
  print (i)
  
  
print("\n")  
print("\n")  
print("\n")  
  
ma = []
contador = 1

for i in range(6):
  columna = []
  for j in range(6):
    columna.append(contador)
    contador = contador + 1 
  ma.append(columna)
  
  
for i in range(6):
  for j in range(6):
    print(ma[j][i], end=" ")
  print()  
  