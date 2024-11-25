diccionario = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del alumno: ')
        nombre = input('Introduce el nombre del alumno: ')
        direccion = input('Introduce la dirección del alumno: ')
        telefono = input('Introduce el teléfono del alumno: ')
        email = input('Introduce el correo electrónico del alumno: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        diccionario[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del alumno: ')
        if nif in diccionario:
            del diccionario[nif]
        else:
            print('No existe el alumno con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del alumno: ')
        if nif in diccionario:
            print('NIF:', nif)
            for clave, valor in diccionario[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el alumno con el nif', nif)
    if opcion == '4':
        print('Lista de alumno')
        for clave, valor in diccionario.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de alumno preferentes')
        for clave, valor in diccionario.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir alumno\n(2) Eliminar alumno\n(3) Mostrar alumno\n(4) Listar alumno\n(5) Listar alumno preferentes\n(6) Terminar\nElige una opción:')