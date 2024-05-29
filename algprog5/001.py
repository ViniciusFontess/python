n = int(input())
i = 0
soma = 0
notas = []
while i < n:
    nota = float(input())
    notas.append(nota) 
    soma = soma + nota
    i += 1
    media = soma / n

i = 0
contador = 0
while i < n :
    if notas[i] > media:
        contador += 1
    i += 1
print("Média " + str(media))    
print("Há " + str(contador) + " alunos acima da média")        