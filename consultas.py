def recuperar_dados_consultas(consultas):
    try:
        arq_consultas = open("consultas.txt", "r")
        for linha in arq_consultas:
            if linha.strip(): 
                campos = linha.strip().split(',')
                id_salvo = campos[0]
                id_cli= campos[1]
                id_ani = campos[2]
                id_vet= campos[3]
                dta_consul= campos[4]
                status=campos[5]
                consultas[id_salvo] = [id_cli, id_ani, id_vet,dta_consul,status]
        arq_consultas.close()
    except FileNotFoundError:
        arq_clientes=open('consultas.txt','w')
        arq_clientes.close()