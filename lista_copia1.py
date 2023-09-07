import mysql.connector


conexion1=mysql.connector.connect(host="localhost",
                                   user="usuario1",
                                  passwd="password",
                                  database="libros") #conexion a la base de datos

cursor1 = conexion1.cursor() 
#Objeto de cursor. El cursor es utilizado para ejecutar consultas sql en la base de datos y traer resultados 


cursor1.execute("select * from libros") #el cursor ejecuta la consulta a la base de datos. 
#Esta consulta selecciona todos los registros de la tabla "libros"

for base in cursor1:
    print(base) 
# Se inicia un bucle for que recorre los resultados obtenidos de la consulta SQL. 
# En este caso, cursor1 actúa como un iterable que devuelve los registros uno por uno.





# Entonces debemos trabajar dentro del for para crear la interfaz html en la cual la tabla se verá reflejada?....
# Asi no se mostrará en la consola cmd al ejercutar el scritp, si no, debemos 
# crear otro archivo html a parte e impotar lo que tenemos acá...
# La cuestion es como traemos lo que hay acá, hacia el script html... supongo que sera con un import lista.py

conexion1.close()        

