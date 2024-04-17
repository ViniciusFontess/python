nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")


if nome and email :
    pos_a = email.find("@")
    servidor = email[pos_a:]
    if pos_a != -1 and "." in servidor :
        print("Cadastro concluído! ")    
    else :
        print("Digite seu nome ou e-mail corretamente ")

    
else : 
    print("Digite seu nome ou e-mail corretamente ")
