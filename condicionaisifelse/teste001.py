u
#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 < n2 :
    print("O maior número é o " + str(n2))
elif n2 < n1 :
    print("O maior número é o " + str(n1))
else :
    print("Estes números são iguais")

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = int(input("Digite um número: "))    
if valor > 0 :
    print("Este valor é positivo! ")
elif valor < 0 :
    print("Este valor é negativo! ")
else :
    print(" O número é 0 !! ")

 #Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo =(input("Digite seu sexo com F (feminino) ou M (masculino): "))
if sexo == 'F' : 
    print("O seu sexo é Feminino! ")      
elif sexo == 'M' :
    print("O seu sexo é Masculino ")     
else : 
    print("Sexo inválido")  

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
digite = str(input("Digite uma letra? "))
if digite == "a" or digite == "A" or digite == "E" or digite == "e" or digite == "i" or digite == "I" or digite == "o" or digite == "O" or digite == "U" or digite == "u" :
    print("Sua letra é uma vogal! ")
else :
    print("Sua letra é uma consoante! ")

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
"""
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

n1 = float(input("Qual é a sua nota de VGA Paulo? "))    
n2 = float(input("Qual é a sua nota de Cálculo I Paulo? "))
media = n1 + n2 / 2
if n1 > 10 :
    print("Esta nota é inválida! ")
elif n2 > 10 :
    print("Esta nota é inválida! ") 
else:   
    if media == 10 :
        print("Aprovado com Distinção! ")
    elif media >= 7 :
        print("Aprovado! ")    
    else : 
        print("Reprovado! ")

#Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite outro número: "))
if n1 > n2 > n3 :
    print("O maior número é o " + str(int(n1)))
if n2 > n1 > n3 :
    print("O maior número é o " + str(int(n2)))
if n1 > n3 > n2 :
    print("O maior número é o " + str(int(n1)))
if n2 > n3 > n1 :
    print("O maior número é o " + str(int(n2)))
if n3 > n1 > n2 :
    print("O maior número é o " + str(int(n3)))  
else :
    (print("O maior número é o " + str(n3)))    

                      


