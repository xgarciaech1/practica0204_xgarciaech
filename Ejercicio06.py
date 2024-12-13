diccionario = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del alumno: ')
        nombre = input('Introduce el nombre del alumno: ')
        telefono = input('Introduce el teléfono del alumno: ')
        email = input('Introduce el correo electrónico del alumno: ')
        aprobado = input('¿Es un aprobado? (S/N)? ').upper()
        alumno = {'nombre':nombre, 'teléfono':telefono, 'email':email, 'aprobado':aprobado =='S'}
        diccionario[nif] = alumno
        
    if opcion == '2':
        nif = input('Introduce NIF del alumno: ')
        if nif in diccionario:
            del diccionario[nif]
        else:
            print('No existe el alumno con el nif', nif)

    if opcion == '3':
        nif = input('Introduce NIF del alumno: ')
        if nif in diccionario:
            for clave, valor in diccionario[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el alumno con el nif', nif)

    if opcion == '4':
        print('Lista de alumno')
        for clave, valor in diccionario.items():
            print(clave, valor['nombre'])

    if opcion == '5':
        print('Lista de alumnos aprobados')
        if aprobado=='S':
            print(nombre)

    opcion = input('Menú de opciones\n(1) Añadir alumno\n(2) Eliminar alumno\n(3) Mostrar alumno\n(4) Listar alumno\n(5) Listar alumnos aprovados\n(6) Terminar\nElige una opción:')