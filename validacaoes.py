def validar_cpf(cpf):
    cpf_limpo = cpf.replace(".", "").replace("-", "").strip()
    if len(cpf_limpo) != 11 or not cpf_limpo.isdigit():
        return False
    if cpf_limpo == cpf_limpo[0] * 11:
        return False
    soma_1 = 0
    peso_1 = 10
    for i in range(9):
        soma_1 += int(cpf_limpo[i]) * peso_1
        peso_1 -= 1
    resto_1 = soma_1 % 11
    if resto_1 < 2:
        digito_1 = 0
    else:
        digito_1 = 11 - resto_1

    soma_2 = 0
    peso_2 = 11
    for i in range(10):
        if i < 9:
            soma_2 += int(cpf_limpo[i]) * peso_2
        else:
            soma_2 += digito_1 * peso_2
        peso_2 -= 1
    resto_2 = soma_2 % 11
    if resto_2 < 2:
        digito_2 = 0
    else:
        digito_2 = 11 - resto_2
    if int(cpf_limpo[9]) == digito_1 and int(cpf_limpo[10]) == digito_2:
        return True
    else:
        return False
    

def validar_fone(telefone):
    fone_limpo = telefone.replace("").replace("-").replace("-").strip    
    if len(fone_limpo) not in [10, 11]:
        return False
    if fone_limpo[0] == '0':
        return False
    if len(fone_limpo) == 11 and fone_limpo[2] != '9':
        return False
    if fone_limpo == fone_limpo[0] * len(fone_limpo):
        return False
        
    return True