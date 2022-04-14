'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
'''
num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite um numero inteiro: '))
real = float(input('Digite um numero real: '))
print(f'a) o produto do dobro do primeiro com metade do segundo: \n R: {(num1*2)+(num2/2)}')
print(f'b) a soma do triplo do primeiro com o terceiro: \n R: {(num1*3)+(real)}')
print(f'c) o terceiro elevado ao cubo: \n R: {real**3}')