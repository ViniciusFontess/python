def troca_primitiva (x,y) :
    aux = x
    x = y
    y = aux

def troca_vetor(x, pos1, pos2) :
    aux = x[pos1]
    x[pos1] = x[pos2]
    x[pos2] = aux

a = 10
b = 20
print(a)
print(b)
troca_primitiva(a,b)
print(a)
print(b)

c= []
c.append(10)
c.append(20)

print(c[0])
print(c[1])
troca_vetor(c, 0, 1)
print(c[0])
print(c[1])
