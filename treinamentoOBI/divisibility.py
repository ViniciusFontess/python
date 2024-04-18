i = int(input())
while(i>0) :
    a,b = input().split()
    a = int(a)
    b = int(b)
    if b>a :
        calculo = b - a
        print(calculo)
    if a>b and a%b==0:
        calculo3 = a%b
        print(calculo3)
    if a==b :
        calculo4 = a%b
        print(calculo4)      
    elif a>b :
        calculo = a%b 
        calculo2= b - calculo 
        print(calculo2)  
    
    i=i-1



