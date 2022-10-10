import pandas as pd


# LENDO CSV
df = pd.read_csv("../CSV/countries_of_the_world.csv", decimal=',')

# LISTAS DE CONTINENTES PARA USO NA FUNÇÃO

europe_ctn = ['EASTERN EUROPE','BALTICS','WESTERN EUROPE','C.W. OF IND. STATES']
africa_ctn = ['SUB-SAHARAN AFRICA' ,'NORTHERN AFRICA']
asia_ctn = ['C.W. OF IND. STATES', 'NEAR EAST', 'ASIA (EX. NEAR EAST)']
americas_ctn = ['LATIN AMER. & CARIB', 'NORTHERN AMERICA']
oceania_ctn = ['OCEANIA']

# FUNÇÃO QUE UTILIZA COMO PARAMETROS O NOME E A LISTA CONSUMIDA


def buildContinent(name, ctn):
    continent = {}
    for column in df.columns.values:
            continent[column] = []
    
    for index in range(len(df)):
        regions = df.loc[index,['Region']][0] 
        for i in range(len(ctn)):
            if regions.find(ctn[i]) != -1:
                for column in df.columns.values:
                    continent[column].append(df.loc[index,[column]][0])

        export = pd.DataFrame(continent) 
        export.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)
        export.to_csv(f'{name}.csv')

# FUNÇÕES RETORNANDO

buildContinent('europe', europe_ctn)
buildContinent('africa', africa_ctn)
buildContinent('asia', asia_ctn)
buildContinent('americas', americas_ctn)
buildContinent('oceania', oceania_ctn)

