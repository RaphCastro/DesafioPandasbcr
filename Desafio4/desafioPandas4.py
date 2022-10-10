import pandas as pd

# CONCATENAÇÃO DOS CSVS
df = pd.concat(
    map(pd.read_csv, ['../CSV/quality_of_life.csv', '../CSV/population_density.csv', '../CSV/life_expectancy.csv']),
    ignore_index = True
    )

# TRANSFORMAR EM DATAFRAME
mergedDf = pd.DataFrame(df)

# GERAR UM CSV A PARTIR DO DATAFRAME
mergedDf.to_csv('PlanilhaSupremaConcatenadaExtremaFinal.csv')