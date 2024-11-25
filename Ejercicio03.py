#Escribir un programa que guarde en un diccionario los precios de los
#artículos de la tabla, pregunte al usuario por un artículo, un número de
#unidades y muestre por pantalla el precio de esa cantidad de producto. Si el
#producto no está en el diccionario debe mostrar un mensaje informando de ello
cesta = {'Pan':1.4, 'huevos':2.3, 'cebolla':0.85,
          'aceite':4.35}
articulo = input('Dime un articulo: ').capitalize()
cantidad = int(input('Dime la cantidad que quires: '))
if articulo in cesta:
    Cesta = (cesta.get(articulo))
    total = ((Cesta) * (cantidad))
    print(total)
else:
    print('no hay')