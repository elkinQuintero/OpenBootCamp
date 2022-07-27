numInicial = 2
numFinal = 8
lista = []
for i in range(numInicial,numFinal+1):
    if i % 2 != 0:
        lista.append(i)

print("La lista de numeros impares desde ", numInicial, " hasta ",numFinal, "es: ",lista)