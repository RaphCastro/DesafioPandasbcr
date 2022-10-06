import pandas as pd

df = pd.read_csv("countries_of_the_world.csv", decimal=',')


# Country_Region_Popdensity = df[["Region", "Country", "Pop. Density (per sq. mi.)"]]
# print(Country_Region_Popdensity)

Country_Region_Popdensity = df[["Region", "Country", "Pop. Density (per sq. mi.)"]]
print(Country_Region_Popdensity)

