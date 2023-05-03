import pyodbc as odbc

driver = "{ODBC Driver 17 for SQL Server}"
server = "localhost\\MYSQLEXPRESS"
database = "FCE_DB"
username = "sa"
password = "test"


def dbconnect(driver, server, database,username,password):
    conn = odbc.connect("DRIVER"+ driver 
                                     + ";SERVER" + server
                                     + ";DATABASE" + database
                                     + ";UID" + username
                                     + ";PWD" + password
                                      )


    
    return conn

conn = dbconnect(driver, server, database,username, password)
print(conn)

query = "select BookId, Title, Author, Category from BOOK where Category = ?"

parameters = ['Fiction'] #Parameter

cursor = conn.cursor(query,parameters)

for row in cursor.execute():
    print(row.BookId, row.Title, row.Author, row.Category)
    
