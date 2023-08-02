# Exercício Python 089: Crie um programa que leia nome e duas 
# notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = list()

while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continua = str(input('Quer continuar? S/N')).upper().strip()[0]
    if 'N' in continua:
        break
print('--'*30)
print(f'{"NA":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)
for i, c in enumerate(alunos):
    print(f'{i:<4}{c[0]:<10}{c[2]:>8.1f}')
while True:
    print('-'*35)
    flag = int(input('Quer mostrar as notas de que aluno? (999 interrompe)'))
    if flag == 999:
        print('BYE...')
        break
    if flag <= len(alunos) -1 :
        print(f'Notas de {alunos[flag][0]} são {alunos[flag][1]}')