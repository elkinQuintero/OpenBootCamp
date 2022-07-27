def añobiciesto():
    año = int(input("Ingrese el año: "))

    if año % 4 != 0: #no divisible entre 4
        return str("No es bisiesto")
    elif año % 4 == 0 and año % 100 != 0: #divisible entre 4 y no entre 100 o 400
        return str("Es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0: #divisible entre 4 y 10 y no entre 400
        return str("No es bisiesto")
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0: #divisible entre 4, 100 y 400
        return str("Es bisiesto")
    
print(añobiciesto())