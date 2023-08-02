velo_max = 80
velo = int(input('Qual sua velocidade? '))

if velo > velo_max:
    multa = velo - velo_max
    print(f'voce está a {multa}kmh acima da velocidade permitida')
    print(f'E será multado em R${multa*7},00')
else:
    print('voce ta dentro da lei')