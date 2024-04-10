#Exemplo espaçamento e formatação
email = "lira@gmail.com"
print("Meu email não é {:^20}, ok? " .format(email))
print("Meu email não é {:>20}, ok? " .format(email))

#Exemplo de Edição de Sinal
custo = 500
faturamento = 270
lucro = faturamento - custo
print("O faturamento foi de {:+,} e o lucro foi de {:-,}" .format(faturamento,lucro))

#Exemplo de Separador de Milhar 
custo = 5000
faturamento = 2700
lucro = faturamento - custo
print("O faturamento foi de R${:,} e o lucro foi de R${:,}" .format(faturamento,lucro))

#Exemplo com casas Decimais fixas
custo = 5000
faturamento = 270
lucro = faturamento - custo
print("O faturamento foi de {:.2f} e o lucro foi de R${:.1f}" .format(faturamento,lucro))

#Exemplo de Percentual
custo = 500
faturamento = 1300
lucro = faturamento - custo
margem = lucro / faturamento
print("A margem de lucro foi de {:.1%}" .format(margem))

#Exemplo Formato Moeda
custo = 5000
faturamento = 27000
lucro = faturamento - custo
print("O faturamento foi de R$ {:,.2f} e o lucro foi de R${:,.2f}" .format(faturamento,lucro))
#Transformando no formato brasileiro
lucro_texto = "R${:_.2f}" .format(lucro)
print(lucro_texto.replace("." , ",").replace("_" , "."))

#Função round
imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print("O valor do imposto foi de R${:.2f}" .format(valor_imposto))




      