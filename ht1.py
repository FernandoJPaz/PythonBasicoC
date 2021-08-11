#Ejercicio 1
'''
n = int(input("Introduce la altura del triángulo (entero positivo): "))

for i in range(n): #Delimitar mi rango 
    for j in range(i+1):
        print("*", end="")
    print("")
'''

#Ejercicio

n = int(input("Introduce un número entero positivo mayor que 2: "))

i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")