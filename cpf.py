def valida_cpf(cpf):
    # Remove caracteres especiais
    cpf = cpf.replace(".", "").replace("-", "")
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    
    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False
    
    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    
    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False
    
    # CPF válido
    return True


# Exemplo de uso
cpf = input("Digite o CPF para validação: ")
if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
