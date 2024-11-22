#Escribir un programa que pregunte al usuario su nombre, edad, dirección y
#teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
#mensaje “<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>”.
nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')
direccion = input('Dime tu direccion: ')
telefono = input('Dime tu telefono: ')
datos = {}
datos[nombre] = nombre
datos[edad] = edad
datos[direccion] = direccion
datos[telefono] = telefono
print('tu nombre es', datos[nombre], 'tienes', datos[edad], 'años tu direccion es', datos[direccion], 'y tu telefono es', datos[telefono])