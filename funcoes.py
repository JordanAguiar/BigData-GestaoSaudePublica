import csv

def criacaoPlanilha():
    with open("registro.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["CPF","Nome", "Idade","DataNasc", "Sexo", "Vacina"])

# vai ser registrado o nome ou o codigo da vacina que ele vai tomar
def adicionarPaciente():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    idade = input("Idade: ")
    dataNasc = input("Data de Nascimento: ")
    sexo = input("Sexo(M/F): ")
    vacina = cadastroVacina()
    with open("registro.csv", "a", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow([cpf, nome, idade, dataNasc, sexo, vacina])

def verificarPaciente():
    with open("registro.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha) 

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
                print(f"Vacina: {linha[5]}")
                return
            
        print("Paciente não encontrado!")

                
def cadastroVacina():
    print("""
    -------------------
    | 1 - ASTRAZENECA |
    | 2 - PFIZER      |
    | 3 - CORONAVAC   |
    -------------------    
    """)
    vacinaAplicada = int(input())
    match vacinaAplicada:
         case 1:
              return "ASTRAZENECA"
         case 2:
              return "PFIZER"
         case 3:
              return "CORONAVAC" 