peso = input("Ingrese su peso en Kg: ")
estatura = input("Ingrese su estatura en metros: ")
imc = int(peso) / (float(estatura)**2)
print("Su indice de masa corporal es: ", round(imc,2))