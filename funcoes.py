import csv
import random

def criacaoPlanilha():
    with open("registro.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["CPF","Nome", "Idade","DataNasc", "Sexo", "Situação"])

# vai ser registrado o nome ou o codigo da vacina que ele vai tomar
def adicionarPaciente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    dataNasc = input("Data de Nascimento: ")
    sexo = input("Sexo(M/F): ")
    verificacao = input("Vacina: ")
    with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([cpf, nome, idade, dataNasc, sexo, verificacao])
    # verificacao = input("Vacina(s/n): ")
    ''' if verificacao == "n":
        # vacinaA = "VacinadoPE"
        vacinaA = "Pendente"
        with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([cpf, nome, idade, dataNasc, sexo, vacinaA])
    else:
        vacinaB = "Vacinado"
        with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow([cpf, nome, idade, dataNasc, sexo, vacinaB]) '''

def verificarPaciente():
    with open("registro.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha) 
# para fazer busca por CPF, a intenção é fazer isso quando o paciente já for registrado
# assim não será cadastrado de novo e apenas atualizamos os dados
# talvez algo que crie outro arquivo apenas para registro das vacinas e do cpf do paciente
def consultarPaciente():
    cpf = input("Digite o CPF do paciente que deseja consultar: ")
    with open("registro.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] == cpf:
                print(f"CPF: {linha[0]}")
                print(f"Nome: {linha[1]}")
                print(f"Idade: {linha[2]}")
                print(f"Data de Nascimento: {linha[3]}")
                print(f"Sexo: {linha[4]}")
                print(f"Vacinas: {linha[5]}")
                return
        print("Paciente não encontrado.")   

def cadastroVacina():
      id = random.randint(1, 100)
      nomeVac = input("Informe o nome do medicamento: ")
      fabricante = input("Informe o fabricante do medicamento: ")
      lote = input("Informe o lote do medicamento: ")
      with open("vacinas.csv", "a", newline="", encoding="utf-8") as arquivo:
          escritor = csv.writer(arquivo)
          escritor.writerow([id,nomeVac, fabricante, lote])

def listarVac():
    with open("vacinas.csv", "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha) 