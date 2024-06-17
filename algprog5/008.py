def copia_e_converte(valores, valores_int):
    i = 0
    while i < len(valores) :
        valores_int[i] = int(valores[i])
        i+=1        


def acha_menor_elemento(v, posicao_inicial): 
    menor = v[posicao_inicial]
    posicao_do_menor = posicao_inicial
    j = posicao_inicial + 1
    while j < len(v):
        if v[j] < menor:
            menor = v[j]
            posicao_do_menor = j
        j+=1
    return posicao_do_menor 


def troca(v,i,j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux
    

def ordena(v):
    i = 0
    while i < len(v) - 1:
        posicao_do_menor = acha_menor_elemento(v,i)
        troca(v,i,posicao_do_menor)
        i+=1





entrada = input()
valores = entrada.split(" ")
valores_int = [0]* len(valores) #[0,0,0,0,0,0]
copia_e_converte(valores,valores_int)
ordena(valores_int)
print(valores_int)
