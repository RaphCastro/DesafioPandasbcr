import pandas as pd

df = pd.read_csv("countries_of_the_world.csv", decimal=',')

america = {}
africa = {}
asia = {}
europa = {}
oceania = {}

for column in df.columns.values:
    america[column] = []
    africa[column] = []
    asia[column] = []
    europa[column] = []
    oceania[column] = []

for index in range(len(df)):
    Regions = df.loc[index,['Region'][0]]

    if "LATIN AMER. & CARIB" in Regions:
        for column in df.columns.values:
            america[column].append(df.loc[index,[column]][0])
    elif "NORTHERN AMERICA" in Regions:
        for column in df.columns.values:
            america[column].append(df.loc[index,[column]][0])
    elif "NORTHERN AFRICA" in Regions:
        for column in df.columns.values:
            africa[column].append(df.loc[index,[column]][0])
    elif "SUB-SAHARAN AFRICA" in Regions:
        for column in df.columns.values:
            africa[column].append(df.loc[index,[column]][0]) 
    elif "ASIA (EX. NEAR EAST)" in Regions:
        for column in df.columns.values:
            asia[column].append(df.loc[index,[column]][0])
    elif "NEAR EAST" in Regions:
        for column in df.columns.values:
            asia[column].append(df.loc[index,[column]][0])
    elif "OCEANIA" in Regions:
        for column in df.columns.values:
            oceania[column].append(df.loc[index,[column]][0])
    elif "EASTERN EUROPE" in Regions:
        for column in df.columns.values:
            europa[column].append(df.loc[index,[column]][0])
    elif "WESTERN EUROPE" in Regions:
        for column in df.columns.values:
            europa[column].append(df.loc[index,[column]][0])

america = pd.DataFrame(america)
africa = pd.DataFrame(africa)
asia = pd.DataFrame(asia)
oceania = pd.DataFrame(oceania)
europa = pd.DataFrame(europa)

america.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)
africa.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)
asia.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)
oceania.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)
europa.sort_values(["Pop. Density (per sq. mi.)"], ascending=False, inplace=True)

america.to_csv("America.csv", index=False)
africa.to_csv("Africa.csv", index=False)
asia.to_csv("Asia.csv", index=False)
oceania.to_csv("Oceania.csv", index=False)
europa.to_csv("Europa.csv", index=False)