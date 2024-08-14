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

#Crie um código que recalcule o valor do livro da sua lista  de produtos e ajuste na tabela

produtos4 = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
[1000, 2500]
[50000, 40]
[7000, 1200]
[20000, 1500]
[5800, 1300]
[7200, 2500]
[200, 800]
[3300, 700]
[1900, 400]

]

if 'livro' in produtos4:
    i_livro = produtos4.index('livro')
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1]*1.1
    print(produtos_ecommerce[i_livro][1])




             