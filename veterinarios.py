def recuperar_dados_veterinarios(veterinarios):
    try:
        arq_veterinarios = open("veterinarios.txt", "r")
        for linha in arq_veterinarios:
            if linha.strip():     
                campos = linha.strip().split(',')
                id_salvo = campos[0]
                nome = campos[1]
                dta_nas = campos[2]
                cpf = campos[3]
                fone = campos[4]
                crmv=campos[5]
                status=campos[6]
                veterinarios[id_salvo] = [nome, dta_nas, cpf, fone,crmv,status]
        arq_veterinarios.close()
    except FileNotFoundError:
        arq_veterinairos=open('veterinarios.txt','w')
        arq_veterinarios.close()