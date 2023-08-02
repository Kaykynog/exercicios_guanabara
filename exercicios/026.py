# Peça um numero ao usuario e retorne:
# A unidade, dezena, centena e milhar do numero

numero = input('numero: ')

print(f'unidade: {numero[3:4]}')
print(f'dezena: {numero[2:3]}')
print(f'centena: {numero[1:2]}')
print(f'milhar: {numero[0]}')