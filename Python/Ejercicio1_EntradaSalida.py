file = open("Ejercicio1.txt",'w')
file.write('Elemento1\n')
file.close()

file =open("Ejercicio1.txt",'r+')
file.readline()
file.write('Elemento2\n')

file.seek(10)
print(file.read())
file.close()
