from random import randint

A = [[randint(0, 11) for i in range(3)] for i in range(3)]

state = False

for i in A:
  print(i)
  
  
ma = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 12]
]

for i in ma:
  print(i)
  
for i in range(3):
  for j in range(3):
    if ma[i][j] == 12:
      print("El numero 12 se encuentra en la posicion: ", i, j)
      state = True
  
if state == False:
  print("El numero 12 no se encuentra en el array")
  
  
     