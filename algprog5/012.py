n = input()
valores = n.split(" ")
i = 0
blacklist = []
while i < len(valores) :
    alvo = valores[i]
    j = 0
    contador = 0
    while j < len(valores) :
        if valores[j] == alvo :
            contador+=1
        j+=1
    print(alvo + "aconteceu" + str(contador))
    i=+1    
