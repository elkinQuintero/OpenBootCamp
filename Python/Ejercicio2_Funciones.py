
def numeroprimo():
  numero = int(input('Introduce un número entero: '))

  if numero > 1:
    for i in range(2,int(numero)):
        if (int(numero) % i) == 0:
            return str("El numero "+str(numero)+ " no es primo")

    return str("El numero "+str(numero)+ " es primo")
  else:
    return str("El numero "+str(numero)+ " debe ser mayor a 1")

print(numeroprimo())

