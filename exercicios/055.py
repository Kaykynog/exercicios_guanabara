# Criar uma frase qualquer e dizer se é ou não um palindromo

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'a frase invertida e sem espaços ficou {inverso}')
if inverso == junto:
    print('É um palíndromo! ')
else: 
    print('A frase não é um palíndromo')