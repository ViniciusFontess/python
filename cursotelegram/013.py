#Funções python

texto = "lira"
texto1 = "Lira"
print(texto.capitalize()) #Deixar a primeira letra em maiúsculo
print(texto1.casefold()) #Deixar a primeira letra em minúsculo
texto3 = "lira@yahoo.com.br"
print(texto3.count(".")) #Contar a quantidade dentro do argumento
print(texto3.endswith("yahoo.com.br")) #Verifica se é verdadeiro ou falso o que possui dentro da variável
print(texto3.find("@"))
texto4 = "João123"
print(texto4.isalnum()) #Obs: seria falso se o texto fosse Jo~ao ou Joao#
print(texto4.isalpha()) #Obs: nesse caso João123 é falso, pois não apresenta somente números
print(texto4.isnumeric()) 
texto5 = "1000.00"
print(texto5.replace('.' , ',')) #Obs: A primeira posição é o que você quer trocar, já a segunda é o que você quer colocar no lugar
texto6 = "lira@gmail.com"
print(texto6.split("@")) #Obs: essa função irá separar/quebrar em dois lados a partir do argumento
print(texto6[4:])  
print(texto6[: -10])
texto7 = """Olá bom dia 
Venho por meio deste email lhe informar o faturamento da loja no dia de hoje.
Faturamento = 2.500,00
"""
print(texto7.splitlines()) #Obs: essa função vai colocar vírgula e parar a cada enter no teclado
texto8 = " BEB123453 "
print(texto8.strip()) #Obs: ele vai tirar os espaços inúteis do dado fornecido
texto9 = "vinicius fontes de andrade"
print(texto9.title())
print(texto9.upper())


