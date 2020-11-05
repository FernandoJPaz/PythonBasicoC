#Crear una clase
class MyClass:

  edad = 5
  
  #def imprimirEdad( i )
  def ImprimirEdad(edad):
    print(edad)

#Crear objeto
# MyClass c = new MyClass() ---  JAVA
# Todos los atributos y metodos los va tener (C)

#nombreVariable  
p1 = MyClass()
print(p1.edad)

miObjeto = MyClass()
miObjeto.edad = 1000
print("Mi edad es", miObjeto.edad)

# JAVA
# public void myMetodo(name , age){
# 
# }

#La función __init __ ()
class Person:
  def __init__(self, name, age):
    self.name = name #Equivalente a this en java
    self.age = age

p1 = Person("John", 36)

p2 = Person ("Fernando jose Paz", 24)

print(p1.name)
print(p1.age)

print("----")

print(p2.name)
print(p2.age)

#Métodos de objetos
class Person:
  #1 prioridad
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Fernando", 24)
p1.myfunc()


#El auto parámetro
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Curso de Python", 36)
p1.myfunc()

#Modificar las propiedades del objeto
p1.age = 40

#Eliminar propiedades de objeto
del p1.age

del p1 