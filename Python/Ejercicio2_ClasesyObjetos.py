# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que 
# tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus 
# atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    
    def inicializar(self, Nombre, Nota):
        self.Nombre = Nombre
        self.Nota = Nota

    def imprimir(self):
        print("Nombre: ",self.Nombre)
        print("Nota: ",self.Nota)

    def Aprueba(self):
        if (self.Nota>=3):
            print(f"El estudiante {self.Nombre} aprueba con una nota de {self.Nota}")
        else:
            print(f"El estudiante {self.Nombre} reprueba con una nota de {self.Nota}")
    


estudiante = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota: "))

estudiante1 = Alumno()
estudiante1.inicializar(estudiante,nota)
estudiante1.imprimir()
estudiante1.Aprueba()