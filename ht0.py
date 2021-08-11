peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
#imc  = peso / (estatura * estatura)
imc = round(float(peso) / float(estatura)**2,2)
print("Tu índice de masa corporal es " , imc)



