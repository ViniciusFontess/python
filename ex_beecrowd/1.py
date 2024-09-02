A, B = input().split(" ")

vetor_a = [int(x) for x in A]
vetor_b = [int(x) for x in B]


if vetor_a[0] == 0 and vetor_b[0] == 0:
    print(" ")


tamanho_a = len(vetor_a) 
tamanho_b = len(vetor_b) 

numero_a = ""
numero_b = ""

if tamanho_a == 1 and tamanho_b == 1:
    numero_a = vetor_a[0]
    numero_b = vetor_b[0]

elif tamanho_a == 1:    
    numero_a = vetor_a[0]

elif tamanho_b == 1:
    numero_b = vetor_b[0]

else:    
    i = 0
    while i < tamanho_a - 1: 
           numero_a = vetor_a[i]
           numero_a += ""
           i+=1
    while i < tamanho_b - 1: 
           numero_b = vetor_b[i]
           numero_b += ""
           i+=1    


numero_a = int(numero_a)
numero_b = int(numero_b)

contador_posicoes = [0]*9
i = 0

while i < len(contador_posicoes):
      contador_posicoes[i] = int(contador_posicoes[i])
      i+=1
print(contador_posicoes)

if numero_a < numero_b:
       aux = numero_a
       numero_a = numero_b
       numero_b = aux


armazenar = []
armazenar.append(numero_a)

while numero_a >= numero_b :   
    i = 0
    while i < len(armazenar) :
        if armazenar[i] == 0:
                contador_posicoes[0]+=1
        elif armazenar[i] == 1:
                contador_posicoes[1]+=1
        elif armazenar[i] == 2:
                contador_posicoes[2]+=1   
        elif armazenar[i] == 3:
                contador_posicoes[3]+=1                
        elif armazenar[i] == 4:
                contador_posicoes[4]+=1   
        elif armazenar[i] == 5:
                contador_posicoes[5]+=1   
        elif armazenar[i] == 6:
                contador_posicoes[6]+=1     
        elif armazenar[i] == 7:
                contador_posicoes[7]+=1   
        elif armazenar[i] == 8:
                contador_posicoes[8]+=1   
        elif armazenar[i] == 9:
                contador_posicoes[9]+=1
        i+=1
    numero_a+=1

    print(contador_posicoes[0] + " " + contador_posicoes[1] + " " + contador_posicoes[2] + " " + contador_posicoes[3] + " " + contador_posicoes[4] + " " + contador_posicoes[5] + " " + contador_posicoes[6] + " " + contador_posicoes[7] + " " + contador_posicoes[8] + " " +  contador_posicoes + "\n")
    
