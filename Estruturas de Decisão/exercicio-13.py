'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar
outro valor deve aparecer valor inválido.

'''
list = [ "Domingo","Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

for i in list:
    dia = int(input('Qual dia da semana: '))
    if dia >=1 and dia <=7:
        print(list[dia-1])
    else: print('valor inválido')
    break