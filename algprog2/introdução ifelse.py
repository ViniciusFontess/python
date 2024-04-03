print("Digite a primeira nota: ")
nota1 = input()
nota1 = float(nota1)

print("Digite a segunda nota: ")
nota2 = input()
nota2 = float(nota2)

print("Digite a terceira nota: ")
nota3 = input()
nota3 = float(nota3)

media = int(nota1+nota2+nota3) / 3
if(media<6) :
    print(" Pela sua médio você foi REPROVADO! ")
elif(media>6) :
    print(" Pela sua média você foi APROVADO! ") 
else :
    print(" A sua nota não é valida no sistema ")