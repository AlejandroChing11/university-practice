from random import randint

B = [[randint(0, 11) for i in range (2)]for j in range (2)]

for i in B:
  print(i)


suma = 0
for fila in B:
  for nums in fila:
    suma += nums 
    
    
print(suma)