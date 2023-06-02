string = 'ola'
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[1;31m',
}
print(f'{cores[vermelho]}{string}{cores[limpa]}')