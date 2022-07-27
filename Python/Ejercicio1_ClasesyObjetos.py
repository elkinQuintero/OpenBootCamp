class Vehiculo:
    color = None
    ruedas = None
    puertas = None

class Coche(Vehiculo):
    Velocidad = None
    Cilindraje = None


coche1 = Coche()

coche1.color = "Rojo"
coche1.ruedas = 4
coche1.puertas = 5
coche1.Velocidad = 80
coche1.Cilindraje = 1500

print(f"El coche es de color {coche1.color}, tiene {coche1.puertas} puertas, {coche1.ruedas} ruedas, velocidad de {coche1.Velocidad} y cilindraje {coche1.Cilindraje} ")


# # inicializamos la clase
# class Vehiculo():
#     # inicializamos los atributos
#     def __init__(self, color, ruedas, puertas):
#         self.color = color
#         self.ruedas = ruedas
#         self.puertas = puertas

#     def __str__(self):
#         return "Color {}, {} ruedas".format( self.color, self.ruedas, self.puertas )

# class Coche(Vehiculo):

#     def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
#         self.color = color
#         self.ruedas = ruedas
#         self.puertas = puertas
#         self.velocidad = velocidad
#         self.cilindrada = cilindrada

#     def __str__(self):
#         return "color {}, {} km/h, {} ruedas, {} puertas, {} cc".format( self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

# # bloque principal
# # creamos el nuevo objeto, lo inicializamos y se imprime
# coche = Coche("azul", 4, 4, 150, 1200)
# print(coche)