import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()
conexion.commit()

cursor.execute("SELECT * FROM usuarios WHERE id = '23243685-1663-4839-827f-0606b7f61dad'")
usuario = cursor.fetchone()
print(usuario)

conexion.commit()
conexion.close()