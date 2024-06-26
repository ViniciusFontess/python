#Sistema de matricula com persistência de dados via arquivo
print("Progama iniciado")
continua = True
i = 0
while continua:
    print("1- Cadastrar aluno, Editar aluno, Remover aluno ou Listar alunos")
    print("2- Cadastrar matrícula, Editar matrícula, Remover matrícula ou Listar Disciplinas")
    print("3- Matricular aluno em uma Disciplina")
    print("4- Cancelar Matrícula de um estudante")
    try:
        o_que_deseja_fazer = int(input())
    except KeyboardInterrupt:
        continua = False

    if o_que_deseja_fazer == 1:
        print("1- Cadastrar aluno")
        print("2- Editar aluno")
        print("3- Remover aluno")
        print("4- Listar alunos")
        o_que_deseja_fazer2 = int(input())
        if o_que_deseja_fazer2 == 1:
            print("Digite o nome do aluno: ")
            cadastrar_nome_aluno = input()
            print("Digite o CPF do aluno: ")
            cpf_aluno = int(input())
            if len(cpf_aluno) == 11 :
                continua = True
            else :
                print("Digite seu CPF corretamente e digite apenas números! ")
            data = open("matricula.txt" , "a")
            mensagem = cadastrar_nome_aluno + " - " + str(cpf_aluno)
            data.write(mensagem)
            data.close()
        if o_que_deseja_fazer == 2: 
            data1 = open("matricula.txt" , "r")
            ler_linha = data1.readlines()
            i = 0
            while i < len(ler_linha):
                mensagem1 = ler_linha[i].split("-")
                print(str(i) "- " + str(mensagem[0]))
                i+=1
            print("Qual o índice do aluno você deseja editar?")   
