import pandas as pd
import sqlite3


conn = sqlite3.connect('desafioPandas.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS desafioPandas
        ([Country] TEXT,
        [Region] TEXT,
        [Population] INTEGER, 
        [Area (sq. mi.)] INTEGER,
        [Pop. Density (per sq. mi.)] REAL,
        ['Coastline (coast/area ratio)'] REAL, 
        [Net migration] REAL,
        [Infant mortality (per 1000 births)] REAL,
        ['GDP ($ per capita)'] REAL, 
        [Literacy (%)] REAL,
        [Phones (per 1000)] REAL, 
        [Arable (%)] REAL, 
        [Crops (%)] REAL, 
        [Other (%)] REAL,
        [Climate] REAL,
        [Birthrate] REAL,
        [Deathrate] REAL,
        [Agriculture] REAL, 
        [Industry] REAL, 
        [Service] REAL
          )''')
                     
conn.commit()

# 3 - pegue todas as colunas e linhas da planilha exceto as colunas coastline e gdp , suba em um banco sql em uma unica table 
# USE O CSV (countries_of_the_world)

df = pd.read_csv("countries_of_the_world.csv", decimal=',')
dfClean = df.drop(['Coastline (coast/area ratio)', 'GDP ($ per capita)'], axis = 'columns')

dfClean.to_sql('desafioPandas', conn, if_exists='replace', index = False)


c.execute('''  
SELECT * FROM desafioPandas
          ''')