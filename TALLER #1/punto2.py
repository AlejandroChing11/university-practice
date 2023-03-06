import random

numeros = random.sample(range(1, 101), 100)  
matriz = [[numeros.pop() for j in range(10)] for i in range(10)] 


for i in matriz:
    print(i)