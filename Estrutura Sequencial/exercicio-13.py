'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as
seguintes fórmulas:
a)Para homens: (72.7*h) - 58
b)Para mulheres: (62.1*h) - 44.7
'''
sexo = input('sexo(H/M): ')
altura = float(input('Qual sua altura: '))
if sexo == 'M':
    print(f'Seu peso ideal é {(62.1*altura)-44.7}')
elif sexo == 'H':
    print(f'Seu peso ideal é: {(72.7*altura)-58}')
else: print('erro!')