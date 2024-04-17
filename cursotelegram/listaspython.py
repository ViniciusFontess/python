#Associação de listas 

produtos2 =['tv', 'celular' , 'mouse', 'teclado', 'tablet']
print(produtos2[1])

vendas = [1000, 1500, 350, 270, 900]
print(vendas[1])

vendas[3] = 300
print(' As Vendas do {} foram de {} unidades' .format(produtos2[3], vendas[3]))

#As strings são imutáveis
texto = "lira@gmail.com"
texto = texto.replace("i" , "a")
print(texto)

produtos1 = ['tv', 'celular', 'tablet', 'mouse', 'teclado', 'geladeira', 'forno']
estoque = [100, 150, 100, 120, 70, 90, 80]
i = produtos1.index("geladeira")
qtdestoque= estoque[i]
print('A quantidade de estoque da geladeira é de: {} ' .format(qtdestoque))

#CRIE UM PROGRAMA PARA FAZER A CONSULTA DE ESTOQUE, CASO ELE NÃO EXISTA NA LISTA, O INFORME
produtos = input('Insira o nome do produto em letra minúscula: ')
if produtos in produtos1 :
    i = produtos1.index(produtos)
    qtdestoque = estoque[i]
    print('Temos {} unidades de {} no estoque' .format(qtdestoque, produtos))
else :
    print('{} não existe no estoque. ' .format(produtos))    






             