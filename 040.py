# Converter para binário octal e hexadecimal 
numero = int(input('Digite um nuemero para ser convertido: '))
base = int(input('1 - Binario\n2 - Octal\n3 - hexa\n'))

if base == 1:
    binario = bin(numero)
    print(binario)
    
elif base == 2:
    octal = oct(numero)
    print(octal)

elif base == 3:
    hexa = hex(numero)
    print(hexa)
