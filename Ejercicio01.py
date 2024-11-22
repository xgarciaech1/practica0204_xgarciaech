#Escribir un programa que guarde en una variable el diccionario
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
#muestre su símbolo o un mensaje de aviso si la divisa no está en el
#diccionario.
moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input('Dime tu divisa: ').capitalize()
if divisa in moneda:
    print(moneda.get(divisa))
else:
    print('no esta esa moneda.')