"""
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años la entrada es gratis, si tiene entre 4 y 18 debe pagar 5€ y si es mayor de 18, 10€.
"""
edad = int(input('Introduce tu edad: '))

if edad < 4:
    print('El precio de a entrada es 0.')
elif edad >= 4 and edad < 18:
    print('El precio de la entrada es 5€.')
else:
    print('El precio de la entrada es 10€')
