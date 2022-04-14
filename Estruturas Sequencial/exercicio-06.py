'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''
import math
pi = math.pi
r = input('Qual o raio: ')
r = float(r)
a = (pi*r**2)
print(f'Area é igual: {a:.3f}')
