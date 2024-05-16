def mdc(a,b):
    i = 0
    aux = 0
    resto = 0
    if a == b :
        print("O mdc entre os números é " + str(n1))
    if a > b : 
        aux = a
        a = b
        b = aux
    if a % b == 0 : 
        print("O mdc entre os números é " + str(n2))
    if a % b != 0 :    
        while i < b :         
            resto = a % b
            a = b
            b = resto 
                
        i = i+1

    return(a)
n = int(input())
i = 0
a = 0
b = 0
while i < n :
    if i == 0 :
        a = int(input())
        m = a 
    else :
        b = int(input())
        m = mdc(a,b)
        a = m 
    i = i + 1
print(m)        



    




