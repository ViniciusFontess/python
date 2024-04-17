dia = int(input("Digite aqui o dia do seu nascimento: "))
mes = int(input("Digite aqui o mês do seu nascimento: "))
ano = int(input("Digite aqui o ano do seu nascimento: "))
diaatual = int(input("Digite aqui o dia atual: "))
mesatual = int(input("Digite aqui o mes atual: "))
anoatual = int(input("Digite aqui o ano atual: "))
calculoano = anoatual - ano
if mesatual<mes and diaatual<dia :
    print("Você tem " + str(calculoano-1) + " anos de idade ")
elif mesatual>mes and diaatual>dia :
    print("Você tem " + str(calculoano) + " anos de idade ")
elif mesatual>mes and diaatual<dia :
    print("Você tem " + str(calculoano) + " anos de idade ")
elif mesatual<mes and diaatual<dia :
    print("Você tem " + str(calculoano-1) + " anos de idade ") 
else: 
    print("Digite corretamente a sua idade POR FAVOR! ")