diaria = int(input("Qual é o preço da diária deste apartamento em R$? "))
aps = int(input("Qual o número de apartamentos que vocês possuem? "))
valorpromo = diaria * 0.75
valortotal = valorpromo * aps 
valorsetenta = aps * 0.7 * valorpromo 
valorsempromo = diaria * aps 
input("O valor promocional da diária será de: R$ " + str(valorpromo))
input("O valor total arrecado, caso neste fim de semana o hotel atinja total ocupação será de: R$ " + str(valortotal))
input("Valor total a ser arrecadado caso a ocupação neste final de semana atinja 70%: R$ " + str(valorsetenta))
input("Valor que o hotel deixará de arrecadar caso em virtude da promoção caso atinga a total ocupação será de: R$ " + str(valorsempromo)) 