# Exercício Python 092: Crie um programa que leia nome, ano de nascimento 
# e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por
# acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
# de contratação e o salário. Calcule e acrescente, além da idade, com 
# quantos anos a pessoa vai se aposentar.


dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nasc. : '))
dados['idade'] = 2023 - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35 - 2023)
print(dados)