coletacpf = input("Insira seu CPF (digite apenas números): ")
if len(coletacpf) == 11 :
    if coletacpf.isnumeric :
        print("O seu cpf é {} " .format(coletacpf))
else :
    print("Digite seu CPF corretamente e digite apenas números ")



