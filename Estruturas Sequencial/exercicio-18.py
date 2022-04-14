'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
, calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''
pacote = input('Qual o temanho do seu pacote: ')
internet = input('Qual a velocidade da sua internet: ')
pacote = int(pacote)
internet = int(internet)
dowload = (pacote/(internet/10))
tempo = dowload/60
print(f'O tempo de dowload é de {tempo:.2f} minutos!')
