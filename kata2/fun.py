
"""
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
"""

def circle_area(radius):
    pi = 3.1415
    return 2 * pi * radius**2

def cilinder_volume(radius, high):
    return circle_area(radius)*high

print(cilinder_volume(3,5))