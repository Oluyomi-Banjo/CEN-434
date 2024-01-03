from crud import *

my_db = conn.connect(
    host = 'localhost',
    user = 'root',
    password = 'jesus4life'
)

# print(my_db)

my_cursor = my_db.cursor()

print('############### Welcome ###############')
db_name = input('Enter your desired db name: ')
task = input('What would you like to do?: \n 1. Create Database \n 2. Create Table \n 3. Add data to the table \n 4. Read data \n 5. Update a record \n 6. Delete a record \n 7. Delete a table \n Answer here: ')

if int(task) == 1:
    db_name = input('Enter the name of the database: ')

    create_database(my_cursor=my_cursor, db_name=db_name)


elif int(task) == 2:
    table_name = input('Enter the table name: ')
    column1 = input('Enter the first column: ')
    column2 = input('Enter the second column: ')

    my_cursor.execute(f'USE {db_name}')
    
    create_table(my_cursor=my_cursor, table_name=table_name, column1=column1, column2=column2)

elif int(task) == 3:
    table_name = input('Enter the table name: ')

    column1 = input('Enter the first column: ')
    value1 = input('Enter the value of the first column: ')

    column2 = input('Enter the second column: ')
    value2 = input('Enter the value of the second column: ')

    my_cursor.execute(f'USE {db_name}')
    
    add_data(my_db=my_db, my_cursor=my_cursor, table_name=table_name, column1=column1, column2=column2, value1=value1, value2=value2)

elif int(task) == 4:
    table_name = input('Enter the table name: ')
    column1 = input('Enter the first column: ')
    column2 = input('Enter the second column: ')

    my_cursor.execute(f'USE {db_name}')

    read_data(my_cursor=my_cursor, table_name=table_name, column1=column1, column2=column2)

elif int(task) == 5:
    table_name = input('Enter the table name: ')
    column = input('Enter the column name: ')

    initial_data = input('Enter the initial data: ')
    new_data = input('Enter the new data: ')

    my_cursor.execute(f'USE {db_name}')

    update_data(my_db=my_db, my_cursor=my_cursor, table_name=table_name, column=column, initial_data=initial_data, new_data=new_data)

elif int(task) == 6:
    table_name = input('Enter the table name: ')
    column = input('Enter the column: ')
    data = input('Enter the data row you wish to delete: ')

    my_cursor.execute(f'USE {db_name}')

    delete_data(my_db=my_db, my_cursor=my_cursor, table_name=table_name, column=column, data=data)

elif int(task) == 7:
    table_name = input('Enter the table name: ')

    my_cursor.execute(f'USE {db_name}')

    delete_table(my_db=my_db, my_cursor=my_cursor, table_name=table_name)
