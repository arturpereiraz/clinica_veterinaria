from clientes import recuperar_dados_clientes, gravar_dados_clientes, cadastrar_clientes,exibir_clientes,clientes_ativos, clientes_inativos, pesquisar_cli, animais_clie

from animais import recuperar_dados_animais,gravar_dados_animais, cadastrar_animais,exibir_animais, animais_ativos, animais_inativos, pesquisar_ani, animais_consul

from veterinarios import recuperar_dados_veterinarios,gravar_dados_veterinarios,cadastrar_veterinarios,exibir_veterinarios, veterinarios_ativos,veterinarios_inativos, pesquisar_vet, veterinarios_consul

from consultas import recuperar_dados_consultas, gravar_dados_consultas,cadastrar_consultas,exibir_consultas

from validacaoes import validar_cpf, validar_fone
import  os

resp = ''

clientes={}
animais={}
veterinarios={}
consultas={}

recuperar_dados_clientes(clientes)
recuperar_dados_animais(animais)
recuperar_dados_veterinarios(veterinarios)
recuperar_dados_consultas(consultas)


while resp != '0':
    
    os.system("clear")

    print("#############################")
    print("#### PYVET-GERENCIMENTO #####")
    print("#############################")
    print("##  1 - Clientes            #")
    print("##  2 - Animais             #")
    print("##  3 - Veterinários        #")
    print("##  4 - Consultas           #")
    print("##  5 - Relatórios          #")
    print("##  6 - Informações         #")
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
                while True:
                    cpf=input("CPF:")
                    if validar_cpf(cpf)== True:
                        break
                    else:
                        print("Digite um cpf válido")
                while True:
                    fone=input("Fone:")
                    if validar_fone(fone)==True:
                        break
                    else:
                        print("Digite um telefone válido")
                status=("ativo")
                id=str((len(clientes)+1))
                clientes[id]=[nome,dta_nas,cpf,fone,status]

                cadastrar_clientes(clientes,id)

                print(f"Cliente cadastrado com sucesso!\nO id do cliente é {id}")
                           
                input("Pressione ENTER para continuar...")


            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Cliente #####")
                print("#############################")
                print()

                id=(input("Informe o ID do cliente:"))

                if id in clientes:
                    exibir_clientes(id)
                else:
                    print("Cliente não encontrado")

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
                    while True:
                        nv_cpf=input("CPF:")
                        if validar_cpf(nv_cpf)== True:
                            break
                        else:
                            print("Digite um cpf válido")
                    while True:
                        nv_fone=input("Fone:")
                        if validar_fone(nv_fone)=="True":
                            break
                        else:
                            print("Digite um telefone válido")
                    nv_status=input("Status(Ativo/Inativo):)")
                    nv_status=nv_status.lower()
                    clientes[id]=[nv_nome,nv_dta_nas,nv_cpf,nv_fone,nv_status]

                    gravar_dados_clientes(clientes)
                    
                    print("Dados alterados com sucesso")

                else:
                    
                    print("Cliente não encontrado")

                input("Pressione ENTER para continuar...")
                    

            elif opcao=="4":
                os.system("clear")  


                print("#############################")
                print("#### Excluir Cliente #####")
                print("#############################")
                print()

                id=input("Digite o id do cliente:")

                if id in clientes:
                    clientes[id][4]="inativo"
                    gravar_dados_clientes(clientes)
                    print("Cliente excluído/desativado com sucesso")
                else:
                    print("Cliente não encontrado")
                
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
                if id_clie not in clientes:
                    print("Cliente não cadastrado")
                    id_clie=input("Digite um id válido")
                status="ativo"
                animais[id]=[nome,dta_nas,tipo,raca,id_clie,status]

                cadastrar_animais(animais,id)

                print(f"Animal cadastrado com sucesso!\nO id do animal é {id}")
                
                input("Pressione ENTER para continuar...")


            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Animal#####")
                print("#############################")
                print()

                id=input("Informe o ID do animal:")

                if id in animais:
                    exibir_animais(id)
                else:
                    print("Animal não encontrado")
                
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
                    nv_dono=input("Digite id do cliente:")
                    if id_clie not in clientes:
                        print("Cliente não cadastrado")
                        nv_dono=input("Digite um id válido")
                    nv_status=input("Status(Ativo/Inativo):")
                    nv_status=nv_status.lower()
                    animais[id]=[nv_nome, nv_dta_nas, nv_tipo,nv_raca,nv_dono, nv_status]
                    
                    gravar_dados_animais(animais)
                    
                    print("Dados alterados com sucesso")

                else:
                    print("Animal não encontrado")
                
                input("Pressione ENTER para continuar...")

            elif opcao=="4":
        
                os.system("clear")  

                print("#############################")
                print("#### Excluir Animal #####")
                print("#############################")
                print()

                id=input("Digite o id do animal:")

                if id in animais:
                    animais[id][5]="inativo"
                    gravar_dados_animais(animais)
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
                while True:
                    cpf=input("CPF:")
                    if validar_cpf(cpf)== True:
                        break
                    else:
                        print("Digite um cpf válido")
                while True:
                    fone=input("Fone:")
                    if validar_fone(fone)=="True":
                        break
                    else:
                        print("Digite um telefone válido")
                crmv=input("Digite seu CRMV:")
                status="ativo"
                id=str((len(veterinarios)+1))
                veterinarios[id]=[nome,dta_nas,cpf,fone,crmv,status]

                cadastrar_veterinarios(veterinarios,id)

                print(f"Veterinário cadastrado com sucesso!\nO id do veterinário é {id}")
                
                input("Pressione ENTER para continuar...")


        
            elif opcao=="2":
            
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Veterinário #####")
                print("#############################")
                print()

                id=(input("Informe o ID do veterinário:"))
                if id in veterinarios:
                    exibir_veterinarios(id)
                else:
                    print("Veterinário não encontrado")
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
                    while True:
                        nv_cpf=input("CPF:")
                        if validar_cpf(nv_cpf)== True:
                            break
                        else:
                            print("Digite um cpf válido")
                    while True:
                        nv_fone=input("Fone:")
                        if validar_fone(nv_fone)=="True":
                            break
                        else:
                            print("Digite um telefone válido")
                    nv_crmv=input("CRMV:")
                    nv_status=input("Status(Ativo/Inativo):")
                    nv_status=nv_status.lower()
                    veterinarios[id]=[nv_nome, nv_dta_nas,nv_cpf,nv_fone, nv_crmv,nv_status]

                    gravar_dados_veterinarios(veterinarios)
                    print("Dados alterados com sucesso")
                else:
                    print("Veterinário não encontrado")
                input("Pressione ENTER para continuar...")

        
            elif opcao=="4":
                os.system("clear")  

                print("#############################")
                print("#### Excluir Veterinário #####")
                print("#############################")
                print()

                id=input("Digite o id do veterinário:")

                if id in veterinarios:
                    veterinarios[id][5]="inativo"            
                    gravar_dados_veterinarios(veterinarios)
                    print("Veterinário excluído com sucesso")

                else:
                    print("Veterinário não encontrado")

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
                if id_clie not in clientes:
                    print("Cliente não cadastrado")
                    id_clie=input("Digite um id válido")
                id_ani=input("ID animal:")
                if id_ani not in animais:
                    print("Animal não cadastrado")
                    id_ani=input("Digite um id válido")
                id_vet=input("ID veterinário:")
                if id_vet not in veterinarios:
                    print("Veterinário não cadastrado")
                    id_vet=input("Digite um id válido")
                id=str((len(consultas)+1))
                dta_consul=input("Data:")
                status="agendada"
            
                consultas[id]=[id_clie, id_ani,id_vet,dta_consul,status]
                
                cadastrar_consultas(consultas,id)

                print(f"Consulta cadastrada com sucesso!\nO id da consulta é {id}")

                input("Pressione ENTER para continuar...")


            elif opcao=="2":
                os.system("clear")  

                print("#############################")
                print("#### Exibir dados Consulta#####")
                print("#############################")
                print()

                id=(input("Informe o ID da consulta:"))      
                
                if id in consultas:
                    exibir_consultas(id,clientes,animais,veterinarios)

                else:
                    print("Consulta não encontrada")

                input("Pressione ENTER para continuar...")


            elif opcao=="3":
            
                os.system("clear")  

                print("#############################")
                print("#### Alterar consulta #####")
                print("#############################")
                print()
                
                print("Digite 1 para alterar todos os dados da consulta")
                print()
                print("Digite 2 para alterar o status da consulta")
                print()
                alter=input("Digite a opção:")

                if alter=='1':    
                    id=input("Digite o id da consulta:")

                    if id in consultas:
                        nv_nid_clie=input("ID cliente:")
                        nv_id_ani=input("ID animal:")
                        nv_id_vet=input("ID veterinário:")
                        nv_dta_consul=input("Data:")
                        nv_status=input("Status:")
                        nv_status=nv_status.lower
                        consultas[id]=[nv_nid_clie,nv_id_ani,nv_id_vet,nv_dta_consul,nv_status]
                    
                        gravar_dados_consultas(consultas)
                        print("Dados alterados com sucesso")
                    else:
                        print("Consulta não encontrada")
                elif alter=='2':
                
                    id=input("Digite o id da consulta:")
                    if id in consultas:
                        nv_status=input("Status:")
                        consultas[id][4]=nv_status.lower()
                        gravar_dados_consultas(consultas)

                    else:
                        print("Consulta não encontrada")

                
                input("Pressione ENTER para continuar...")

        
            elif opcao=="4":
                os.system("clear")  


                print("#############################")
                print("#### Excluir Consulta #####")
                print("#############################")
                print()
    
                id=input("Digite o id da consulta:")
                
                if id in consultas:                
                    consultas[id][4]="inativa"     
                    gravar_dados_consultas(consultas)
                    print("Consulta excluída com sucesso")
                else:
                    print("Consulta não encontrada")

                input("Pressione ENTER para continuar...")

    elif resp == '5':
        os.system("clear")  
        opcao=""
        while opcao!="5":  
            os.system("clear")
            print("#############################")
            print("#### MÓDULO- RELATÓRIOS #####")
            print("#############################")
            print("##  1 - Relatórios Clientes        #")
            print("##  2 - Relatórios Animais         #")
            print("##  3 - Relatórios Veterinários    #")
            print("##  4 - Relatórios Consultas       #")
            print("##  5 - Menu Principal             #")

            opcao = input("Digite uma opção: ")
        
            if opcao=="1":       
                os.system("clear")
                opcao=""
                while opcao!="5":  
                    os.system("clear")
                    print("#############################")
                    print("#### RELATÓRIOS- CLIENTES #####")
                    print("#############################")
                    print("##  1 - Clientes ativos         #")
                    print("##  2 - Clientes inativos       #")
                    print("##  3 - Pesquisar Usuário       #")
                    print("##  4 - Animais                 #")
                    print("##  5 - Menu Principal          #")

                    opcao = input("Digite uma opção: ")

                    if opcao=="1":
                        os.system("clear")  
                        print("#############################")
                        print("#### CLIENTES ATIVOS #####")
                        print("#############################")
                
                        clientes_ativos()
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="2":
                        os.system("clear")  
                        print("#############################")
                        print("#### CLIENTES INATIVOS #####")
                        print("#############################")
                
                        clientes_inativos()
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="3":
                        os.system("clear")  
                        print("#############################")
                        print("#### PESQUISAR CLIENTES #####")
                        print("#############################")
                
                        pes=input("Informe o início do nome: ")
                        
                        pesquisar_cli(pes)
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="4":
                        os.system("clear")
                        print("#############################")
                        print("#### ANIMAIS-CLIENTES #####")
                        print("#############################")

                        id=input("Digite o id do cliente:")

                        animais_clie(id,clientes)

                        input("Pressione ENTER para continuar...")
                
            elif opcao=="2":       
                os.system("clear")
                opcao=""
                while opcao!="5":  
                    os.system("clear")
                    print("#############################")
                    print("#### RELATÓRIOS- ANIMAIS #####")
                    print("#############################")
                    print("##  1 - Animais ativos         #")
                    print("##  2 - Animais inativos       #")
                    print("##  3 - Pesquisar Animal       #")
                    print("##  4 - Consultas               #")
                    print("##  5 - Menu Principal          #")

                    opcao = input("Digite uma opção: ")

                    if opcao=="1":
                        os.system("clear")  
                        print("#############################")
                        print("#### ANIMAIS ATIVOS #####")
                        print("#############################")
                
                        animais_ativos(clientes)
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="2":
                        os.system("clear")  
                        print("#############################")
                        print("#### ANIMAIS INATIVOS #####")
                        print("#############################")
                
                        animais_inativos(clientes)
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="3":
                        os.system("clear")  
                        print("#############################")
                        print("#### PESQUISAR ANIMAIS #####")
                        print("#############################")
                
                        pes=input("Informe o início do nome: ")
                        
                        pesquisar_ani(pes)
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="4":
                        os.system("clear")
                        print("#############################")
                        print("#### CONSULTAS- ANIMAIS #####")
                        print("#############################")

                        id=input("Digite o id do animal:")

                        animais_consul(id,animais,clientes,veterinarios)

                        input("Pressione ENTER para continuar...")
            
            elif opcao=="3":       
                os.system("clear")
                opcao=""
                while opcao!="5":  
                    os.system("clear")
                    print("#############################")
                    print("#### RELATÓRIOS- VETERINŔIOS #####")
                    print("#############################")
                    print("##  1 - Veternários ativos      #")
                    print("##  2 - Veterinários inativos   #")
                    print("##  3 - Pesquisar Veterinário   #")
                    print("##  4 - Consultas               #")
                    print("##  5 - Menu Principal          #")

                    opcao = input("Digite uma opção: ")

                    if opcao=="1":
                        os.system("clear")  
                        print("#############################")
                        print("#### VETERINÁRIOS ATIVOS #####")
                        print("#############################")
                
                        veterinarios_ativos()
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="2":
                        os.system("clear")  
                        print("#############################")
                        print("#### VETERINÁRIOS INATIVOS #####")
                        print("#############################")
                
                        veterinarios_inativos()
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="3":
                        os.system("clear")  
                        print("#############################")
                        print("#### PESQUISAR VETERINÁRIO #####")
                        print("#############################")
                
                        pes=input("Informe o início do nome: ")
                        
                        pesquisar_vet(pes)
                        
                        input("Pressione ENTER para continuar...")
                    
                    elif opcao=="4":
                        os.system("clear")
                        print("#############################")
                        print("#### CONSULTAS-VETERINÁRIOS #####")
                        print("#############################")

                        id=input("Digite o id do veterinário:")

                        veterinarios_consul(id,animais,clientes)

                        input("Pressione ENTER para continuar...")

                

                        


    
    elif resp=="6":
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
    

