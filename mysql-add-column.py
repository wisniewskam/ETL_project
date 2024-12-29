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
file = 'customers_credit_limits.csv'
file_path = os.path.join(cur_path, 'data_files', file)
print(file_path)

# create new column "creditCategory" based on "creditLimit"
query = "SELECT customerName, creditLimit, city,  " \
        "CASE "\
        "WHEN creditLimit < 20000 THEN 'LOW' " \
        "WHEN creditLimit < 100000 THEN 'MEDIUM' " \
        "WHEN creditLimit >= 100000 THEN 'HIGH' " \
        "END AS creditCategory " \
        "FROM customers;"

df = pd.read_sql_query(query, engine)

df.to_csv(file_path, index=False)