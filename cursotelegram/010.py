comando = input("Digite o nome do produto: ")
comando2 = input("Digite a categoria do produto: ")
comando3 = int(input("Digite a quantidade atual no estoque desse produto: "))
if comando and comando2 and comando3 :
    if comando2 == "alimento" or "bebida" or "limpeza" :
        if comando2 == "alimento" :
            comando3<50
            print("Solicitar {} à equipe de compras, temos apenas {} em estoque " .format(comando,comando3))
        if comando2 == "bebida" :
            comando3<75 
            print("Solicitar {} à equipe de compras, temos apenas {} em estoque " .format(comando,comando3))   
        if comando2 == "limpeza" :
            comando3<30
            print("Solicitar {} à equipe de compras, temos apenas {} em estoque " .format(comando,comando3))   
    else :
        print("Preencha corretamente as informações produto, categoria e quantidade! ")    

