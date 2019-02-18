import sqlite3

#Crear Conexión a base de datos
conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

try:
    cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100),edad INTEGER, email VARCHAR (100))")
except:
    print("Ya existe la table usuarios")


# cursor.execute("SELECT * FROM usuarios LIMIT 1")
# usuario = cursor.fetchone()
# print(usuario)


# cursor.execute("INSERT INTO usuarios VALUES ('Hector',27,'fabri0176@gmail.com')")
# conexion.commit()

usuarios=[
    ('Mario',51,'mario@ejemplo.com'),
    ('Mercedes',38,'mercedes@ejemplo.com'),
    ('Juan',19,'juan@ejemplo.com'),
]

# cursor.executemany("INSERT INTO usuarios VALUES(?,?,?)",usuarios)
# conexion.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()


for usuario in usuarios:
    print(usuario)

conexion.close()