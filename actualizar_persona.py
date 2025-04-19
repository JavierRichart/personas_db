import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
id_persona = int(input('ID a modificar: '))
nombre = input('Nuevo nombre: ')
apellido = input('Nuevo apellido: ')
edad = int(input('Edad: '))
valores = (nombre, apellido, edad, id_persona)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Entrada editada')
cursor.close()
personas_db.close()