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
        print("##  0- Sair                      #")
        opcao = input("Digite uma opção: ")

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
    elif resp == '4':
        # A inteção inicial desse módulo é associar consultas com os Animais e veterinários ou com um apenas.
        # Ver se é melhor criar um dicionário aqui ou dentro dos outros módulos.
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
        if opcao=="0":
            pass
        elif opcao=="2":
            print("JIOdjoidf")

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
    

