#While
# While -> Mientras 
# Condicion Finita
# Instrucciones

#The while Loop
print("Primer Ejemplo")
i = 1
while i < 10:
  print(i)
  i += 1
print("Fin Primer Ejemplo")

#The break Statement
print("Segundo Ejemplo")
i = 1
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1
print("Fin Segundo Ejemplo")
#The continue Statement
print("3 Ejemplo")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("Fin 3 Ejemplo")

#The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")