#https://codeforces.com/contest/1283/problem/A
i = int(input())
while(i>0):
    h,m = input().split()
    h = int(h)
    m= int(m)
    calculominutos = h*60
    soma = calculominutos + m 
    calculoanonovo = 1440 - soma
    print(calculoanonovo)
    i=i-1



