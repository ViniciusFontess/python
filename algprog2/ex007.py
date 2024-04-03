numero = int(input(" Digite um número: "))
if (numero%10 == 0) :
   print(" O número digitado é divisível pelos númerros 10, 5 e 2 ")
elif (numero%5 == 0 and numero%2 == 1) :
   print(" O número digitado é divisível apenas pelo número 5 ")
elif (numero%5 ==0 and numero%2 ==0 ) :
   print(" O número digitado é divisível pelos números 5 e 2") 
elif (numero%2 == 0 ) :
   print(" O número digitado é divisível apenas pelo número 2 ")
else :
   print(" O número digitado não é divisível por 10, 5 e 2 ")



      
  