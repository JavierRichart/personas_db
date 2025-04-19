import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)

cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
id_persona = int(input('Dime id a eliminar: '))
valor = (id_persona,)
cursor.execute(sentencia_sql, valor)
personas_db.commit()
print('Registro eliminado')
cursor.close()
personas_db.close()
