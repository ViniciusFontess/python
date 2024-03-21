entradadistancia = int(input("Qual é a distancia de Araçatuba até Campo Grande em km? \n"))
velocidade = int(input("E qual foi a sua velocidade em km/h? \n"))
calculotempomedio = entradadistancia / velocidade 
velms = velocidade / 3.6
print("O tempo médio para chegar ao local será de: " + str(calculotempomedio))
print("Já a sua velocidade em m/s será de: " + str(velms))