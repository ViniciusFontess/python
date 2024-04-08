vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700
meta = 1000
if vendas_funcionario1 >= meta :
    if vendas_funcionario1 >= 2000 :
        bonus15 = vendas_funcionario1 * 0.15
        print("O funcionário 1 ganhou {} R$ de bônus ".format(bonus15))
    elif vendas_funcionario1 < 2000 :
        bonus1 = vendas_funcionario1 * 0.1
        print("O funcionário 1 ganhou {} R$ de bônus ".format(bonus1))
else :  
    print("O funcionário 1 ganhou 0 R$ de bônus ") 
if vendas_funcionario2 >= meta :
    if vendas_funcionario2 >= 2000 :
        bonus16= vendas_funcionario2 * 0.15
        print("O funcionário 2 ganhou {} R$ de bônus " .format(bonus16))   
    elif vendas_funcionario2 < 2000 :   
        bonus2 = vendas_funcionario2 * 0.1
        print("O funcionário 2 ganhou {} R$ de bônus " .format(bonus2))    
else :
    print("O funcionário 2 ganhou 0 R$ de bônus ") 
if vendas_funcionario3 >= meta :
    if vendas_funcionario3 >= 2000: 
        bonus17 = vendas_funcionario3 * 0.15
        print("O funcionário 1 ganhou {} R$ de bônus ".format(bonus17))
    elif vendas_funcionario3 < 2000 :
        bonus3 = 2700 * 0.1
        print("O funcionário 3 ganhou {} R$ de bônus " .format(bonus3))    
else :
    print("O funcionário 3 ganhou 0 R$ de bônus ") 
