import pandas as pd
import matplotlib.pyplot as plt

#Testando Pandas e Matplot

df = pd.read_csv("registro.csv")

print(df.to_string())

mediaIdade = df['idade'].mean()

print(f"media de idade de pessoas vacinadas: {mediaIdade:.2f}")

df['idade'].plot(kind='hist')
plt.show()