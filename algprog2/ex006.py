h1 = input("Digite o horario ")
t1 = h1.split(":") 
h2 = input("Digite outro horario ")
t2 = h2.split(":")

hora = t1[0] + t2[0]
min = t1[1] + t2[1]
seg = t1[2] + t2[2]

if (seg>=60):
    rs = seg%60
    ms = rs
    min = ms + 1

if (min>=60) :
    rm = min%60
    mm = rm
    hora = mm + 1


print("A soma dos horarios digitados foi "+ str() + ":" + str()+ ":" + str())

