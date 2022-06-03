'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule
a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.

'''
notas = []
while len(notas) <2:
    x = int(input('Qual sua nota: '))
    notas.append(x)
media = sum(notas)/len(notas)
print(media)
nota_1 , nota_2 = notas
if media >=9 and media <= 10:
    print ('A')
    print('aprovado')
elif media >7.5 and media < 9:
    print('B')
    print('aprovado')
elif media >= 6 and media < 7.5:
    print('C')
    print('aprovado')
elif media >4 and media < 6:
    print('D')
    print('reprovado')
elif media < 4 and media >= 0:
    print('E')
    print('reprovado')
print(nota_1)
print(nota_2)