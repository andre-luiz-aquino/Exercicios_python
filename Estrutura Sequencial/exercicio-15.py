'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
'''
ganho = float(input('quanto vc ganha por hora?'))
horas = float(input('quantas horas vc trabalhou?'))
salario = (ganho*horas)
i_r = (salario)*0.11
i_s = (salario)*0.08
s_i = (salario)*0.05
print(' + Salário Bruto : R$:', salario,'\n','- IR (11%) : R$:',i_r,'\n','- INSS (8%) : R$:',i_s,'\n', \
'- Sindicato ( 5%) :',s_i,'\n','= Salário Liquido : R$:',(salario-i_r-i_s-s_i))