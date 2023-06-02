salario = float(input('Qual o seu salário?'))
casa = float(input('Qual valor da casa? '))
tempo = int(input('quanto tempo vc vai pagar? '))
salario30 = salario *30 / 100
ano = tempo*12
prestacao = casa / ano

if prestacao > salario30:
    print('Voce nao tem renda pra esta casa')
elif prestacao < salario30:
    print('Voce pode comprar')