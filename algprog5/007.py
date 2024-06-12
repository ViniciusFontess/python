numeros = input().split()
vetor = []
i = 0
menor= None
while i < len(numeros) :
    vetor.append(int(numeros[i]))
    i+=1
i = 0
while i < len(vetor) : 
    if i == 0 :
        menor= vetor[0]
    if menor> vetor[i] :
        menor = vetor[i]
    i+=1    
print(menor)  
