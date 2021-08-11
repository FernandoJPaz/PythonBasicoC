''' - Java - C# - C++
for (int i=0; i < 10 ; i++){

  //declareaciones o bloques de codigo

}
'''

#Sintaxis
#for objetoiterativo in secuencia : 
#  declaraciones (ifs , fors , while , metodos o funciones) 

#Pasos
# 1. for 
# 2. variable que va manejar las iteraciones 
# 3. secuencia a iterar o recorrer
# 4. el area declaracion, donde vamos a manejar cada elemento de la secuencio   

#Python For Loops
fruits = ["apple", "banana", "cherry", "watermelon", "berry", "peach", "lemon"]

for fruit in fruits:
  print("Hola ", fruit)
  

#Looping Through a String
for x in "banana":
  print(x)


#The break Statement
fruits = ["apple" , "cherry","banana","apple1", "banana1", "cherry1" ]
for x in fruits:
    print(x)
    if x == "banana": 
      break


print("------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#The continue Statement
print("The continue Statement")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#The range() Function
for x in range(6):
  print(x)  


for x in range(2, 6):
  print(x)

print("range con 3 parametros")
for x in range(2, 30, 3):
  print(x)


#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
      print(x, y)

#Contador De forma descendete 
num = 10
for i in range(1,num+1):
  print(num-i)

