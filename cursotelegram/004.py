meta = 20000
vendas = 500000

if vendas < meta :
    print("Não ganhou bônus! ")
elif vendas > (2 * vendas) :
    bonus = int(0.07 * vendas)
    print("O seu bônus é de {}! " .format(bonus))      
else : 
    bonus = int(0.03 * vendas)
    print("Ganhou {} de bônus! " .format (bonus))    
