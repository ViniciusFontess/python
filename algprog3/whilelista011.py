n = int(input())
i = 1
maiorvalor = 0
maiord = 0
while (i<8) :
    n1 = int(input())
    if n1 > maiorvalor :
        maiorvalor = n1 
        maiord=i

    
    i=i+1
print("O dia com mas discos foi o " + str(maiord) + " e a quantidade de discos nesse dia foram de " + str(maiorvalor))
    