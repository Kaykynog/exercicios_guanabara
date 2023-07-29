# Exercício Python 090: Faça um programa que leia nome e média de um 
# aluno, guardando também a situação em um dicionário. No final, mostre 
# o conteúdo da estrutura na tela.

nome = dict()
nome['Nome'] = str(input('Nome: '))
nome['Media'] = float(input('Digite a media: '))

if nome['Media'] >= 7:
    nome['Situação'] = 'Aprovado'
elif nome['Media'] < 7 and nome['Media'] >= 5:
    nome['Situação'] = 'Recuperação'
else:
    nome['Situação'] = 'Reprovado'


for k, v in nome.items():
    print(f'{k} {v}')


