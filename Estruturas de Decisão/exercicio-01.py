'''
Faça um Programa que peça dois números e imprima
o maior deles.
'''
num_1 = float(input('Qual seu numero: '))
num_2 = float(input('Qual seu numero: '))
x = ''
if num_1 > num_2:
    x = num_1
else:
    x = num_2
print(f'O maior numero é: {x}')