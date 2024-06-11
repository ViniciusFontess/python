gabarito = input().split()
nestudantes = int(input())
i = 0
contador = 0
aux = []
while i < nestudantes :
    j = 0
    letra_assinalada = input().split(' ')
    while j < 6 :
        if gabarito[j] == letra_assinalada[j] :
            contador+=1
        j+=1
    aux.append(contador)
    contador = 0
    
    i+=1
print(aux)
