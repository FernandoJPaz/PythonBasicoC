#Python For Loops
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  

#Looping Through a String
for x in "banana":
  print(x)


#The break Statement
fruits = ["apple" , "cherry","banana","apple1", "banana1", "cherry1" ]
for x in fruits:
    print(x)
    if x == "banana": 
        break


print("------ 1")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


#The continue Statement
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
