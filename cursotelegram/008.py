
meta_funcionario = 1000
meta_loja = 25000
vendas_funcionario = 15000
vendas_loja = 280000
if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja :
    bonus = 0.03 * vendas_funcionario
    print("O bônus do funcionário foi de {}" .format(bonus))
else :
    print("O funcionário não ganhou o bônus! ")    

notafuncionario = 9
meta_nota = 9
if notafuncionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja) :
    bonus2 = 0.03 * vendas_funcionario
    print("O bônus do funcionário foi de {} " .format(bonus2))
else :
    print("O funcionário não ganhou o bônus! ")
