n = int(input())
i = 0 
n2 = 0
n3 = 0
while (i<n) :
    n1 = int(input())
    if n1%2==0 : 
        n2 = n2 + 1
    if n1%2==1 :
        n3 = n3 + 1
    i=i+1    
print("O número de ímpares: " + str(n3))
print("O número de pares: " + str(n2))      