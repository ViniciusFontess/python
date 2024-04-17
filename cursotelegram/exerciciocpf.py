coletacpf = input("Insira seu CPF (digite apenas números): ")
#tratar o cpf

#tirar espaços no inicio e no final 
#tirar os pontos e traços

coletacpf = coletacpf.strip()
coletacpf = coletacpf.replace("." , "")
coletacpf = coletacpf.replace("-" , "")
if len(coletacpf) == 11 and coletacpf.isnumeric :
        print(coletacpf)
else :
    print("Digite seu CPF corretamente e digite apenas números! ")



