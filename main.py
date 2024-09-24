import inventoryManagementBackend as imb
import delete
# server = '<your-server-name>'
# database = '<database-name>'
def inventoryManageSystem(server,database):
    # server = 'LAPTOP-UMGS7KJ4'
    # database = 'InventoryManagementSystem'
    print("\t\t\t\t\t\t\t********************************************")
    print('\t\t\t\t\t\t\t\tInventory Management System')
    print("\t\t\t\t\t\t\t********************************************")

    print('\n')
    print('''
        1. Add
        2. Update
        3. Delete
        4. Show Stock
        5. Delete all data from table
        6. Current Stock
        7. Exit
        ''')


    choice = int(input('What task do you want to perform? '))
    
    try:
        
        if choice == 1:
            imb.Add(server, database)
        elif choice == 2:
            imb.Update(server, database)
        elif choice == 3:
            imb.Delete(server, database)
        elif choice == 4:
            imb.show_stock(server, database)
        elif choice == 5:
            delete.delete_all(server, database)
        elif choice == 6:
            imb.current_stock(server, database)
        else:
            exit()
        
    except Exception as e:
        print('Error :',e)

       
print('< Login Database >')
server = input('Server : ')
database = input('Database : ')

inventoryManageSystem(server,database)

while True:
    run_again = input('\nDo you want to perform another task? (yes/no) : ').lower()
    if run_again == 'yes' or run_again == 'y':
        inventoryManageSystem(server,database)
    else:
        exit()