'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
'''
horas = input('Quantas horas voce trabalhou: ')
ganha = input('Quanto voce ganha por hora: ')
horas = float(horas)
ganha = float(ganha)
salario = horas*ganha
print(f'Seu salario do mes é {salario} R$:.')