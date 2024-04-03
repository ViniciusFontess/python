"""Escreva um programa que receba dois tempos no formato hh : mm : ss (um
tempo por linha), some os dois tempos e escreva o tempo resultante. Por exemplo, para os tempos 03:10:32 e 04:55:40, você deve escrever na tela 08:06:12.
Dica: para ler os tempos, você vai precisar utilizar input.split() de uma forma
diferente da que usamos até agora, procure informações sobre a função split()
do Python.
"""
hora1 = int(input(" Digite a hora 1: "))
minuto1 = int(input(" Digite o minuto 1: "))
seg1 = int(input(" Digite o segundo 1: "))
hora2 = int(input(" Digite a hora 2: "))
minuto2 = int(input(" Digite o minuto 2: "))
seg2 = int(input(" Digite o segundo 2: "))

calculo1 = (hora1+hora2) * 3600
calculo2 = (minuto1+minuto2) * 60
calculo3 = (seg1+seg2) 

calculo4 = calculo1 + calculo2 + calculo3
horastotais = int(calculo4 / 3600)
resto = calculo4 % 3600
minutostotais = int(resto / 60)
segtotais = int(resto % 60)
if (horastotais>=24) :
    totalhoras = horastotais%24
    print("Total de horas: " + str(totalhoras))
else :
    print("Horário resultantes: " + str(horastotais))
print("Minutos resultantes: " + str(minutostotais))
print("Segundos resultantes:  " + str(segtotais))



