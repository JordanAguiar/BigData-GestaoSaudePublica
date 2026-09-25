import csv
import AnaliseGrafica

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
    vacinaAplicada = int(input("Escolha: "))
    match vacinaAplicada:
         case 1:
              return "ASTRAZENECA"
         case 2:
              return "PFIZER"
         case 3:
              return "CORONAVAC" 

def analiseInformacoes():
    print("""
    Qual vacina voce quer analisar:
    1 - PFIZER
    2 - CORONAVAC
    3 - ASTRAZENECA
    4 - Se deseja apenas ver o comparativo entre as 3 vacinas
    """)
    analise = int(input("Digite um numero: "))
    match analise:
        case 1:
            print("""
            O que voce quer analisar?
                1 - Registro de pessoas que tomaram Pfizer
                2 - Media de idade de pessoas que tomaram Pfizer
                3 - Moda da idade de pessoas que tomaram Pfizer
            """)
            decisao = int(input("Escolha um número: "))
            match decisao:
                case 1:
                    AnaliseGrafica.pfizerTomadas()
                case 2:
                    AnaliseGrafica.pfizerMediaIdade()
                case 3:
                    AnaliseGrafica.pfizerModaIdade()
                case _:
                    print("Digito incorreto!!")
        case 2:
            print("""
            O que voce quer analisar?
                1 - Registro de pessoas que tomaram Coronavac
                2 - Media de idade de pessoas que tomaram Coronavac
                3 - Moda da idade de pessoas que tomaram Coronavac
            """)
            decisao = int(input("Escolha um número: "))
            match decisao:
                case 1:
                    AnaliseGrafica.coronavacTomadas()
                case 2:
                    AnaliseGrafica.coronavacMediaIdade()
                case 3:
                    AnaliseGrafica.coronavacModaIdade()
                case _:
                    print("Digito incorreto!!")
        case 3:
            print("""
            O que voce quer analisar?
                1 - Registro de pessoas que tomaram astrazeneca
                2 - Media de idade de pessoas que tomaram astrazeneca
                3 - Moda da idade de pessoas que tomaram astrazeneca
            """)
            decisao = int(input("Escolha um número: "))
            match decisao:
                case 1:
                    AnaliseGrafica.astrazenecaTomadas()
                case 2:
                    AnaliseGrafica.astrazenecaMediaIdade()
                case 3:
                    AnaliseGrafica.astrazenecaModaIdade()
                case _:
                    print("Digito incorreto!!")
        case 4:
              AnaliseGrafica.comparacaoVacinas()
        case _:
            print("Digito incorreto!!")