from pickle import dump, load

class Vehiculo:
    def __init__(self, color, puertas, placa):
        self.color = color
        self.puertas = puertas
        self.placa = placa

    def __str__(self):
        return f"El vehiculo de placa {self.placa} es de color {self.color} y tiene {self.puertas} puertas"

vehiculo1 = Vehiculo("Verde", 4, "abc123")
print(vehiculo1)

file = open("Vehiculos", 'w+b')

dump(vehiculo1, file)

file.seek(0)
new_vehiculo = load(file)

print(new_vehiculo)
file.close()