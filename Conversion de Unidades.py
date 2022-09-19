# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 09:54:07 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


def conversion(cm):
    pulgadas = cm / 2.54
    return pulgadas


cm = float(input("Ingrese centimetros: "))
pulgadas = conversion(cm)

print(f'La conversion de {cm} centimetros a pulgadas es {pulgadas} pulgadas')
