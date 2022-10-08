import pandas as pd
import sqlite3

# FUNÇÃO PARA REALIZAR CONEXÃO AO DB, SERÁ REUTILIZADA NO CRUD
def connect_to_db():
    conn = sqlite3.connect('desafioPandas.db')
    return conn

# FUNÇÃO QUE EXECUTA A CRIAÇÃO DA TABLE
def create_table():
    try:
        conn = connect_to_db()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS countries
            (country_id INTEGER PRIMARY KEY NOT NULL,
            [Country] TEXT,
            [Region] TEXT,
            [Population] INTEGER, 
            [Area (sq. mi.)] INTEGER,
            [Pop. Density (per sq. mi.)] REAL,
            [Coastline (coast/area ratio)] REAL, 
            [Net migration] REAL,
            [Infant mortality (per 1000 births)] REAL,
            [GDP ($ per capita)] REAL, 
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
        print("Tabela criada com sucesso!")
    except:
        print("Criação de tabela mal-sucedida")
    finally:
        conn.close()

# FUNÇÃO INSERT 
def insert_country(country):
    inserted_country = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(''' INSERT INTO countries
            (Country ,
            Region ,
            Population , 
            Area (sq. mi.) ,
            Pop. Density (per sq. mi.) ,
            Coastline (coast/area ratio) , 
            Net migration ,
            Infant mortality (per 1000 births) , 
            GDP ($ per capita),
            Literacy (%) ,
            Phones (per 1000) , 
            Arable (%) , 
            Crops (%) , 
            Other (%) ,
            Climate ,
            Birthrate ,
            Deathrate ,
            Agriculture , 
            Industry , 
            Service 
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
            (country['Country'],
             country['Region'],
             country['Population'],
             country['Area (sq. mi.)'],
             country['Pop. Density (per sq. mi.)'],
             country['Coastline (coast/area ratio)'],
             country['Net migration'],
             country['Infant mortality (per 1000 births)'],
             country['GDP ($ per capita)'],
             country['Literacy (%)'],
             country['Phones (per 1000)'],
             country['Arable (%)'],
             country['Crops (%)'],
             country['Other (%)'],
             country['Climate'],
             country['Birthrate'],
             country['Deathrate'],
             country['Agriculture'],
             country['Industry'],
             country['Service']
            ),)

        conn.commit()
        inserted_country = get_country_by_id(cur.lastrowid)
    except:
        conn().rollback()

    finally:
        conn.close()

    return inserted_country

# FUNÇÃO GET (GENERALIZADA)
def get_countries():
    countries = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries")
        rows = cur.fetchall()

        # CONVERNTENDO AS LINHAS EM DICIONARIO PARA RETORNO E PERCORRENDO
        country = {}
        for i in rows:
             country['Country'] = i['Country'],
             country['Region'] = i['Region'],
             country['Population'] =i['Population'],
             country['Area (sq. mi.)'] = i['Area (sq. mi.)'],
             country['Pop. Density (per sq. mi.)'] = i['Pop. Density (per sq. mi.)'],
             country['Coastline (coast/area ratio)'] = i['Coastline (coast/area ratio)'],
             country['Net migration'] = i['Net migration'],
             country['Infant mortality (per 1000 births)'] = i['Infant mortality (per 1000 births)'] ,
             country['GDP ($ per capita)'] = i['GDP ($ per capita)'],
             country['Literacy (%)'] = i['Literacy (%)'],
             country['Phones (per 1000)'] = i['Phones (per 1000)'],
             country['Arable (%)'] = i['Arable (%)'],
             country['Crops (%)'] = i['Crops (%)'],
             country['Other (%)'] = i['Other (%)'],
             country['Climate'] = i['Climate'],
             country['Birthrate'] = i['Birthrate'],
             country['Deathrate'] = i['Deathrate'],
             country['Agriculture'] = i['Agriculture'],
             country['Industry'] = i['Industry'],
             country['Service'] = i['Service']
             countries.append(country)
             print(countries)
    except Exception as e:
        print('ERROR', e, type(e))
        raise e        
    finally:
        conn.close()

    print(countries, 'aloha')
    return countries

# FUNÇÃO PARA CAPTURAR UM PAÍS PELO ID
def get_country_by_id(country_id):
    country = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM countries WHERE country_id = ?", 
        (country_id))
        row = cur.fetchone()

        # CONVERNTENDO AS LINHAS EM DICIONARIO PARA RETORNO
        country = {}
        country['Country'] = row['Country'],
        country['Region'] = row['Region'],
        country['Population'] =row['Population'],
        country['Area (sq. mi.)'] = row['Area (sq. mi.)'],
        country['Pop. Density (per sq. mi.)'] = row['Pop. Density (per sq. mi.)'],
        country['Coastline (coast/area ratio)'] = row['Coastline (coast/area ratio)'],
        country['Net migration'] = row['Net migration'],
        country['Infant mortality (per 1000 births)'] = row['Infant mortality (per 1000 births)'],
        country['GDP ($ per capita)'] = row['GDP ($ per capita)'],
        country['Literacy (%)'] = row['Literacy (%)'],
        country['Phones (per 1000)'] = row['Phones (per 1000)'],
        country['Arable (%)'] = row['Arable (%)'],
        country['Crops (%)'] = row['Crops (%)'],
        country['Other (%)'] = row['Other (%)'],
        country['Climate'] = row['Climate'],
        country['Birthrate'] = row['Birthrate'],
        country['Deathrate'] = row['Deathrate'],
        country['Agriculture'] = row['Agriculture'],
        country['Industry'] = row['Industry'],
        country['Service'] = row['Service']
        
    except:
        country = {}

    finally:
        conn.close()

    return country

# FUNÇÃO PARA ATUALIZAR O PAÍS
def update_country(country):
    updated_country = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute('''UPDATE countries SET Country = ?,
            Region = ? ,
            Population = ? , 
            Area (sq. mi.) = ? ,
            Pop. Density (per sq. mi.) = ? ,
            Coastline (coast/area ratio) = ? , 
            Net migration = ? ,
            Infant mortality (per 1000 births) = ? , 
            GDP ($ per capita) = ?,
            Literacy (%) = ? ,
            Phones (per 1000) = ? , 
            Arable (%) = ? , 
            Crops (%) = ? , 
            Other (%) = ? ,
            Climate = ? ,
            Birthrate = ? ,
            Deathrate = ? ,
            Agriculture = ? , 
            Industry = ? , 
            Service = ?  ''',  
            (country['[Country] '],
             country['Region'],
             country['Population'],
             country['Area (sq. mi.)'],
             country['Pop. Density (per sq. mi.)'],
             country['Net migration'],
             country['Infant mortality (per 1000 births)'],
             country['GDP ($ per capita)'],
             country['Literacy (%)'],
             country['Phones (per 1000)'],
             country['Arable (%)'],
             country['Crops (%)'],
             country['Other (%)'],
             country['Climate'],
             country['Birthrate'],
             country['Deathrate'],
             country['Agriculture'],
             country['Industry'],
             country['Service'],))

        conn.commit()
        #RETORNAR O PAÍS ATUALIZADO
        updated_country = get_country_by_id(country["country_id"])

    except:
        conn.rollback()
        updated_country = {}

    finally:
        conn.close()

    return updated_country

# FUNÇÃO PARA DELETAR PAÍS
def delete_country(country_id):
    msg = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from countries WHERE country_id = ?",     
                      (country_id,))
        conn.commit()
        msg["status"] = "País removido com sucesso"
    except:
        conn.rollback()
        msg["status"] = "Não foi possível remover o país"
    finally:
        conn.close()

    return msg



# df = pd.read_csv("countries_of_the_world.csv", decimal=',')
# dfClean = df.drop(['Coastline (coast/area ratio)', 'GDP ($ per capita)'], axis = 'columns')
# dfClean.to_sql('countries',connect_to_db(), if_exists='append', index = False)

