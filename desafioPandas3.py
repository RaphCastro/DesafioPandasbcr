import pandas as pd
import psycopg2

# 3 - pegue todas as colunas e linhas da planilha exceto as colunas coastline e gdp , suba em um banco sql em uma unica table 
# USE O CSV (countries_of_the_world)


config= {
    "host"      : "localhost",
    "database"  : "desafioPandas",
    "user"      : "postgres",
    "password"  : "12021999"
    }

#  Função para Conectar ao PostGres 
def connect(config):
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**config)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

#  Função de Inserção
def insertRequest(conn, insert_req):
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()

conn = connect(config)

df = pd.read_csv("countries_of_the_world.csv", decimal=',')
dfClean = df.drop(['Coastline (coast/area ratio)', 'GDP ($ per capita)'], axis = 'columns')
dfClean.to_csv()



# def createTable(cursor):
#     cursor.execute("""
#     DROP TABLE IF EXISTS desafioPandas; CREATE
#     UNLOGGED TABLE desafioPandas(
#         'Country' TEXT, 
#         'Region' TEXT, 
#         'Population' INTEGER, 
#         'Area (sq. mi.)' INTEGER,
#        'Pop. Density (per sq. mi.)' NUMERIC, 
#        'Net migration' NUMERIC,
#        'Infant mortality (per 1000 births)' NUMERIC, 
#        'Literacy (%)' NUMERIC,
#        'Phones (per 1000)' NUMERIC, 
#        'Arable (%)' NUMERIC, 
#        'Crops (%)' NUMERIC, 
#        'Other (%)' NUMERIC,
#        'Climate' NUMERIC,
#        'Birthrate' NUMERIC,
#        'Deathrate' NUMERIC,
#        'Agriculture' NUMERIC, 
#        'Industry' NUMERIC, 
#        'Service' NUMERIC
#     );
#     """) 

for i in dfClean.index:
    query = """
    INSERT into desafioPandas(column1, column2, column3) values('%s',%s,%s);
    """ % (dfClean['column1'], dfClean['column2'], dfClean['column3'])
    single_insert(conn, query)

conn.close()

print(dfClean.dtypes)



