'''
Faça um Programa que leia três números e mostre o maior deles.
'''
numeros = []
while len(numeros) < 3:
    num = float(input('Fale um numero: '))
    numeros.append(num)
print(f'O maior numero que vc digitou foi: {max(numeros)}')