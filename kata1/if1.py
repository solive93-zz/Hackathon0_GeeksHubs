"""
escribir un programa qye almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla su la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas
"""

password = "contraseña"
password_del_usuario = input("Introduzca la contraseña: ").lower

if password == password_del_usuario:
    print('El password es correcto')
else:
    print('Password incorrecto!')