def recuperar_dados_animais(animais):
    try:
        arq_animais = open("animais.txt", "r")
        for linha in arq_animais:
            if linha.strip():
                campos = linha.strip().split(',')
                id_salvo = campos[0]
                nome = campos[1]
                dta_nas = campos[2]
                tipo = campos[3]
                raca = campos[4]
                id_cli=campos[5]
                status=campos[6]
                animais[id_salvo] = [nome, dta_nas,tipo,raca,id_cli,status]
        arq_animais.close()
    except FileNotFoundError:
        arq_animais=open('animais.txt','w')
        arq_animais.close()
    return animais

def gravar_dados_animais(animais):
    arq_animais=open("animais.txt","w")
    for chaves, dados in animais.items():
        arq_animais.write(chaves+',')
        arq_animais.write(dados[0]+',')
        arq_animais.write(dados[1]+',')
        arq_animais.write(dados[2]+',')
        arq_animais.write(dados[3]+',')                                              
        arq_animais.write(dados[4]+',')
        arq_animais.write(dados[5]+'\n')
    arq_animais.close()


def cadastrar_animais(animais,id):
    arq_animais=open("animais.txt","a")
    arq_animais.write(id+',')
    arq_animais.write(animais[id][0]+',')
    arq_animais.write(animais[id][1]+',')
    arq_animais.write(animais[id][2]+',')
    arq_animais.write(animais[id][3]+',')
    arq_animais.write(animais[id][4]+',')
    arq_animais.write(animais[id][5]+'\n')
    arq_animais.close()


def exibir_animais(id):
    arq_animais= open("animais.txt", "r")
    for linha in arq_animais:
      campos=linha.strip().split(',')
      if campos[0]==id and campos[6]=="ativo":
        nome=campos[1]
        dta_nas=campos[2]
        tipo=campos[3]
        raca=campos[4]
        id_cli=campos[5]
        status=campos[6]
        print(f"Nome:{nome}")
        print(f"Data de nascimento:{dta_nas}")
        print(f"Tipo:{tipo}")
        print(f"Raça:{raca}")
        print(f"Status:{status.capitalize()}")
    arq_animais.close()

def animais_ativos(clientes):
    arq_animais= open("animais.txt", "r")
    for linha in arq_animais:
        campos=linha.strip().split(',')
        if campos[6]=="ativo":
            nome=campos[1]
            dta_nas=campos[2]
            tipo=campos[3]
            raca=campos[4]
            dono=clientes[campos[5]][0]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"Tipo:{tipo}")
            print(f"Raça:{raca}")
            print(f"Dono:{dono}")
    arq_animais.close()



def animais_inativos(clientes):
    arq_animais= open("animais.txt", "r")
    for linha in arq_animais:
        campos=linha.strip().split(',')
        if campos[6]=="inativo":
            nome=campos[1]
            dta_nas=campos[2]
            tipo=campos[3]
            raca=campos[4]
            dono=clientes[campos[5]][0]
            print(f"Nome:{nome}")
            print(f"Data de nascimento:{dta_nas}")
            print(f"Tipo:{tipo}")
            print(f"Raça:{raca}")
            print(f"Dono:{dono}")
    arq_animais.close()


def pesquisar_ani(pes):
    print()
    arq_animais= open("animais.txt", "r")
    for linha in arq_animais:
        campos=linha.strip().split(',')
        nome=campos[1]
        if nome.startswith(pes):
             print(nome)
    arq_animais.close()



def animais_consul(id,animais,clientes,veterinarios):
    arq_consultas= open("consultas.txt", "r")
    for linha in arq_consultas:
      campos=linha.strip().split(',')
      if campos[2]==id:
        cliente=clientes[campos[1]][0]
        veterinario=veterinarios[campos[3]][0]
        data=campos[4]
        status=campos[5]
        print(f"CONSULTAS DO ANIMAL {animais[id][0]}")
        print(f"Cliente:{cliente}")
        print(f"Veterinário:{veterinario}")
        print(f"Data:{data}")
        print(f"Status:{status.capitalize()}")
        print("-"*50)
    arq_consultas.close()