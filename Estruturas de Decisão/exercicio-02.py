'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num = float(input('Qual seu numero: '))
if num < 0:
    print('negativo!')
elif num == 0:
    print('Nem positivo, nem negativo!')
else:
    print('positivo')