import  os

resp = ''

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
        print("##  0- Sair                      #")
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
            id=input("ID:")


    elif resp == '2':
        
        os.system("clear")
        
        print("#############################")
        print("#### MÓDULO- ANIMAIS #####")
        print("#############################")
        print("##  1 - Cadastrar Animal         #")
        print("##  2 - Exibir dados de Animal   #")
        print("##  3 - Alterar dados de Animal  #")
        print("##  4 - Excluir Animal           #")
        print("##  0- Sair                      #")
        opcao = input("Digite uma opção: ")

        if opcao=="1":
            
            os.system("clear")  
            
            print("#############################")
            print("#### Cadastrar Animal #####")
            print("#############################")
            print()
            nome=input("Nome:")
            dta_nas=input("Data de nascimento(xx/xx/xxx):")
            cpf=input("Tipo:")
            fone=input("Raça:")
            id=input("ID:")
            id_clie=input("Digite o id do cliente:")
    
    elif resp == '3':
        
        os.system("clear")  
        
        print("#############################")
        print("#### MÓDULO- VETERINÁRIOS #####")
        print("#############################")
        print("##  1 - Cadastrar Veterinário         #")
        print("##  2 - Exibir dados de Veterinário   #")
        print("##  3 - Alterar dados de Veterinário  #")
        print("##  4 - Excluir Veterinário           #")
        print("##  0- Sair                           #")
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
            id=input("ID:")
    
    elif resp == '4':
        os.system("clear")  
        
        print("#############################")
        print("#### MÓDULO- CONSULTAS #####")
        print("#############################")
        print("##  1 - Cadastrar Consulta         #")
        print("##  2 - Exibir dados de Consulta   #")
        print("##  3 - Alterar dados de Consulta  #")
        print("##  4 - Excluir Consulta           #")
        print("##  0- Sair                        #")
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
            dta_consul=input("Data:")
            status=input("Status:")

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
    

