import  os

resp = ''

clientes={
    1:["artur","01/04/20006","70168641461","999999",]}

animais={
    1:["Pingo","23/04/2021","Cachorro","Vira-lata",1]
    }

veterinarios={
    1:["Maria","13/01/2002","9489438","999999","1234"]
    }

consultas={
    1:[1,1,1,"04/06/2026","Marcada"]
    }


while resp != '0':
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
            id=(len(clientes)+1)
            clientes[id]=[nome,dta_nas,cpf,fone]

            print(clientes)
        
        elif opcao=="2":
            os.system("clear")  

            print("#############################")
            print("#### Exibir dados Cliente #####")
            print("#############################")
            print()

            id=int(input("Informe o ID do cliente:"))
            if id in clientes:
                print(f"Nome:{clientes[id][0]}")
                print(f"Data nascimento:{clientes[id][1]}")
                print(f"Cpf:{clientes[id][2]}")
                print(f"Fone:{clientes[id][3]}")
        
        elif opcao=="3":
            os.system("clear")  

            print("#############################")
            print("#### Alterar dados Cliente #####")
            print("#############################")
            print()

            id=int(input("Digite o id do cliente:"))

            if id in clientes:
                nv_nome=input("Nome:")
                nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                nv_cpf=input("CPF:")
                nv_fone=input("Telefone:")
                clientes[id]=[nv_nome, nv_dta_nas,nv_cpf,nv_fone]
        
        elif opcao=="4":
            os.system("clear")  


            print("#############################")
            print("#### Excluir Cliente #####")
            print("#############################")
            print()

            id=int(input("Digite o id do cliente:"))
        
            del clientes[id]
        

    elif resp == '2':
        
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
            id=(len(animais)+1)
            id_clie=input("Digite o id do cliente:")
            
            animais[id]=[nome,dta_nas,tipo,raca,id_clie]

        elif opcao=="2":
            os.system("clear")  

            print("#############################")
            print("#### Exibir dados Animal#####")
            print("#############################")
            print()

            id=int(input("Informe o ID do animal:"))
            if id in animais:
                print(f"Nome:{animais[id][0]}")
                print(f"Data nascimento:{animais[id][1]}")
                print(f"Tipo:{animais[id][2]}")
                print(f"Raça:{animais[id][3]}")
                print(f"Dono(a):{clientes[animais[id][4]][0]}")

        elif opcao=="3":
            os.system("clear")  

            print("#############################")
            print("#### Alterar dados Animal #####")
            print("#############################")
            print()

            id=int(input("Digite o id do animal:"))

            if id in animais:
                nv_nome=input("Nome:")
                nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                nv_tipo=input("Tipo:")
                nv_raca=input("Raça:")
                nv_dono=input("Dono(a):")
                animais[id]=[nv_nome, nv_dta_nas, nv_tipo,nv_raca,nv_dono]
        
        elif opcao=="4":
            os.system("clear")  


            print("#############################")
            print("#### Excluir Animal #####")
            print("#############################")
            print()

            id=int(input("Digite o id do cliente:"))
        
            del animais[id]
        

    elif resp == '3':
        
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
            id=(len(veterinarios)+1)

            veterinarios[id]=[nome,dta_nas,cpf,fone,crmv]
        
        elif opcao=="2":
            
            os.system("clear")  

            print("#############################")
            print("#### Exibir dados Veterinário #####")
            print("#############################")
            print()

            id=int(input("Informe o ID do veterinário:"))
            if id in veterinarios:
                print(f"Nome:{veterinarios[id][0]}")
                print(f"Data nascimento:{veterinarios[id][1]}")
                print(f"Cpf:{veterinarios[id][2]}")
                print(f"Fone:{veterinarios[id][3]}")
                print(f"CRMV:{veterinarios[id][4]}")

        elif opcao=="3":
            os.system("clear")  

            print("#############################")
            print("#### Alterar dados Veterinário #####")
            print("#############################")
            print()

            id=int(input("Digite o id do veterinário:"))

            if id in veterinarios:
                nv_nome=input("Nome:")
                nv_dta_nas=input("Data de nascimento(xx/xx/xxx):")
                nv_cpf=input("CPF:")
                nv_fone=input("Telefone:")
                nv_crmv=input("CRMV:")
                veterinarios[id]=[nv_nome, nv_dta_nas,nv_cpf,nv_fone, nv_crmv]
        
        elif opcao=="4":
            os.system("clear")  


            print("#############################")
            print("#### Excluir Veterinário #####")
            print("#############################")
            print()

            id=int(input("Digite o id do veterinário:"))
        
            del veterinarios[id]
    
        

    elif resp == '4':
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
            id=(len(consultas)+1)
            dta_consul=input("Data:")
            status=input("Status:")
            
            consultas[id]=[id_clie, id_ani,id_vet,dta_consul,status]

        elif opcao=="2":
            os.system("clear")  

            print("#############################")
            print("#### Exibir dados Consulta#####")
            print("#############################")
            print()

            id=int(input("Informe o ID da consulta:"))
            if id in consultas:
                print(f"Cliente:{clientes[consultas[id][0]][0]}")
                print(f"Animal:{animais[consultas[id][1]][0]}")
                print(f"Veterinário:{veterinarios[consultas[id][2]][0]}")
                print(f"Data:{consultas[id][3]}")
                print(f"Status:{consultas[id][4]}")

        elif opcao=="3":
            
            os.system("clear")  

            print("#############################")
            print("#### Alterar consulta #####")
            print("#############################")
            print()

            id=int(input("Digite o id da consulta:"))

            if id in consultas:
                nv_nid_clie=int(input("ID cliente:"))
                nv_id_ani=int(input("ID animal:"))
                nv_id_vet=int(input("ID veterinário:"))
                nv_dta_consul=input("Data:")
                nv_status=input("Status:")
                consultas[id]=[nv_nid_clie,nv_id_ani,nv_id_vet,nv_dta_consul,nv_status]
        
        elif opcao=="4":
            os.system("clear")  


            print("#############################")
            print("#### Excluir Consulta #####")
            print("#############################")
            print()

            id=int(input("Digite o id da consulta:"))
        
            del consultas[id]        

    elif resp=="5":
        
        os.system("clear")
        
        print("#############################")
        print("#### MÓDULO-INFORMAÇÕES #####")
        print("#############################")
        print("###  Projeto de Gestão de Clínica Veterinária   ###")
        print("###  Equipe de desenvolvimento:                 ###")
        print("###  * Artur Pereira @artur_pereiraz            ###")
        print("###  UFRN - Bacharel em Sistemas de Informações ###")
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
    

