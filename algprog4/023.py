def quebra(n) :
    i = 0
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
n = input()
func = quebra(n)
print(n)

