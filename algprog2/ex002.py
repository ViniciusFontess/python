i = int(input("Digite um valor inteiro positivo de i: "))
j = int(input("Digite um valo inteiro positivo de j: "))
m = (i + j) - (i % j)
if (i>0 and j>0) :
 print("O menor número inteiro m maior que i e múltiplo de j é:  " + str(m))
else :
  print(" Os números digitados não são inteiros positivos! ") 
