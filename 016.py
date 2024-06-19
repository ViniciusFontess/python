valores = input().split() ## 1 4 2 3
i = 0
vetor = []
while i < len(valores):
    vetor.append(int(valores[i]))
    i+=1
i = 0
n = len(vetor)
while i <= n-2 :
    diferença = vetor[i] - vetor[i+1] ##i = 0  1-4 = -3
    if diferença < 0 :
        modulo = diferença * -1 #modulo
    else :
        modulo = diferença
    vetor_modulo = []    
    vetor_modulo.append(modulo) 
n1 = len(vetor) - 1
vetor_n = []  
vetor_n[n1] = n1
i = 0
vetor_n[0] = 1
i = 1
while i < n1 - 1:
