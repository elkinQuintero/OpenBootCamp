import math

def areaTriangulo(altura, base):
    return (altura*base)/2

def areaCirculo(radio):
    return (radio**2)*math.pi

altura=float(input("Ingrese la altura del triangulo: "))
base=float(input("Ingrese la base del triangulo: "))
print(f"El área del triangulo es: {round(areaTriangulo(altura,base),2)}")

radio=float(input("Ingrese el radio del circulo: "))
print(f"El área del circulo es: {round(areaCirculo(radio),2)}")
