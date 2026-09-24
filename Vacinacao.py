import csv
import funcoes

''' def criacaoPlanilha():
    with open("registro.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["CPF","Nome", "Idade","DataNasc", "Sexo", "Situação"])

def adicionarPaciente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    # idade = input("Idade: ")
    dataNasc = input("Data de Nascimento: ")
    sexo = input("Sexo(M/F): ")
    verificacao = input("Vacina(s/n): ")
    if verificacao == "n":
        vacinaA = "VacinadoPE"
        with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([cpf, nome, dataNasc, sexo, vacinaA])
    else:
        vacinaB = "Vacinado"
        with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([cpf, nome, dataNasc, sexo, vacinaB])

def verificarPaciente():
    with open("registro.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)  '''     
                
#Status sistema
sistema = "on"

#Loop de Registro
while (sistema != "off"):
    print(""""
    ###############Painel###############
    # 1- Criar Planilha                #
    # 2- Adicionar Paciente            #
    # 3- Verificar Pacientes           #
    # 4- Consultar Paciente            #
    # 5- Cadastrar Vacina              #
    # 6- Listar Vacinas                #
    # 7- Finalizar Programa            #
    ####################################
    """) 
    painel = int(input())
    match painel:
        case 1:
            funcoes.criacaoPlanilha()
        case 2:
            funcoes.adicionarPaciente()
        case 3:
            funcoes.verificarPaciente()
        case 4:
            funcoes.consultarPaciente()
        case 5:
            funcoes.cadastroVacina()
        case 6:
            funcoes.listarVac()
        case 7:
            sistema = "off"
        case _:
            print("Opção inválida!!")




