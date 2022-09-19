# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:24:32 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""

# Función que convertirá de centímetros a pulgadas según el valor entregado por el usuario


def conversion(unidad):  # Parametro 'unidad' (centimetros)
    return unidad / 2.54


centimetros = float(input("Ingrese los centímetros a convertir a pulgadas: "))
# Entregamos el valor entregado por el usuario a la funcion que convertirá de cm a pulgadas
resultado = conversion(centimetros)

print(f'La conversión de {centimetros} cm a pulgadas es {resultado} pulgadas.')
