custofabrica = float(input("Qual o custo fabril do carro em R$? "))
calculofabrica = custofabrica * 1.28
impostos = calculofabrica * 1.45
custofinalcarro = calculofabrica + impostos 
print("O custo final ao consumidor será de: R$ " + str(custofinalcarro))
