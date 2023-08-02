try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Problema encontrado foi com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possível dividir um numero por zero!')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')