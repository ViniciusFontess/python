n = int(input())
i = 0
vetor = []
contador = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
while i < n :
    resultado_lancamento = input()
    i+=1
    vetor.append(resultado_lancamento)
    aux = len(vetor) - 1
    j=0
    while j < len(vetor) - 1 :
        if vetor[j] == 1 :
            contador+=1
        if vetor[j] == 2 :
            contador1+=1
        if vetor[j] == 3 :
            contador2+=1
        if vetor[j] == 4 :
            contador3+=1
        if vetor[j] == 5 :
            contador4+=1
        if vetor[j] == 6 :
            contador5+=1 
        j+=1          
print(contador,contador1,contador2,contador3,contador4,contador5)      
