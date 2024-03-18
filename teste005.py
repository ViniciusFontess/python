download = int(input("Qual o tamanho do arquivo em MB para o download? "))
velocidade = int(input("Qual é a sua velocidade de download em Mbps da sua internet? "))
calculo = int(round((download / velocidade) /60,2))
print("O tempo aproximado de download do arquivo usando este link será de " + str(calculo) + " minutos ")


                
                 