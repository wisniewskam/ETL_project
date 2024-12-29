from sqlalchemy import create_engine
import pandas as pd
import os

# to be modified - add your credentials
user = ''
password = ''
host = ''
database = ''
port = 0000

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

cur_path = os.getcwd()
file = 'customers_NYC_London.csv'
file_path = os.path.join(cur_path, 'data_files', file)
print(file_path)

query = "SELECT customerName,creditLimit, city FROM customers" \
        "WHERE city = 'NYC' OR city = 'London';"

df = pd.read_sql_query(query, engine)

df.to_csv(file_path, index=False)