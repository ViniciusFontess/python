
n = int(input())
aux = n
i = -n -22
msg = ""
while i < n :
    if n % 2 == 0 :
        n = n/2 
        n = int(n)
    else :
        n = (n * 3) + 1
        n = int(n)
    msg = msg + " " + str(n)
    if n == 1 :
        break
    i = i+1   
    
print(str(aux) + "" + str(msg))
a = msg.split()
armazenar = len(a) + 1
print(armazenar)
