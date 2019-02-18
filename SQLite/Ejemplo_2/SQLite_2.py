import sqlite3
import uuid

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

try:
    cursor.execute('''
        CREATE TABLE usuarios(
            id VARCHAR (36) PRIMARY KEY,
            dni VARCHAR(9) UNIQUE ,
            nombre VARCHAR (100),
            edad INTEGER,
            email VARCHAR(100)
        )
    ''')
    conexion.commit()
except sqlite3.OperationalError:
    print("La tabla usuarios ya existe en la base de datos")
except:
    print("Error desconocido")

print(uuid.uuid4())

try:
    usuarios=[
        ('13243685-1663-4839-827f-0606b7f61dac','222222222A','Hector',27,'hector@ejemplo.com'),
        ('23243685-1663-4839-827f-0606b7f61dad','222222222B','Mario',51,'mario@ejemplo.com'),
        ('33243685-1663-4839-827f-0606b7f61dae','222222222C','Mercedes',38,'mercedes@ejemplo.com'),
        ('43243685-1663-4839-827f-0606b7f61daf','222222222D','Juan',19,'juan@ejemplo.com')
    ]
    cursor.executemany("INSERT INTO usuarios VALUES(?,?,?,?,?)",usuarios)
    conexion.commit()
except sqlite3.IntegrityError:
    print("Hay datos duplicados, verifique la información a guardar")

#Productos
try:
    cursor.execute('''
        CREATE TABLE productos(
            id VARCHAR (36) PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL ,
            marca VARCHAR (50) NOT NULL,
            precio FLOAT NOT NULL
        )
    ''')
    conexion.commit()
except sqlite3.OperationalError:
    print("La tabla productos ya existe en la base de datos")
except:
    print("Error desconocido")
else:
    print("Tabla productos creada")



try:
    productos = [
        ('11243685-1663-4839-827f-0606b7f61dac', 'Teclado', 'Logitech', 19.95),
        ('22243685-1663-4839-827f-0606b7f61dac', 'Pantalla 19"', 'Logitech', 20.00),
        ('33243685-1663-4839-827f-0606b7f61dac', 'Mouse', 'Logitech', 17.00),
        ('45243685-1663-4839-827f-0606b7f61dac', 'Impresora', 'Logitech', 18.00),
    ]

    cursor.executemany("INSERT INTO productos VALUES(?,?,?,?)",productos)
    conexion.commit()
except sqlite3.IntegrityError:
    print("Hay datos duplicados, verifique la información a guardar")

cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()

for producto in productos:
    print(producto)

conexion.close()