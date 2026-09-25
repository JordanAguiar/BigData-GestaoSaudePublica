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
    media = pfizer["Idade"].mean()
    print(f"A media de idade das pessoas que mais se vacinaram com a pfizer é de {media:.1f} anos")

def pfizerModaIdade():
    moda = pfizer["Idade"].mode().iloc[0]
    print(f"Pessoas com {moda} anos são as que mais foram vacinas.")

#So quem tomou CoronaVac
coronavac = df[df["Vacina"] == "CORONAVAC"]

def coronavacTomadas(): 
    print(f"Registro de pessoas que so tomaram coronavac:\n{coronavac}")

def coronavacMediaIdade():
    media = coronavac["Idade"].mean()
    print(f"A media de idade das pessoas que mais se vacinaram com a coronavac é de {media:.1f} anos")

def coronavacModaIdade():
    moda = coronavac["Idade"].mode().iloc[0]
    print(f"Pessoas com {moda} anos são as que mais foram vacinas.")


#So quem tomou Astrazeneca
astrazeneca = df[df["Vacina"] == "ASTRAZENECA"]

def astrazenecaTomadas(): 
    print(f"Registro de pessoas que so tomaram astrazeneca:\n{astrazeneca}")


def astrazenecaMediaIdade():
    media = astrazeneca["Idade"].mean()
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
    #para aumentar o retangulo do grafico
    plt.figure(figsize = (9, 6))

    # usando data de nascimento para calcular a idade
    data_Nasc = pd.to_datetime(
    df[dt].astype(str).str.zfill(8), format="%d%m%Y", errors="coerce"
    )

    # calculo para saber a idade 
    hj = pd.Timestamp.now()
    df['Idade'] = (hj - data_Nasc).dt.days // 365.25

    # cria os grupos
    # não sei se tiro os jovens...
    df["faixa_etaria"] = pd.cut(df["Idade"],
                                bins = [-1, 12, 17, 29, 59, 99],
                                labels = [
                                            "Crianças (0-12)",
                                            "Adolescentes (13-17)",
                                            "Jovens (18-29)",
                                            "Adultos (30-59)",
                                            "Idosos (60+)"
                                    ]
                            )
    # calculando a porcentagem de pessoas vacinadas em cada grupo
    cont = df["faixa_etaria"].value_counts(normalize = True,
                                          sort = False) * 100
    # o grafico de barras
    gra = cont.plot(kind = "bar", color = "#3895e7c9", edgecolor = "black")
    plt.title("Porcentagem de Vacinados por Faixa Etária")
    plt.xlabel("Faixa Etária (grupos)")
    plt.ylabel("Porcentagem (%)")
    plt.xticks(rotation=10)
    # para colocar a porcentagem em cima das barras
    for i in gra.patches:
        gra.annotate(f"{i.get_height():.1f}%",
                     (i.get_x() + i.get_width() / 2.0, i.get_height()),
                     ha = "center",
                     va = "bottom",
                     xytext = (0, 3),
                     textcoords = "offset points")
    plt.tight_layout()
    plt.show()   
