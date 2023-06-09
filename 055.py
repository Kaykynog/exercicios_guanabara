# Criar uma frase qualquer e dizer se é ou não um palindromo

frase = str('a sacada da casa').lower()
invertida = ''.join(p[:-1] for p in frase.split())
frase.join(' ', '')
print(frase)
print(f'frase ao contrario {invertida}')

# if invertida == frase:
#     print('Palindromo')
# else: 
#     print('Nao é palindromo')
