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

def gravar_dados_consultas(consultas):
  arq_consultas=open('consultas.txt','w')
  for chaves, dados in consultas.items():
    arq_consultas.write(chaves+',')
    arq_consultas.write(dados[0]+',')
    arq_consultas.write(dados[1]+',')
    arq_consultas.write(dados[2]+',')
    arq_consultas.write(dados[3]+',')
    arq_consultas.write(dados[4]+'\n')
  arq_consultas.close()

def cadastrar_consultas(consultas,id):
     arq_consultas=open("consultas.txt","a")
     arq_consultas.write(id+',')
     arq_consultas.write(consultas[id][0]+',')
     arq_consultas.write(consultas[id][1]+',')
     arq_consultas.write(consultas[id][2]+',')
     arq_consultas.write(consultas[id][3]+',')
     arq_consultas.write(consultas[id][4]+'\n')              
     arq_consultas.close()

def exibir_consultas(id,clientes,animais,veterinarios):
    arq_consultas= open("consultas.txt", "r")
    for linha in arq_consultas:
        campos=linha.strip().split(',')
        if campos[0]==id:
            id_cli=campos[1]
            id_ani=campos[2]
            id_vet=campos[3]
            dta_consul=campos[4]
            status=campos[5]
            print(f"Cliente:{clientes[id_cli][0]}")
            print(f"Animal:{animais[id_ani][0]}")
            print(f"Veterinário:{veterinarios[id_vet][0]}")
            print(f"Data consulta:{dta_consul}")
            print(f"Status:{status.capitalize()}")
    arq_consultas.close()