import pandas as pd
import matplotlib.pyplot as plt

colunas = [
    "CPF",
    "Nome",
    "Idade",
    "DataNascimento",
    "Sexo",
    "Vacina",
]
df = pd.read_csv("registro.csv", names = colunas)

#So quem tomou Pfizer
pfizer = df[df["Vacina"] == "PFIZER"]

def pfizerTomadas(): 
    print(f"Registro de pessoas que so tomaram Pfizer:\n{pfizer}")

def pfizerMediaIdade():
    media = pfizer["idade"]
    print(f"A media de idade das pessoas que mais se vacinaram com a pfizer é de {media:.1f} anos")

def pfizerModaIdade():
    moda = pfizer["Idade"].mode().iloc[0]
    print(f"Pessoas com {moda} anos são as que mais foram vacinas.")

#So quem tomou CoronaVac
coronavac = df[df["Vacina"] == "CORONAVAC"]

def coronavacTomadas(): 
    print(f"Registro de pessoas que so tomaram coronavac:\n{coronavac}")

def coronavacMediaIdade():
    media = coronavac["idade"]
    print(f"A media de idade das pessoas que mais se vacinaram com a coronavac é de {media:.1f} anos")

def coronavacModaIdade():
    moda = coronavac["Idade"].mode().iloc[0]
    print(f"Pessoas com {moda} anos são as que mais foram vacinas.")


#So quem tomou Astrazeneca
astrazeneca = df[df["Vacina"] == "ASTRAZENECA"]

def astrazenecaTomadas(): 
    print(f"Registro de pessoas que so tomaram astrazeneca:\n{astrazeneca}")


def astrazenecaMediaIdade():
    media = astrazeneca["idade"]
    print(f"A media de idade das pessoas que mais se vacinaram com a astrazeneca é de {media:.1f} anos")

def astrazenecaModaIdade():
    moda = astrazeneca["Idade"].mode().iloc[0]
    print(f"Pessoas com {moda} anos são as que mais foram vacinas.")

#Comparação das 3 Vacinas
def comparacaoVacinas():
    contagem = df["Vacina"].value_counts()
    plt.pie(
        contagem,
        labels=contagem.index,
        autopct="%1.1f%%"
    )
    plt.title("Distribuição de pacientes por vacina")
    plt.show()


def plotFaixaEtaria(df, dt = "DataNascimento"):
    data_Nasc = pd.to_datetime(
    df["DataNascimento"].astype(str).str.zfill(8), format="%d%m%Y", errors="coerce"
    )
    hj = pd.Timestamp.now()
    df['Idade'] = (hj - data_Nasc).dt.days / 365.25
    mediaIdade = df['Idade'].mean()

