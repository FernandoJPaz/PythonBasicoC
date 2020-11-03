#Crear una clase
class MyClass:

  edad = 50

  def ImprimirEdad(edad):
    print(edad)

#Crear objeto
# MyClass c = new MyClass() ---  JAVA
p1 = MyClass()
print(p1.edad)

# public void myMetodo(name , age){
# 
# }

#La función __init __ ()
class Person:
  def __init__(self, name, age):
    self.name = name #Equivalente a this en java
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

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