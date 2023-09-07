import mysql.connector

conexion1=mysql.connector(host="localhost", user="usuario1",passwd="password")
cursor1=conexion1.cursor()
cursor1.execute("select * from libros")
for fila in cursor1:
    print(fila)
conexion1.close()        




#------------
# print("<table>")
# 
# 
# for fila in cursor1:
#   <tr>  
#           <td>        
#       print(fila)
#             </td>
#   </tr>  
#
#print("</table>")
#