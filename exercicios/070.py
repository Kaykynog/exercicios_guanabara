# Programa que lê nome preço de varios produtos, até o usuario não quiser mais
# mostrar no final qual é o total gasto, quantos custam mais de 1000 e o nome 
# nome do produto mais barato
total = 0
nome = []
menor = 0
contador = 0
totmil = 0
mais_barato = ''

while True:
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Digite o valor do produto: '))
    contador += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if contador == 1:
        menor = valor
        mais_barato = nome
    else:
        if valor < menor:
            menor = valor
            mais_barato = nome
    continua = str(input('Deseja contnuar S/N?' )).upper().strip()[0]
    if continua in 'Ss':
        pass
    if continua in 'Nn':
        break
print(f'Total da compra: {total:.2f}')
print(f'Temos {totmil} produtos custando mais de 1000,00 R$')
print(f'O produto mais barato foi {mais_barato} custando {menor:.2f} R$')
    
