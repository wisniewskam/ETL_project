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
file = 'payments.csv'
file_path = os.path.join(cur_path, 'data_files', file)
print(file_path)

# create new column "creditCategory" based on "creditLimit"
query = "SELECT checkNumber, paymentDate, amount, customerNumber  " \
        "FROM payments;"

df = pd.read_sql_query(query, engine)

'''
df.set_index('checkNumber', inplace=True)
df = df.stack().reset_index()
'''

df.columns = ['orderID', 'payment date', 'amount', 'customer']

df.to_csv(file_path, index=False)