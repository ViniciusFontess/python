aplicacaomensal = int(input("Qual é o valor da sua aplicação mensal? R$ "))
taxa = float(input("Qual a taxa da aplicação? "))
meses = int(input("Qual o número de meses que você pretende investir? "))
cálculo = int((aplicacaomensal * (1+taxa)**meses - 1) / 1)
print("O valor acumulado será de: R$ " + str(cálculo))