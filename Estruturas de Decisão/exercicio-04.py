'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input('Qual sua letra: ')
consoante = ['a','e','i','o','u','y']
vogal = ['b','c','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z']
if letra in consoante:
    print('consoante')
elif letra in vogal:
    print('Vogal')
else:
    print('Digito invalido!')