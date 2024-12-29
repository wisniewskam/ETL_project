#modules
import mysql.connector
from mysql.connector import errorcode

try:
    con = mysql.connector.connect(read_default_file='path to .my.cnf')
    print('Connected to mysql database')
    con.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Wrong credentials')
    else:
        print(err)

