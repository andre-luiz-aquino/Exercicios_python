'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
numeros = []
while len(numeros) < 3:
    num = float(input('Fale um numero: '))
    numeros.append(num)
print(f'O maior numero que vc digitou foi: {max(numeros)}. \nO menor numero que vc digitou foi: {min(numeros)}.')