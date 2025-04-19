import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES (%s, %s, %s)'
nombre = input('Nombre: ')
apellido = input('Apellido: ')
edad = int(input('Edad: '))
valores = (nombre, apellido, edad)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Agregado correctamente {valores}')
cursor.close()
personas_db.close()