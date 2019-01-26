usuarios = {'Marta','David','Elvira','Juan','Marcos'}
administradores = {'Juan','Marta'}

administradores.discard('Juan')
administradores.add('Marcos')

for usuario in usuarios:
    if usuario in administradores:
        print('El usuario '+usuario+' es admin')
    else:
        print('El usuario ' + usuario + ' no es admin')
