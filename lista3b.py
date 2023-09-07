import mysql.connector

conexion1=mysql.connector(host="localhost", 
                          user="usuario1", 
                          passwd="password",
                          database="libros")

cursor1=conexion1.cursor()

cursor1.execute("select * from libros")

for tabla in cursor1:
    print(tabla)
conexion1.close()        