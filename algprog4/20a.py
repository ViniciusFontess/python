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
n1 = int(input())
n2 = int(input())
euclides = mdc(n1,n2)
print(euclides) 





