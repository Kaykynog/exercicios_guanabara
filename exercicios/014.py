#Pintando parede, para 2 m^2 de parede, precisa de 1litro de tinta

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}X{altura} e sua area é de {area}m^2,')
print(f'Para pingtar essa parede, você precisará de {tinta}l de tinta.')