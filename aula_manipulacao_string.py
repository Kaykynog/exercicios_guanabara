# Analisando textos 
# Cadeia de caracteres '' ou ""
# # Fatiamento 
# len - compreenda
# count - contador
# find - encontrar
# in - existe ? -- OPERADOR
# Métodos :
# replace - trocar/reposicionar 
# upper - transforma em maiúscula
# lower - transforma em minuscula
# capitalize - deixa tudo em minusculo e somente a primeira sera maiuscula 
# title - transforma todas letras iniciais em maiuscula
# strip - remove os espaços inuteis(no inicio e no final)
# rstrip - remove os espaços inuteis(somente na direita)
# lstrip - remove os espaços inuteis(somente na esquerda)
# split - divide a string por palavras (caractere de split - splitador)
# join - junta todos elementos da frase (substitui os espaços por algo especificador '-')

frase = 'curso em video python'
print(len(frase))
print(frase.find('deo')) # encontrou 'deo' começando do 11
print(frase.find('android')) # retornará -1 pois nao encontrou essa palavra na string
print(frase.replace('python', 'Android')) # encontrou 'python' e substituiu por 'android'
print(frase.upper()) # trasnfromou em maiuscula
print(frase.lower()) # trasnfromou em minuscula
print(frase.capitalize()) # inicial maiuscula
print(frase.title()) # todas iniciais maiuscula

