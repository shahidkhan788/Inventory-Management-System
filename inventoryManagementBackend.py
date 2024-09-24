import pandas as pd
import pyodbc

# server = 'LAPTOP-UMGS7KJ4'
# database = 'inventoryManagementSystem'
    
    
def Add(server,database):
    conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    print('In which table do you add data? ')
    print("1. Product")
    print("2. Customer")
    print("3. Supplier")
    
    choice = int(input('> '))
    if choice == 1:
        try:
            cursor.execute('''
                                CREATE TABLE Product
                                (
                                    ProductCode INT PRIMARY KEY,
                                    ProductName VARCHAR(255),
                                    Quantity INT,
                                    Price DECIMAL(10,2),
                                    SupplierID INT,
                                    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
                                );
                            ''')
        except Exception as e:
            pass
        sql_query = 'insert into Product (ProductCode,ProductName,Quantity,Price,SupplierID) values(?,?,?,?,?)'
        n = int(input('How many data do you want to add in it? '))
        for i in range(n):
            print(f'< The {i+1} record information >')
            product_code = int(input("Product Code : "))
            product_name = input("Product Name : ")
            quantity = int(input("Quantity : "))
            price = float(input('Price : '))
            supplierID = int(input('SupplierID : '))         
            cursor.execute(sql_query,(product_code,product_name,quantity,price,supplierID))
        conn.commit()
        print('Data inserted successfully.')
        cursor.close()
        conn.close()

    elif choice == 2:
        try:
            cursor.execute('''
                                CREATE TABLE Customer
                                (
                                    CustomerID INT PRIMARY KEY,
                                    CustomerName VARCHAR(255),
                                    ProductName VARCHAR(255),
                                    Quantity INT,
                                    Price DECIMAL(10,2),
                                    Address TEXT,
                                    ProductCode INT,
                                    FOREIGN key (ProductCode) REFERENCES Product(ProductCode)
                                );
                            ''')
        except Exception as e:
            pass
        sql_query = "insert into Customer (CustomerID, CustomerName, ProductName, Quantity, Price, Address,ProductCode) values (?,?,?,?,?,?,?)"
        n = int(input("How many records do you want to insert in this table? "))
        for i in range(n):
            print(f'"Enter information as per table records {i+1}"')
            customerID = int(input("Customer ID : "))
            customerName = input("What's your name? ")
            productName = input('ProductName : ')
            quantity = int(input('Quantity : '))
            price = float(input('Price : '))
            address = input("Address : ")
            productCode = int(input('ProductCode : '))
            cursor.execute(sql_query,(customerID,customerName,productName,quantity,price,address,productCode))
        conn.commit()
        print('Data inserted successfully.')
        cursor.close()
        conn.close()

        
    elif choice == 3:
        try:
            cursor.execute('''
                                CREATE TABLE Supplier
                                (
                                    SupplierID INT PRIMARY KEY,
                                    SupplierName VARCHAR(255),
                                    Address VARCHAR(500),
                                    Contact BIGINT,
                                    ProductName VARCHAR(255),
                                    Quantity INT,
                                    Price DECIMAL(10,2)
                                );
                            ''')
        except Exception as e:
            pass
        sql_query = "insert into Supplier (SupplierID, SupplierName, Address, Contact, ProductName, Quantity, Price) values (?,?,?,?,?,?,?)"
        n = int(input("How many records do you want to insert in this table? "))
        for i in range(n):
            print(f'"Enter information as per table records {i+1}"')
            supplierID = int(input('Supplier ID : '))
            supplierName = input('Supplier Name : ')
            address = input('Address : ')
            contact = int(input('Contact : '))
            productName = input('Product Name : ')
            quantity = int(input('Quantity : '))
            price = float(input('Price : '))
            cursor.execute(sql_query,(supplierID,supplierName,address,contact,productName,quantity,price))
        
        conn.commit()
        print('Data inserted successfully.')
        cursor.close()
        conn.close()
        
    else:
        print('choice was wrong!')
        
def Update(server,database):
    conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    print('What table data do you want to update? ')
    print("1. Product")
    print("2. Customer")
    print("3. Supplier")
    
    choice = int(input('> '))
    if choice == 1:
        column_name = input('What column data do you want to update? ')
        value = input('Enter the value to be inserted : ')
        productCode = int(input('Enter the product code of this record : '))
        cursor.execute(f'update product set {column_name} = {value} where ProductCode = {productCode};' )
        conn.commit()
        print('Data updated successfully.')
        cursor.close()
        conn.close()
        
    elif choice == 2:
        column_name = input('What column data do you want to update? ')
        value = input('Enter the value to be inserted : ')
        customerID = int(input('Enter the CustomerID of this record : '))
        cursor.execute(f'update product set {column_name} = {value} where ProductCode = {customerID};' )
        conn.commit()
        print('Data updated successfully.')
        cursor.close()
        conn.close()
        
    elif choice == 3:
        column_name = input('What column data do you want to update? ')
        value = input('Enter the value to be inserted : ')
        supplierID = int(input('Enter the SupplierID of this record : '))
        cursor.execute(f'update supplier set {column_name} = {value} where ProductCode = {supplierID};' )
        conn.commit()
        print('Data updated successfully.')
        cursor.close()
        conn.close()

    else:
        print('Wrong choice.!')

def Delete(server,database):
    conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    print('What table data do you want to delete? ')
    print("1. Product")
    print("2. Customer")
    print("3. Supplier")
    
    choice = int(input('> '))
    
    if choice == 1:
        productCode = int(input('Enter the product code of this record : '))
        cursor.execute(f'delete product where ProductCode = {productCode};' )
        conn.commit()
        print('Data deleted successfully.')
        cursor.close()
        conn.close()
        
    elif choice == 2:
        customerID = int(input('Enter the CustomerID of this record : '))
        cursor.execute(f'delete customer where CustomerID = {customerID};')
        conn.commit()
        print('Data deleted successfully.')
        cursor.close()
        conn.close()
        
    elif choice == 3:
        supplierID = int(input('Enter the SupplierID of this record : '))
        cursor.execute(f'delete supplier where SupplierID = {supplierID};' )
        conn.commit()
        print('Data deleted successfully.')
        cursor.close()
        conn.close()
    
    else:
        print('Wrong choice..!')

def show_stock(server, database):
    
    conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_string)
    
    print('What table data do you want to show? ')
    print("1. Product")
    print("2. Customer")
    print("3. Supplier")

    choice = int(input('> '))
    
    if choice == 1:
        data = pd.read_sql_query('select * from Product;',conn)
        df = pd.DataFrame(data)
        print(df)
        save = input('Do you want save it? (yes/no) : ').lower()
        if save == 'yes' or save == 'y':
            df.to_csv('Data.csv',index=False)
            
    elif choice == 2:
        data = pd.read_sql_query('Select * from Customer;',conn)
        df = pd.DataFrame(data)
        print(df)
        save = input('Do you want save it? (yes/no) : ').lower()
        if save == 'yes' or save == 'y':
            df.to_csv('Data.csv',index=False)
    
    elif choice == 3:
        data = pd.read_sql_query('select * from Supplier;',conn)
        df = pd.DataFrame(data)
        print(df)
        save = input('Do you want save it? (yes/no) : ').lower()
        if save == 'yes' or save == 'y':
            df.to_csv('Data.csv',index=False)


def current_stock(server, database):
    
    conn_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()
    
    print('What product data do you want to see?')
    productCode = int(input('Product Code : '))
    
    print('1. Warehouse Stock\n2. Current Stock')
    choice = int(input('>'))
    if choice == 1:
        try:
            data = pd.read_sql_query('''
                           select p.ProductCode,s.ProductName,(s.Quantity - p.Quantity) as WarehouseStock from Supplier as s
                           left join Product as p
                           on s.SupplierID = p.SupplierID;
                           ''',conn)
            df = pd.DataFrame(data)
            print(df)
            save_data = input('Do you want to save it? (yes/no) : ').lower()
            if save_data == 'yes' or save_data == 'y':
                df.to_csv('Data.csv', index=False)
                
        except Exception as e:
            print(f'Error : {e}')
            
    elif choice == 2:
        try:
            # Update the stock quantity based on sales data using a parameterized query
            cursor.execute('''
                UPDATE Product
                SET Quantity = Quantity - (
                    SELECT SUM(Quantity) AS SoldOutProduct
                    FROM Customer
                    WHERE ProductName IN (
                        SELECT ProductName
                        FROM Product
                        WHERE ProductCode = ?
                    )
                    GROUP BY ProductName
                )
                WHERE ProductCode = ?;
            ''', (productCode, productCode))

            # Retrieve the updated product information using a parameterized query
            
            
            data = pd.read_sql_query(f'Select ProductName, Quantity as CurrentStock from product Where productCode = {productCode};',conn)
            df = pd.DataFrame(data)
            print(df)
            
            save_data = input('Do you want to save it? (yes/no) : ').lower()
            if save_data == 'yes' or save_data == 'y':
                df.to_csv('Data.csv', index=False)
                
        except Exception as e:
            print(f'Error : {e}')
    else:
        print('Invalid input!')


            

