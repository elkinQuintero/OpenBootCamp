import time

hora = time.strftime('%H')
min = time.strftime('%M')

if int(hora) >= 20:
    print("Es hora de ir a casa")
else:
    print("Quedan {} horas y {} minutos para ir a casa".format(20-int(hora), 59-int(min)))