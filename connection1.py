import pyodbc as odbc

driver_name = 'SQL SERVER'
server_name = 'LAPTOP-TEST'
database = 'Test'


def dbconnect(driver_name, server_name, database):
    connection_string = f"""
    DRIVER ={{{driver_name}}};
    SERVER = {server_name};
    database = {database};
    Trust_Connection = yes;
"""
    
    return connection_string

connection_string = dbconnect(driver_name, server_name, database)

conn = odbc.connect(connection_string)
print(conn)