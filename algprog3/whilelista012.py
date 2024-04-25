n = int(input())
i = 0
maiornota = 0
menornota = 0
while (i<n) :
    n1= int(input())
    if n1>=0 and maiornota < n1 :
        maiornota = n1
    if n1>=0 and menornota < n1 :    
        menornota = n1
    i=i+1    
print("A maior nota da sala foi: " + str(maiornota))
print("A menor nota da sala foi: " + str(menornota))