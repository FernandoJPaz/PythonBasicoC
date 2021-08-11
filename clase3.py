'''
if ( condiciones o muchas condicion) {

  // conjunto de codigo en caso de cumpliar las condiciones ;

}
'''


#sintaxis 
#if condicion o muchas condiciones : 
# Conjunto de instrucciones  
 
#Pasos 
#palabra if 
#condicion 
#sentencia de ejecucion, si cumplo la condicion
#sentencia de ejecucion, donde no cumple condicion

#Condiciones de Python y declaraciones If
print("----")
print("Condiciones de Python y declaraciones If")
a = 10
b = 200

if b > a :
  print("b is greater than a")

print("----")


#Sangría
'''
a = 33
b = 200
if b > a:
print("b is greater than a") # ESTA PORCION DE CODIGO VA DA ERROR / SANGRIA
'''

#Elif
#Si las condiciones anterios no son verdaderas , pruebe esta condicion
a = 33 
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#ELSE
a = 200
b = 33

if b > a:
  print("b is greater than a")  
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Short Hand If
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR 
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")


#Nested If
x = 30 

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
    if x > 30 :
      print ("and also above 30")
      if x > 40 : 
        print("and also above 40")
        if x > 50:
          print("and also above 50")
        else :
          print("but not above 50")
      else:
        print("but not above 40")
    else:
      print("but not above 30")    
  else:
    print("but not above 20.")
else:
  print("but not above 10")
