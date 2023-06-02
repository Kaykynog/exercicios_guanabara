distancia = int(input('Qual a distancia da sua viagem: '))
if distancia > 200:
    print(f'Sua passagem custa: R${distancia*0.45}')
else:
    print(f'Sua passagem custa: R${distancia*0.50}')
