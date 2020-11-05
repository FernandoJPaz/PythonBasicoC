#Crear una clase para padres
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("Person", "Clase Persona")
x.printname()

#Crear una clase secundaria
class Student(Person):
  pass #palabra reservada que funciona cuando no deseo agregar mas atributos o metodos

'''

  def AprobarCurso(nota):
    if nota > 60:
      print("Usted Aprobo")
      else:
        print("Usted Reprobo")
        
'''
y = Student("Student", "Clase Estudiante" )
y.printname()

#Agregue la función __init __ ()
'''
class Student(Person):
    def __init__(self, fname, lname):
        #add properties etc.
'''

class Student(Person): 
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

y = Student("Mike", "O")
y.printname()


#Utilice la función super ()
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#Agregar propiedades
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    print(self.firstname, self.lastname,self.graduationyear)

x = Student("Fernando", "Paz", 2021)


#Estudiante = Student("Fernando", "Olsen", "2019")

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
 

x = Student("Fernando", "Paz", "2014")
x.welcome()    