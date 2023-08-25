#Trabalho do Arthur Paes, Vicente Estefan e Guilherme Mamedes

import pandas as pd
import ssl
import matplotlib.pyplot as plt
ssl._create_default_https_context = ssl._create_unverified_context

dado = pd.read_csv("https://raw.githubusercontent.com/drobaina/Python/main/microdados_ed_basica_RJ_2022.csv", header=0)

# Filtrar a Cidade de Angra dos Reis
filtrar_cidade = dado[dado['NO_MUNICIPIO'].isin(['Angra dos Reis'])]

# Agrupar as Cidades com o Acesso dos Alunos a Internet
internet = dado.groupby('NO_MUNICIPIO')['IN_INTERNET_ALUNOS'].value_counts(normalize=True).unstack()
top_internet= internet[1].nlargest(10)
cidades = ["Macuco", "Comendador Levy Gasparian","Barra do Piraí","Rio das Ostras","Três Rios","Resende","Teresópolis","Volta Redonda","Areal","Cantagalo"]
# Top 10 Cidades em % de Alunos com Acesso a Internet
plt.figure(figsize=(20, 8))
plt.bar(cidades,top_internet)
plt.title("% de Escolas com Internet pros Alunos")

escolas_RJ = dado['TP_DEPENDENCIA'].value_counts(normalize=True)
c=[1,2,3,4]
values=["Municipal","Privada","Estadual","Federal"]
plt.bar(c,escolas_RJ)
plt.title("% de Tipo de Escola no Estado de RJ")
plt.xticks(c,values)




