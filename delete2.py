
import pyodbc

def delete_all(server, database):
    
    print('What table data Do you want to delete all? ')
    print("1. Product")
    print("2. Customer")
    print("3. Supplier")
    
    choice = int(input('> '))
    
    if choice == 1:
        conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        Cursor = conn.cursor()
        
        Cursor.execute('drop table Product;')
        conn.commit()
        print('Table has been dropped from database.')
        Cursor.close()
        conn.close()
        
    elif choice == 2:
        conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        Cursor = conn.cursor()
        
        Cursor.execute('drop table Customer;')
        conn.commit()
        print('Table has been dropped from database.')
        Cursor.close()
        conn.close()
    
    elif choice == 3:
        conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_string)
        Cursor = conn.cursor()
        
        Cursor.execute('drop table Supplier;')
        conn.commit()
        print('Table has been dropped from database.')
        Cursor.close()
        conn.close()