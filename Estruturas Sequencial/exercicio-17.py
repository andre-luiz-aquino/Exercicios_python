'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde
os valores para cima, isto é, considere latas cheias.
'''
import math
area_a_ser_pintada = int(input('Qual é a area á ser pintada: '))
cobertura_da_tinta = area_a_ser_pintada/6
latas = math.ceil((cobertura_da_tinta/18)*1.1)
galao = math.ceil((cobertura_da_tinta/3.6)*1.1)
print('Comprando separado!')
print(f' latas: {latas} custo: {latas*80} \n galao: {galao} custo: {galao*25}')
print('Comprando juntos!')
print(f' latas: {latas/2} custo: {(latas/2)*80} \n galao {galao/2} custo: {(galao/2)*25}')
print(f'Total: {(latas/2)*80+(galao/2)*25}')
