frase = input()
tamanho = len(frase) - 1
i = 0
finversa = ""
while (tamanho >= i) :
    finversa = finversa + frase[tamanho]
    tamanho = tamanho - 1

print(finversa)

