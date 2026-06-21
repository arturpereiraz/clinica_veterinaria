def recuperar_dados_clientes(clientes):
    try:
        arq_clientes = open("clientes.txt", "r")
        for linha in arq_clientes:
            if linha.strip():  # Evita linhas vazias    
                campos = linha.strip().split(',')
                id_salvo = campos[0]
                nome = campos[1]
                dta_nas = campos[2]
                cpf = campos[3]
                fone = campos[4]
                status=campos[5]
                clientes[id_salvo] = [nome, dta_nas, cpf, fone, status]        
        arq_clientes.close()
    except FileNotFoundError:
        arq_clientes=open('clientes.txt','w')
        arq_clientes.close()
    return clientes
    