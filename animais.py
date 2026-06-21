def recuperar_dados_aniamis(animais):
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