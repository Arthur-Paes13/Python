import pandas as pd
import ssl
import matplotlib.pyplot as plt
ssl._create_default_https_context = ssl._create_unverified_context

#Baixar os dados do Github
br=pd.read_csv("https://raw.githubusercontent.com/Arthur-Paes13/Python/main/relatorio_mei.csv", header=0)
dado=pd.read_excel("https://raw.githubusercontent.com/Arthur-Paes13/Python/main/cnae.xlsx", header=0)
rj=pd.read_csv("https://raw.githubusercontent.com/Arthur-Paes13/Python/main/relatorio_mei_rio.csv", header=0)

#Unir os CSVs com o Excel para fazer um Excel com todos os dados
br=dado.merge(br, on="CNAE", how="inner")
brt= br.merge(rj, on="CNAE", how="inner")

#Tirar repetições da base de dados
brt.drop_duplicates(subset=["CNAE"],inplace=True)

# Ordenar os valores pelo total em ordem decrescente pro RJ e Brasil
brt = brt.sort_values(by="TOTAL_y", ascending=False)

brt2 = brt.sort_values(by="TOTAL_x", ascending=False)

# Selecionar os 5 maiores valores
top_5rj = brt.head(5)
top_5br = brt2.head(5)
# Criar o gráfico de barras
plt.figure(figsize=(25, 6))
plt.bar(top_5rj["Descrição"], top_5rj["TOTAL_y"])

# Adicionar título e rótulos aos eixos
plt.title("Top 5 Ocupações com Maior Total no RJ")
plt.xlabel("Ocupação")
plt.ylabel("Total")

# Mostrar a legenda
plt.legend(["Total"])

# Exibir o gráfico
plt.show()

# Criar o gráfico de barras
plt.figure(figsize=(25, 6))
plt.bar(top_5br["Descrição"], top_5br["TOTAL_x"])

# Adicionar título e rótulos aos eixos
plt.title("Top 5 Ocupações com Maior Total no BR")
plt.xlabel("Ocupação")
plt.ylabel("Total")

# Mostrar a legenda
plt.legend(["Total"])

plt.show()
