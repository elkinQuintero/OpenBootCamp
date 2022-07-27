
paises = input("Ingresa una lista de paises separados por comas: ")
paises = paises.split(",")

print(",".join(sorted(set(paises))))
