'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
-Salário Bruto até 900 (inclusive) - isento
-Salário Bruto até 1500 (inclusive) - desconto de 5%
-Salário Bruto até 2500 (inclusive) - desconto de 10%
-Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
print('Valor da hora trabalhada: ')
valor_hora = float(input( ))
print('Quantas horas trabalhadas: ')
horas = float(input( ))
salario = valor_hora*horas
desconto_ir = float()
sindicato = float(0.03)
fgts = float(0.11)
desconto_total = (salario*sindicato)+(salario*fgts)+(salario*desconto_ir)
salario_liquido = (salario-desconto_total)
if salario < 900:
    desconto_ir = 0
elif salario >= 900 and salario<1500:
    desconto_ir = 0.05
elif salario >=1500 and salario<2500:
    desconto_ir = 0.1
elif salario >2500:
    desconto_ir = 0.2
else:
    print('erro')


print(f'+ Salario bruto = {salario}')
print(f'- IR = {salario*desconto_ir}')
print(f'- Sindicato = {salario*sindicato}')
print(f'- FGTS = {salario*fgts}')
print(f'+ Salario Liquido = {salario-desconto_total}')