n = int(input()) 
i = 0
crescente = 0
verificar = 0
while (i<n) :
    n1 = int(input()) 
    if n1 > crescente :
        crescente = n1 
        verificar = 1

        crescente = n1
    
    i=i+1
if(verificar==1) :
    print("Os núumeros estao em ordem crescente")
else :
    print("Os núumeros estao em ordem decrescente")




