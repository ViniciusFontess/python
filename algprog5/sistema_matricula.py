#Sistema de matricula com persistência de dados via arquivo

#data = open("matricula.txt" , "r")
#ler_linha = data.readlines()
#data.close()


#data = open("matricula.txt" , "w")
#data.write()
#data.close()

#data = open("matricula.txt" , "a")
#data.write()
#data.close()

#REMOVER ALUNO

"""def remover(cpf):
    i = 0
    while i < len(ler_linha0): 
        mensagem0 = ler_linha0[i].split("-")
        dados = ""
        nome = mensagem0[0]
        cpf = mensagem0[1]
        if cpf + "\n" != cpf_aluno:
            dados += cadastrar_nome_aluno + " - " + cpf_aluno
        else :
            print("Digite um cpf que não exista na lista! ")
    i+=1       
    data1 = open("matricula.txt" , "w")
    data1.write(dados)    
    data1.close()"""

#EDITAR ALUNO 
"""def editar_aluno"""




def borda():
    print("****************************************")
print("Progama iniciado")
continua = True
i = 0
while continua:
    continua = False
    borda()
    print("1- Cadastrar aluno, Editar aluno, Remover aluno ou Listar alunos")
    print("2- Cadastrar matrícula, Editar matrícula, Remover matrícula ou Listar Disciplinas")
    print("3- Matricular aluno em uma Disciplina")
    print("4- Cancelar Matrícula de um estudante")
    borda()
    o_que_deseja_fazer = int(input())
    if o_que_deseja_fazer == 1:
        borda()
        print("1- Cadastrar aluno")
        print("2- Editar aluno")
        print("3- Remover aluno")
        print("4- Listar alunos")
        borda()
        o_que_deseja_fazer2 = int(input())


        #CADASTRO DE ALUNO
        
        if o_que_deseja_fazer2 == 1:  

            print("Digite o nome do aluno: ")
            cadastrar_nome_aluno = input()
            print("Digite o CPF do aluno: ")
            cpf_aluno = str(input())
            if len(cpf_aluno) == 11 : 
                continua = True
            else :
                print("Digite seu CPF corretamente e digite apenas números! ")
                continua = False    
            data = open("matricula.txt" , "a") 
            mensagem = cadastrar_nome_aluno + " - " + str(cpf_aluno)
            data.write(mensagem)
            data.close()
            data1 = open("matricula.txt" , "r")
            ler_linha = data1.readlines()

            #Enumerar os alunos da lista
            i = 0
            while i < len(ler_linha): 
                mensagem1 = ler_linha[0].split("")
                print(str(i) + "- " + str(mensagem1[0]))
                i+=1

            #Editar aluno, Nome e CPF

        if o_que_deseja_fazer == 4:
            lista_alunos = open("matricula.txt" , "r")
            print(lista_alunos)
            lista_alunos.close()
