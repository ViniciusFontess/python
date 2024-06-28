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

"""def remover(cpf_aluno1):       
                ler_o_arquivo = open("matricula.txt" , "r")
                ler_linha0 = ler_o_arquivo.readlines()
                ler_o_arquivo.close()
                i = 0
                dados = ""
                while i < len(ler_linha0): 
                    mensagem0 = ler_linha0[i].split("-")
                    cpf = mensagem0[1]
                    if cpf + "\n" != cpf_aluno:
                        dados += cadastrar_nome_aluno + " - " + cpf_aluno
                        i+=1 
                    else: 
                        ("O CPF já existe no sistema, tente novamente")
                        continua = False          
                
                data1 = open("matricula.txt" , "w")
                data1.write(dados)    
                data1.close()
                adicionar_no_arquivo.close()
                data1 = open("matricula.txt" , "r")
                ler_linha = data1.readlines()
                data1.close()"""

#EDITAR ALUNO 


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
            def adicionar(cadastrar_nome_aluno,cpf_aluno):

                ler = open("matricula.txt" , "r")
                ler_linha = ler.readlines()
                ler.close()

                cpf_vetor = []
                adicionar_linhas = []

                i = 0
                while i < len(ler_linha):
                    adicionar_linhas.append(ler_linha[i].split(" - "))
                    cpf_vetor.append(adicionar_linhas[i][1])
                    i+=1

                i = 0
                existe = False
                while i < len(cpf_vetor):
                    if cpf_vetor[i] == cpf_aluno:
                        existe = True
                    i+=1    
 
                if not existe :
                    apendar = open("matricula" , "a")    
                    escrever = cadastrar_nome_aluno + " - " + cpf_aluno
                    apendar.write(escrever)
                    apendar.close()

            #Enumerar os alunos da lista
            enumerar = open("matricula.txt" , "r")
            enumerar1 = enumerar.readlines()
            enumerar.close()
            
            while i < len(enumerar1):
                mensagem = enumerar1[i].split("-")
                print("O aluno foi cadastrado na lista!! " "\n" + str(i) + " - " + str(mensagem[0] + " - " + cpf_aluno))
                i+=1

        #Remover aluno

        if o_que_deseja_fazer2 == 3:
            print("Você deseja remover qual aluno? Digite o índice: ")
            data2 = open("matricula.txt" , "r")
            printar_usuario = data2.readlines()
            data2.close()
            print(printar_usuario)
            indice = int(input())
            print(printar_usuario[indice])
            print("Tem certeza que deseja removê-lo?")
            print("1- SIM")
            print("2- NÃO")
            sim_nao = input()
            if sim_nao == "SIM":
                def remover(cpf_aluno1):       
                    ler_o_arquivo = open("matricula.txt" , "r")
                    ler_linha0 = ler_o_arquivo.readlines()
                    ler_o_arquivo.close()
                    i = 0
                    dados = ""
                    while i < len(ler_linha0): 
                        mensagem0 = ler_linha0[i].split(" - ")
                        cpf = mensagem0[1]
                        if cpf + "\n" != cpf_aluno:
                            dados += cadastrar_nome_aluno + " - " + cpf_aluno
                            i+=1 
                    else: 
                        ("O CPF já existe no sistema, tente novamente")
                        continua = False          
                    data1 = open("matricula.txt" , "w")
                    data1.write(dados)    
                    data1.close()

        if o_que_deseja_fazer2 == 4:
            lista_alunos = open("matricula.txt" , "r")
            print(lista_alunos)
            lista_alunos.close()
