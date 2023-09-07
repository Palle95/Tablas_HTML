import cgi
import mysql.connector
# headers
print("content-Type: text/html")
print()
print("<html>")
    
print("<head> <title> FORMULARIO </title> </head>)")

conexion1=mysql.connector.connect(host="localhost",
                                   user="usuario1",
                                  passwd="password",
                                  database="libros") #conexion a la base de datos

cursor1 = conexion1.cursor()

print("<body> ")

print("<h3> Tablas de MYSQL </h3>")

print("<table>")

cursor1.execute("select * from libros")

for base in cursor1:
    print("<tr>")
    print("<td>")
    print(base) 
    print("</td>")
    print("</tr>")

print("</table>")

print("</body>")     
            
print("</html>")

 



# Objeto de cursor. El cursor es utilizado para ejecutar consultas sql en la base de datos y traer resultados 

# el cursor ejecuta la consulta a la base de datos. 
#Esta consulta selecciona todos los registros de la tabla "libros"

# Se inicia un bucle for que recorre los resultados obtenidos de la consulta SQL. 
# En este caso, cursor1 actúa como un iterable que devuelve los registros uno por uno.

# Entonces debemos trabajar dentro del for para crear la interfaz html en la cual la tabla se verá reflejada?....
# Asi no se mostrará en la consola cmd al ejercutar el scritp, si no, debemos 
# crear otro archivo html a parte e impotar lo que tenemos acá...
# La cuestion es como traemos lo que hay acá, hacia el script html... supongo que sera con un import lista.py

conexion1.close()        

