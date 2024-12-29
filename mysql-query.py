from sqlalchemy import create_engine
import pandas as pd

# to be modified - add your credentials
user = ''
password = ''
host = ''
database = ''
port = 0000

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

query = "SELECT customerName, contactLastName, contactFirstName, city FROM customers " \
        "WHERE city = 'Warszawa';"

'''
for row in cursor:
    print(row)
'''

df = pd.read_sql_query(query, engine)
print(df.head())

# datatypes check
print(df.dtypes)
print(df.shape)

# filters
customerCity = df['city'] == 'Warszawa'
print(customerCity)