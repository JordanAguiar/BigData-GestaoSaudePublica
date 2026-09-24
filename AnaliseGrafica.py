import pandas as pd
import matplotlib.pyplot as plt

#Testando Pandas e Matplot
colunas = [
    "CPF",
    "Nome",
    "Idade",
    "DataNascimento",
    "Sexo",
    "Vacina",
]
df = pd.read_csv("registro.csv", names = colunas)


print(df.to_string())

# mediaIdade = df['Idade'].mean()
# tentando fazer isso com a data de nascimento para poder tirar o registro idade
def plotFaixaEtaria(df, dt = "DataNascimento"):
    data_Nasc = pd.to_datetime(
    df["DataNascimento"].astype(str).str.zfill(8), format="%d%m%Y", errors="coerce"
    )
    hj = pd.Timestamp.now()
    df['Idade'] = (hj - data_Nasc).dt.days / 365.25
    mediaIdade = df['Idade'].mean()





print(f"media de idade de pessoas vacinadas: {mediaIdade:.2f}")

df['Idade'].plot(kind='hist',
                 edgecolor='black')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.show()