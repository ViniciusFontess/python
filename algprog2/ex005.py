n1 = int(input(" Digite um número: "))
n2 = int(input(" Digite outro número: "))
n3 = int(input(" Digite outro número: "))

if(n2>n3):
    a = n3
    n3 = n2
    n2 = a

if(n1>n3):
    a = n3
    n3 = n1
    n1 = a

if(n1>n2):
    a = n2
    n2 = n1
    n1 = a

print(" A ordem dos valores é: " + str ( n1 ) + " < " + str ( n2 ) + " < " + str ( n3 ))






    




