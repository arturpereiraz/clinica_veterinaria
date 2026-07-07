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
        arq_veterinarios=open('veterinarios.txt','w')
        arq_veterinarios.close()

def gravar_dados_veterinarios(veterinarios):
    arq_veterinarios=open("veterinarios.txt","w")
    for chaves, dados in veterinarios.items():
        arq_veterinarios.write(chaves+',')
        arq_veterinarios.write(dados[0]+',')
        arq_veterinarios.write(dados[1]+',')
        arq_veterinarios.write(dados[2]+',')
        arq_veterinarios.write(dados[3]+',')
        arq_veterinarios.write(dados[4]+',')
        arq_veterinarios.write(dados[5]+'\n')
    arq_veterinarios.close()
    

def cadastrar_veterinarios(veterinarios,id):
     arq_veterinarios=open("veterinarios.txt","a")
     arq_veterinarios.write(id+',')
     arq_veterinarios.write(veterinarios[id][0]+',')
     arq_veterinarios.write(veterinarios[id][1]+',')
     arq_veterinarios.write(veterinarios[id][2]+',')
     arq_veterinarios.write(veterinarios[id][3]+',')
     arq_veterinarios.write(veterinarios[id][4]+',')
     arq_veterinarios.write(veterinarios[id][5]+'\n')
     arq_veterinarios.close()

def exibir_veterinarios(id):
    arq_veterinarios= open("veterinarios.txt", "r")
    for linha in arq_veterinarios:
        campos=linha.strip().split(',')
        if campos[0]==id and campos[6]=="ativo":
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            crmv=campos[5]
            status=campos[6]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
            print(f"CRMV:{crmv}")
            print(f"Status:{status.capitalize()}")
    arq_veterinarios.close()

def veterinarios_ativos():
    arq_veterinarios= open("veterinarios.txt", "r")
    for linha in arq_veterinarios:
        campos=linha.strip().split(',')
        if campos[6]=="ativo":
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            crmv=campos[5]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
            print(f"CRMV{crmv}")
    arq_veterinarios.close()

def veterinarios_inativos():
    arq_veterinarios= open("veterinarios.txt", "r")
    for linha in arq_veterinarios:
        campos=linha.strip().split(',')
        if campos[6]=="inativo":
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            crmv=campos[5]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
            print(f"CRMV{crmv}")
    arq_veterinarios.close()


def pesquisar_vet(pes):
    print()
    arq_veterinarios= open("veterinarios.txt", "r")
    for linha in arq_veterinarios:
        campos=linha.strip().split(',')
        nome=campos[1]
        if nome.startswith(pes):
             print(nome)
    arq_veterinarios.close()



def veterinarios_consul(id,animais,clientes):
    arq_consultas= open("consultas.txt", "r")
    for linha in arq_consultas:
      campos=linha.strip().split(',')
      if campos[2]==id:
        for dados in campos:
            if dados=="agendada":
                cliente=clientes[campos[1]]
                animal=animais[campos[3]]
                data=campos[4]
                print(f"CONSULTAS AGENDADAS")
                print(f"Cliente:{cliente[0]}")
                print(f"Animal:{animal[0]}")
                print(f"Tipo:{animal[2]}")
                print(f"Data:{data}")
                print("-"*50)
            elif campos[5]=="finalizada":
                cliente=clientes[campos[1]]
                animal=animais[campos[3]]
                data=campos[4]
                print(f"CONSULTAS FINALIZADAS")
                print(f"Cliente:{cliente[0]}")
                print(f"Animal:{animal[0]}")
                print(f"Tipo:{animal[2]}")
                print(f"Data:{data}")
                print("-"*50)
            elif campos[5]=="cancelada":
                cliente=clientes[campos[1]]
                animal=animais[campos[3]]
                data=campos[4]
                print(f"CONSULTAS CANCELADAS")
                print(f"Cliente:{cliente[0]}")
                print(f"Animal:{animal[0]}")
                print(f"Tipo:{animal[2]}")
                print(f"Data:{data}")
                print("-"*50)
    arq_consultas.close()