import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#NOTE:Abertura de arquivo
df = pd.read_csv("countries_of_the_world.csv", decimal=',')

#Criando dicionário vazio para se povoar com dados filtrados
obj = {}
for column in df.columns.values:
    obj[column] = []

#Percorrendo tabela
for index in range(len(df)):

    #Pegando 3 valores a se filtrar
    mortality = float(df.loc[index,['Infant mortality (per 1000 births)']][0])
    population = int(df.loc[index,['Population']][0])
    literacy = float(df.loc[index,['Literacy (%)']][0])
    
    #Condicional desejada
    if mortality > 50 and population > 2000000 and literacy > 40:
        #Povoando dicionario com valores desejados
        for column in df.columns.values:
            obj[column].append(df.loc[index,[column]][0])

#Transformando dicionário em Dataframe
dadosFinais = pd.DataFrame(obj)
print(dadosFinais)


