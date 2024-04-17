produtos = ["apple tv" , "mac" , "iphone x", "Ipad", "apple watch", "mac book", "airpods"]
print(produtos)
#Adicionar um item
produtos.append("iphone 11")
print(produtos)

#Remover iphoneX
itemremovido = produtos.pop(3)
print(produtos)
print("Removemos o {} da lista".format(itemremovido))

#Remover iphoneX (forma2)
produtoremover = "iphonex"
if produtoremover in produtos:
    produtos.remove("iphonex")
else :
    print("{} não está na lista! ".format(produtoremover))

#Try e except e pass(tratar o erro)
try :
    produtos.remove("iphonex")
    print(produtos)
except :
    pass
