'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
media = []
while len(media)<=3:
    nota = (input('Qual sua nota: '))
    nota = int(nota)
    media.append(nota)
print(f'A media da suas notas foi de: {sum(media)/len(media)}')
