'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
 aluno e apresentar:
-A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
-A mensagem "Reprovado", se a média for menor do que sete;
-A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
notas = []
while len(notas) < 2:
    sua_nota = float(input('Qual sua nota: '))
    notas.append(sua_nota)
print(f'Sua media é:{sum(notas)/len(notas)}')


