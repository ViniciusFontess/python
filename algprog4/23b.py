def quebra(n) :
    i = 0
    n = str(n)
    num = ""
    while i < len(n) :
        if i == 0 :
            pn = n[i]
        elif (i == len(n)-1) :
            um = n[i] 
        else :
            num = num + n[i]       
        i = i+1
    return pn,um,num

n = int(input()) 
x,y,z = quebra(n) 
print
i = 0 
verificarlen = len(z)
aux = 0
aux2 = 0
verificar = True
if len(z)==1 and x == y: 
    print("O número digitado é um palíndromo")
elif x != y : #condição forte para não ser palíndromo
        print("O número digitado não é palíndromo")
else : #analisar se é palíndrmo com os do meio, percorrer a string e comparar igualdade
    while i < verificarlen : 
            aux = (z[i])
            aux2 = (z[verificarlen-1]) 
            i = i+1 
            verificarlen = (verificarlen-1) 
            if aux != aux2 :   
                verificar = False
    if not verificar:
        print("O número digitado não é palíndromo")
    else :
        print("O número digitado é palíndromo")       
