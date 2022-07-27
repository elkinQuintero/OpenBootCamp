from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

def numerosImpares(lis):
    if lis % 2 == 0:
        return False
    return True
def suma(a,b):
    return a+b

resultado = filter(numerosImpares,numeros)
print(reduce(suma, list(resultado)))


# def ej2(lista): 
#     resultado = list(filter((lambda x: x % 2), lista)) 
#     print(resultado)
#     resultado = reduce( (lambda x, y: x + y), resultado) 
#     print(resultado)

# lista = list(range(100))

# ej2(lista)