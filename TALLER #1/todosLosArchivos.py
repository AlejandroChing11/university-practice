
#PUNTO 1
matriz = []
f = 6
c = 6
for i in range(f):
    matriz.append([])
    cont = 1
    menos = 6
    for j in range(c):
        if (i % 2 == 0):
            matriz[i].append(cont)
            cont = cont + 1
        if (i % 2 != 0):
            matriz[i].append(menos)
            menos = menos - 1
print(matriz)








#PUNTO 2
import random
numeros = random.sample(range(1, 101), 100)  
matriz = [[numeros.pop() for j in range(10)] for i in range(10)] 
for fila in matriz:
    print(fila)
    
   
   
   
   
    
    
    
#PUNTO 3.
import random
 
# Inicializamos las variables contadoras
total_hombres = 0
total_mujeres = 0
total_hombres_trabajan = 0
total_mujeres_trabajan = 0
sueldo_hombres_trabajan = 0
sueldo_mujeres_trabajan = 0
 
# Realizamos la encuesta a 10 personas
for i in range(10):
   # Generamos aleatoriamente el sexo (1=masculino, 2=femenino)
   sexo = random.randint(1, 2)
   if sexo == 1:
       total_hombres += 1
   elif sexo == 2:
       total_mujeres += 1
 
   # Generamos aleatoriamente si trabaja (1=si trabaja, 2=no trabaja)
   trabaja = random.randint(1, 2)
   if trabaja == 1:
       sueldo = random.randint(600, 2000)
       if sexo == 1:
           total_hombres_trabajan += 1
           sueldo_hombres_trabajan += sueldo
       elif sexo == 2:
           total_mujeres_trabajan += 1
           sueldo_mujeres_trabajan += sueldo
 
# Calculamos las estadísticas solicitadas
porcentaje_hombres = (total_hombres / 10) * 100
porcentaje_mujeres = (total_mujeres / 10) * 100
porcentaje_hombres_trabajan = (total_hombres_trabajan / total_hombres) * 100
porcentaje_mujeres_trabajan = (total_mujeres_trabajan / total_mujeres) * 100
sueldo_promedio_hombres_trabajan = sueldo_hombres_trabajan / total_hombres_trabajan
sueldo_promedio_mujeres_trabajan = sueldo_mujeres_trabajan / total_mujeres_trabajan
 
# Imprimimos las estadísticas
print("Porcentaje de hombres:", porcentaje_hombres, "%")
print("Porcentaje de mujeres:", porcentaje_mujeres, "%")
print("Porcentaje de hombres que trabajan:", porcentaje_hombres_trabajan, "%")
print("Porcentaje de mujeres que trabajan:", porcentaje_mujeres_trabajan, "%")
print("Sueldo promedio de los hombres que trabajan:", sueldo_promedio_hombres_trabajan)
print("Sueldo promedio de las mujeres que trabajan:", sueldo_promedio_mujeres_trabajan)