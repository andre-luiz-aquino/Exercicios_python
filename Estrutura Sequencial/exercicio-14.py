'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
 variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e
 ]na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''
peso = float(input('informe o peso dos peixes em kg: '))
excedente = (peso -50)
pesokg = (peso > 50)*4*(peso - 50)
multa = (excedente*4)
print(f'Excesso: {excedente}')
print(f'Multa R$:{multa}')