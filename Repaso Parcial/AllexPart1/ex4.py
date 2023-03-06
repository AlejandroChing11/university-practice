f = 10
c = 4
k = "sapo"

A = []

for i in range(f):
  A.append([])
  for j in range(c):
    A[i].append(k)
    
for i in A:
  print(i)