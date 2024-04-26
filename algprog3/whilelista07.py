n = int(input()) 
i = 0
aux = 0
aux1= 0
while (i<n) :
    n1 = int(input()) 
    if n1%2 == 1 :
        aux = aux + n1
        pares = aux
    elif n1%2==0 :
        aux1 = aux1 + n1
        impares = aux1
    i=i+1
print("Soma dos pares:" + str(aux))   
print("Soma dos ímpares:" + str(aux1))  