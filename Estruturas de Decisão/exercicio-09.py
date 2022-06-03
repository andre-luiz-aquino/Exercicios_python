'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
numeros = []
while len(numeros) < 3:
    num = float(input('Fale um numero: '))
    numeros.append(num)
print(f'A ordem decrescente dos numeros que você digitou: {sorted(numeros, reverse=True)}')