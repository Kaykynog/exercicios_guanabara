# Verificando se um numero é primo

n = int(input('Digite um numero para verificar se é primo ou nao: '))
total = 0 
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m',c, end='')
        total += 1
    else:
        print('\033[31m', end='')
print(f'\n\033[mO numero {n} foi divisel {total} vezes')
if total == 2:
    print('É numero primo!!')
else:
    print('Não é primo')