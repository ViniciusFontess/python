faturamento = input("Qual foi o faturamento da loja no mês? ")
custo = input("Qual foi o custo total no mês? ")
if faturamento and custo :
    lucro = int(faturamento) - int(custo)
    print("O lucro mensal foi de {} R$ " .format(lucro))
else : 
    print("Preencha o faturamento e o custo corretamente! ")


