#Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
#correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
#nuevo dato debe imprimirse el contenido del diccionario.
datos = {}
Datos = ['nombre', 'edad', 'sexo', 'correo electronico', 'telefono']
for i in Datos:
    datos[i] = input('dime tu ' + i)
    '''datos['nombre'] = i'''
print(datos)