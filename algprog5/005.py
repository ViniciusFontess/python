i = 0
vetor = []
n_lancamentos = int(input())
j = 37
contador = 0
while i < j :
    vetor.append(0)
    i+=1
i = 0
while i < n_lancamentos :
    n = int(input())
    vetor[n]= vetor[n]+1
    i+=1
print(vetor)    
