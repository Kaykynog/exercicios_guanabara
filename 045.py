# Calculando desconto de uma compra
# A vista 10% desconto / No cartão 5%
# 2x preço normal
# 3x ou mais - 20% juros

valor = float(input('Qual valor do produto? '))
cartao = valor
juros20 = valor *20 / 100
cartao3x = valor + juros20
a_vista = valor *10 / 100  
a_vista_calculado = valor - a_vista
credito = valor *5 / 100
credito_calculado = valor - credito

forma = int(input('Qual a forma de pagamento?\n1 - A vista\n2 - Credito a vista\n3 - Em 2x\n4 - 3x ou mais '))

if forma == 1:
    print(f'Seu produto fica em R${a_vista_calculado},00')
elif forma == 2: 
    print(f'Seu produto fica em R${credito_calculado},00')
elif forma == 3:
    print(f'Seu produto fica em R${valor},00')
elif forma == 4: 
    print(f'Seu produto fica em R${cartao3x},00')
else: 
    print('Digite uma opção ')

    
    