import  os

resp = ''

clientes={}
 
animais={}

veterinarios={}

consultas={}

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
            clientes[id_salvo] = [nome, dta_nas, cpf, fone]
    arq_clientes.close()
except FileNotFoundError:
    pass

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
            animais[id_salvo] = [nome, dta_nas,tipo,raca,id_cli]
    arq_animais.close()
except FileNotFoundError:
    pass


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
            veterinarios[id_salvo] = [nome, dta_nas, cpf, fone,crmv]
    arq_veterinarios.close()
except FileNotFoundError:
    pass

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
    pass


while resp != '0':
    
    os.system("clear")

    print("#############################")
    print("#### PYVET-GERENCIMENTO #####")
    print("#############################")
    print("##  1 - Clientes            #")
    print("##  2 - Animais             #")
    print("##  3 - Veterinários        #")
    print("##  4 - Consultas           #")
    print("##  5 - Informações         #")
    print("##  0- Sair                 #")


    resp = input("Digite uma opção: ")

    if resp == '1':
        opcao=""
        while opcao!="5":

            os.system("clear")  

            print("#############################")
            print("#### MÓDULO- CLIENTES #####")
            print("#############################")
            print("##  1 - Cadastrar Cliente        #")
            print("##  2 - Exibir dados de Cliente  #")
            print("##  3 - Alterar dados de Cliente #")
            print("##  4 - Excluir Cliente          #")
            print("##  5 - Menu Principal           #")
            opcao = input("Digite uma opção: ")

            if opcao=='1':

                os.system("clear")  

                print("#############################")
                print("#### Cadastrar Cliente #####")
                print("#############################")
                print()


                nome=input("Nome:")
                dta_nas=input("Data de nascimento(xx/xx/xxx):")
                cpf=input("CPF:")
                fone=input("Telefone:")
                id=str((len(clientes)+1))
                clientes[id]=[nome,dta_nas,cpf,fone]

                arq_clientes=open("clientes.txt","a")
                arq_clientes.write(id+',')
                arq_clientes.write(clientes[id][0]+',')
                arq_clientes.write(clientes[id][1]+',')
                arq_clientes.write(clientes[id][2]+',')
                arq_clientes.write(clientes[id][3]+'\n')
                arq_clientes.close()

                print(f"Cliente cadastrado com sucesso!")
        
                for chave in clientes:
                    if chave==id:
                        print(f"O id do cliente é {chave}")
                        
                input("Pressiona ENTER para continuar....")

            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Cliente #####")
                print("#############################")
                print()

                id=(input("Informe o ID do cliente:"))
                
                arq_clientes= open("clientes.txt", "r")
                for linha in arq_clientes:
                    campos=linha.strip().split(',')
                    if campos[0]==id:
                        nome=campos[1]
                        dta_nas=campos[2]
                        cpf=campos[3]
                        fone=campos[4]
                        print(f"Nome:{nome}")
                        print(f"Data de nascimento:{dta_nas}")
                        print(f"CPF:{cpf}")
                        print(f"Fone:{fone}")
                arq_clientes.close()

                input("Pressione ENTER para continuar...")

    
            elif opcao=="3":
                os.system("clear")  

                print("#############################")
                print("#### Alterar dados Cliente #####")
                print("#############################")
                print()

                id=input("Digite o id do cliente:")
                
                if id in clientes:
                    nv_nome=input("Nome:")
                    nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                    nv_cpf=input("CPF:")
                    nv_fone=input("Telefone:")
                    clientes[id]=[nv_nome,nv_dta_nas,nv_cpf,nv_fone]
                                      
                    arq_clientes=open("clientes.txt","w")
                    for chaves, dados in clientes.items():
                        arq_clientes.write(chaves+',')
                        arq_clientes.write(dados[0]+',')
                        arq_clientes.write(dados[1]+',')
                        arq_clientes.write(dados[2]+',')
                        arq_clientes.write(dados[3]+'\n')
                    arq_clientes.close()

                    print("Dados alterados com sucesso")
                    input("Pressione ENTER para continuar...")
                    

            elif opcao=="4":
                os.system("clear")  


                print("#############################")
                print("#### Excluir Cliente #####")
                print("#############################")
                print()

                id=input("Digite o id do cliente:")
    
                del clientes[id]

                arq_clientes=open('clientes.txt','w')
                for chaves, dados in clientes.items():
                    arq_clientes.write(chaves+',')
                    arq_clientes.write(dados[0]+',')
                    arq_clientes.write(dados[1]+',')
                    arq_clientes.write(dados[2]+',')
                    arq_clientes.write(dados[3]+'\n')
                arq_clientes.close()

                print("Cliente excluído com sucesso")
                input("Pressione ENTER para continuar...")

        

    elif resp == '2':
        os.system("clear")
        opcao=""
        while opcao!="5":

            os.system("clear")

            print("#############################")
            print("#### MÓDULO- ANIMAIS #####")
            print("#############################")
            print("##  1 - Cadastrar Animal         #")
            print("##  2 - Exibir dados de Animal   #")
            print("##  3 - Alterar dados de Animal  #")
            print("##  4 - Excluir Animal           #")
            print("##  5 - Menu Principal           #")

            opcao = input("Digite uma opção: ")

            if opcao=="1":
            
                os.system("clear")  
            
                print("#############################")
                print("#### Cadastrar Animal #####")
                print("#############################")
                print()
                nome=input("Nome:")
                dta_nas=input("Data de nascimento(xx/xx/xxx):")
                tipo=input("Tipo:")
                raca=input("Raça:")
                id=str((len(animais)+1))
                id_clie=input("Digite o id do cliente:")
            
                animais[id]=[nome,dta_nas,tipo,raca,id_clie]

                arq_animais=open("animais.txt","a")
                arq_animais.write(id+',')
                arq_animais.write(animais[id][0]+',')
                arq_animais.write(animais[id][1]+',')
                arq_animais.write(animais[id][2]+',')
                arq_animais.write(animais[id][3]+',')
                arq_animais.write(animais[id][4]+'\n')
                arq_animais.close()

                print(f"Animal cadastrado com sucesso!")
            
                for chave in animais:
                    if chave==id:
                        print(f"O id do animal é {chave}")
                
                input("Pressione ENTER para continuar...")


            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Animal#####")
                print("#############################")
                print()

                id=input("Informe o ID do animal:")
                arq_animais= open("animais.txt", "r")
                for linha in arq_animais:
                    campos=linha.strip().split(',')
                    if campos[0]==id:
                        nome=campos[1]
                        dta_nas=campos[2]
                        tipo=campos[3]
                        raca=campos[4]
                        print(f"Nome:{nome}")
                        print(f"Data de nascimento:{dta_nas}")
                        print(f"Tipo:{tipo}")
                        print(f"Raça:{raca}")
                arq_animais.close()

                
                input("Pressione ENTER para continuar...")

            elif opcao=="3":
                os.system("clear")  

                print("#############################")
                print("#### Alterar dados Animal #####")
                print("#############################")
                print()

                id=input("Digite o id do animal:")

                if id in animais:
                    nv_nome=input("Nome:")
                    nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                    nv_tipo=input("Tipo:")
                    nv_raca=input("Raça:")
                    nv_dono=input("Dono(a):")
                    animais[id]=[nv_nome, nv_dta_nas, nv_tipo,nv_raca,nv_dono]

                    arq_animais=open("animais.txt","w")
                    for chaves, dados in animais.items():
                        arq_animais.write(chaves+',')
                        arq_animais.write(dados[0]+',')
                        arq_animais.write(dados[1]+',')
                        arq_animais.write(dados[2]+',')
                        arq_animais.write(dados[3]+'\n')
                    arq_animais.close()

                    print("Dados alterados com sucesso")
                    input("Pressione ENTER para continuar...")

            elif opcao=="4":
        
                os.system("clear")  

                print("#############################")
                print("#### Excluir Animal #####")
                print("#############################")
                print()

                id=input("Digite o id do animal:")
        
                del animais[id]

                arq_animais=open('animais.txt','w')
                for chaves, dados in animais.items():
                    arq_animais.write(chaves+',')
                    arq_animais.write(dados[0]+',')
                    arq_animais.write(dados[1]+',')
                    arq_animais.write(dados[2]+',')
                    arq_animais.write(dados[3]+',')
                    arq_animais.write(dados[4]+'\n')
                arq_animais.close()

                print("Animal excluído com sucesso")
                input("Pressione ENTER para continuar...")

        

    elif resp == '3':
        os.system("clear")
        opcao=""
        while opcao!="5":  
            os.system("clear")
            print("#############################")
            print("#### MÓDULO- VETERINÁRIOS #####")
            print("#############################")
            print("##  1 - Cadastrar Veterinário         #")
            print("##  2 - Exibir dados de Veterinário   #")
            print("##  3 - Alterar dados de Veterinário  #")
            print("##  4 - Excluir Veterinário           #")
            print("##  5 - Menu Principal                #")

            opcao = input("Digite uma opção: ")
        
            if opcao=='1':
            
                os.system("clear")  

                print("#############################")
                print("#### Cadastrar Veterinário #####")
                print("#############################")
                print()
                nome=input("Nome:")
                dta_nas=input("Data de nascimento(xx/xx/xxx):")
                cpf=input("CPF:")
                fone=input("Telefone:")
                crmv=input("Digite seu CRMV:")
                id=str((len(veterinarios)+1))

                veterinarios[id]=[nome,dta_nas,cpf,fone,crmv]

                arq_veterinarios=open("veterinarios.txt","w")
                arq_veterinarios.write(id+',')
                arq_veterinarios.write(veterinarios[id][0]+',')
                arq_veterinarios.write(veterinarios[id][1]+',')
                arq_veterinarios.write(veterinarios[id][2]+',')
                arq_veterinarios.write(veterinarios[id][3]+',')
                arq_veterinarios.write(veterinarios[id][4]+'\n')
                arq_veterinarios.close()

                print(f"Veterinário cadastrado com sucesso!")
            
                for chave in veterinarios:
                    if chave==id:
                        print(f"O id do veterinário é {chave}")
                
                input("Pressione ENTER para continuar...")


        
            elif opcao=="2":
            
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Veterinário #####")
                print("#############################")
                print()

                id=(input("Informe o ID do veterinário:"))

                arq_veterinarios= open("veterinarios.txt", "r")
                for linha in arq_veterinarios:
                    campos=linha.strip().split(',')
                    if campos[0]==id:
                        nome=campos[1]
                        dta_nas=campos[2]
                        cpf=campos[3]
                        fone=campos[4]
                        crmv=campos[5]
                        print(f"Nome:{nome}")
                        print(f"Data de nascimento:{dta_nas}")
                        print(f"CPF:{cpf}")
                        print(f"Fone:{fone}")
                        print(f"CRMV:{crmv}")
                arq_veterinarios.close()
                input("Pressione ENTER para continuar...")


            elif opcao=="3":
                os.system("clear")  

                print("#############################")
                print("#### Alterar dados Veterinário #####")
                print("#############################")
                print()

                id=input("Digite o id do veterinário:")

                if id in veterinarios:
                    nv_nome=input("Nome:")
                    nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                    nv_cpf=input("CPF:")
                    nv_fone=input("Telefone:")
                    nv_crmv=input("CRMV:")
                    veterinarios[id]=[nv_nome, nv_dta_nas,nv_cpf,nv_fone, nv_crmv]

                    arq_veterinarios=open("veterinarios.txt","w")
                    for chaves, dados in veterinarios.items():
                        arq_veterinarios.write(chave+',')
                        arq_veterinarios.write(dados[0]+',')
                        arq_veterinarios.write(dados[1]+',')
                        arq_veterinarios.write(dados[2]+',')
                        arq_veterinarios.write(dados[3]+',')
                        arq_veterinarios.write(dados[4]+'\n')
                    arq_veterinarios.close()

                    print("Dados alterados com sucesso")
                    input("Pressione ENTER para continuar...")

        
            elif opcao=="4":
                os.system("clear")  

                print("#############################")
                print("#### Excluir Veterinário #####")
                print("#############################")
                print()

                id=input("Digite o id do veterinário:")
        
                del veterinarios[id]
                   
                arq_veterinarios=open('veterinarios.txt','w')
                for chaves, dados in veterinarios.items():
                    arq_veterinarios.write(chaves+',')
                    arq_veterinarios.write(dados[0]+',')
                    arq_veterinarios.write(dados[1]+',')
                    arq_veterinarios.write(dados[2]+',')
                    arq_veterinarios.write(dados[3]+',')
                    arq_veterinarios.write(dados[4]+'\n')
                arq_veterinarios.close()


                print("Veterinário excluído com sucesso")
                input("Pressione ENTER para continuar...")

    
    
    elif resp == '4':
        os.system("clear")  
        opcao=""
        while opcao!="5":  
            os.system("clear")

            print("#############################")
            print("#### MÓDULO- CONSULTAS #####")
            print("#############################")
            print("##  1 - Cadastrar Consulta         #")
            print("##  2 - Exibir dados de Consulta   #")
            print("##  3 - Alterar dados de Consulta  #")
            print("##  4 - Excluir Consulta           #")
            print("##  5 - Menu Principal             #")

            opcao = input("Digite uma opção: ")

            if opcao=="1":
                    
                os.system("clear")  

                print("#############################")
                print("#### Cadastrar Consulta #####")
                print("#############################")
                print()
                id_clie=input("ID cliente:")
                id_ani=input("ID animal:")
                id_vet=input("ID veterinário:")
                id=str((len(consultas)+1))
                dta_consul=input("Data:")
                status=input("Status:")
            
                consultas[id]=[id_clie, id_ani,id_vet,dta_consul,status]
                
                arq_consultas=open("consultas.txt","a")
                arq_consultas.write(id+',')
                arq_consultas.write(consultas[id][0]+',')
                arq_consultas.write(consultas[id][1]+',')
                arq_consultas.write(consultas[id][2]+',')
                arq_consultas.write(consultas[id][3]+',')
                arq_consultas.write(consultas[id][4]+'\n')              
                arq_consultas.close()

                print(f"Consulta cadastrada com sucesso!")
            
                for chave in consultas:
                    if chave==id:
                        print(f"O id da consulta é {chave}")
                input("Pressione ENTER para continuar...")


            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Consulta#####")
                print("#############################")
                print()

                id=(input("Informe o ID da consulta:"))
                
                arq_consultas= open("consultas.txt", "r")
                for linha in arq_consultas:
                    campos=linha.strip().split(',')
                    if campos[0]==id:
                        id_cli=campos[1]
                        id_ani=campos[2]
                        id_vet=campos[3]
                        dta_consul=campos[4]
                        status=campos[5]
                        print(f"Id cliente:{id_cli}")
                        print(f"Id animal:{id_ani}")
                        print(f"Id veterinário:{id_vet}")
                        print(f"Data consulta:{dta_consul}")
                        print(f"Status:{status}")
                arq_consultas.close()

                input("Pressione ENTER para continuar...")


            elif opcao=="3":
            
                os.system("clear")  

                print("#############################")
                print("#### Alterar consulta #####")
                print("#############################")
                print()

                id=input("Digite o id da consulta:")

                if id in consultas:
                    nv_nid_clie=input("ID cliente:")
                    nv_id_ani=input("ID animal:")
                    nv_id_vet=input("ID veterinário:")
                    nv_dta_consul=input("Data:")
                    nv_status=input("Status:")
                    consultas[id]=[nv_nid_clie,nv_id_ani,nv_id_vet,nv_dta_consul,nv_status]
                    
                    arq_consultas=open('consultas.txt','w')
                    for chaves, dados in consultas.items():
                        arq_consultas.write(chaves+',')
                        arq_consultas.write(dados[0]+',')
                        arq_consultas.write(dados[1]+',')
                        arq_consultas.write(dados[2]+',')
                        arq_consultas.write(dados[3]+',')
                        arq_consultas.write(dados[4]+'\n')
                    arq_consultas.close()

                    print("Dados alterados com sucesso")
                    input("Pressione ENTER para continuar...")

        
            elif opcao=="4":
                os.system("clear")  


                print("#############################")
                print("#### Excluir Consulta #####")
                print("#############################")
                print()

                id=input("Digite o id da consulta:")
        
                del consultas[id]     
                
                arq_consultas=open('consultas.txt','w')
                for chaves, dados in consultas.items():
                    arq_consultas.write(chaves+',')
                    arq_consultas.write(dados[0]+',')
                    arq_consultas.write(dados[1]+',')
                    arq_consultas.write(dados[2]+',')
                    arq_consultas.write(dados[3]+',')
                    arq_consultas.write(dados[4]+'\n')
                arq_consultas.close()
                
                print("Consulta excluída com sucesso")
                input("Pressione ENTER para continuar...")
      

    elif resp=="5":
        os.system("clear")
        opcao=''
        while opcao !="0":
            os.system("clear")
            print("#############################")
            print("#### MÓDULO-INFORMAÇÕES #####")
            print("#############################")
            print("###  Projeto de Gestão de Clínica Veterinária   ###")
            print("###  Equipe de desenvolvimento:                 ###")
            print("###  * Artur Pereira @artur_pereiraz            ###")
            print("###  UFRN - Bacharel em Sistemas de Informações ###")
            print()

            opcao=input("Digite 0 para voltar a tela inicial:")

            print()
    elif resp == '0':
        os.system("clear")
        
        print("#############################")
        print("#### PROGRAMA ENCERRADO #####")
        print("#############################")
    
    
    else:
        os.system("clear")    
        print("#############################")
        print("#### OPÇÃO INVÁLIDA #####")
        print("#### Digite novamente #####")
        print("#############################")
    

