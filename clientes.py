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
    
def gravar_dados_clientes(clientes):
    arq_clientes=open("clientes.txt","w")
    for chaves, dados in clientes.items():
        arq_clientes.write(chaves+',')
        arq_clientes.write(dados[0]+',')
        arq_clientes.write(dados[1]+',')
        arq_clientes.write(dados[2]+',')                                               
        arq_clientes.write(dados[3]+',')
        arq_clientes.write(dados[4]+'\n')
    arq_clientes.close()


def cadastrar_clientes(clientes,id):
    arq_clientes=open("clientes.txt","a")
    arq_clientes.write(id+',')
    arq_clientes.write(clientes[id][0]+',')
    arq_clientes.write(clientes[id][1]+',')
    arq_clientes.write(clientes[id][2]+',')
    arq_clientes.write(clientes[id][3]+',')
    arq_clientes.write(clientes[id][4]+'\n')
    arq_clientes.close()


def exibir_clientes(id):
    arq_clientes= open("clientes.txt", "r")
    for linha in arq_clientes:
        campos=linha.strip().split(',')
        if campos[0]==id and campos[5]=="ativo":
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            status=campos[5]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
            print(f"Status:{status.capitalize()}")
    arq_clientes.close()


def clientes_ativos():
    arq_clientes= open("clientes.txt", "r")
    for linha in arq_clientes:
        campos=linha.strip().split(',')
        if campos[5]=="ativo":
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
    arq_clientes.close()

def clientes_inativos():
    arq_clientes= open("clientes.txt", "r")
    for linha in arq_clientes:
        campos=linha.strip().split(',')
        if campos[5]=="inativo":       
            nome=campos[1]
            dta_nas=campos[2]
            cpf=campos[3]
            fone=campos[4]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"CPF:{cpf}")
            print(f"Fone:{fone}")
    arq_clientes.close()

def pesquisar_cli(pes):
    print()
    arq_clientes= open("clientes.txt", "r")
    for linha in arq_clientes:
        campos=linha.strip().split(',')
        nome=campos[1]
        if nome.startswith(pes):
             print(nome)
    arq_clientes.close()


def animais_clie(id,clientes):
    arq_animais= open("animais.txt", "r")
    for linha in arq_animais:
      campos=linha.strip().split(',')
      if campos[5]==id:
        nome=campos[1]
        dta_nas=campos[2]
        tipo=campos[3]
        raca=campos[4]
        status=campos[6]
        print(f"ANIMAIS DO CLIENTE {clientes[id][0]}")
        print(f"Nome:{nome}")
        print(f"Data de nascimento:{dta_nas}")
        print(f"Tipo:{tipo}")
        print(f"Raça:{raca}")
        print(f"Status:{status.capitalize()}")
        print("-"*50)
    arq_animais.close()