import sqlite3

conn = sqlite3.connect('Ejercicio1.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

cursor.execute("INSERT INTO Alumnos VALUES(1,'Juan','Quintero')")
cursor.execute("INSERT INTO Alumnos VALUES(2,'Mariana','Giraldo')")
cursor.execute("INSERT INTO Alumnos VALUES(3,'Elkin','Valencia')")
cursor.execute("INSERT INTO Alumnos VALUES(4,'Santiago','Zapata')")
cursor.execute("INSERT INTO Alumnos VALUES(5,'Paco','Ramirez')")
cursor.execute("INSERT INTO Alumnos VALUES(6,'Jeffer','Ortega')")
cursor.execute("INSERT INTO Alumnos VALUES(7,'Pepe','Lopez')")
cursor.execute("INSERT INTO Alumnos VALUES(8,'Sofia','Estrada')")

conn.commit()

cursor.execute("SELECT * FROM Alumnos WHERE Nombre='Elkin'")
filas = cursor.fetchall()

print(filas)
cursor.close()
conn.close()


