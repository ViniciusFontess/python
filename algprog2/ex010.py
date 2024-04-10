p1 = float(input("Digite a sua nota da Prova 1: "))
p2 = float(input("Digite a sua nota da Prova 2: "))
p3 = float(input("Digite a sua nota da Prova 3: "))
ml = (p1 + p2 + p3) / 3
ma = (p1+(p2*2)+(p3*3)+(ml*2))/7
if ma >= 9 :
    print("O seu conceito é A")
elif ma>7.5 and ma<9 :
    print("O seu conceito é B")    
elif ma>=6 and ma<7.5 :
    print("O seu conceito é C")
elif ma>=4 and ma<6 :
    print("O seu conceito é D")
else :
    print("O seu conceito é E")            