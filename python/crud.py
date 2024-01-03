import mysql.connector as ctor


# my_db = ctor.connect(
#     host = 'localhost',
#     user = 'root',
#     password = 'Mockingbird11@'
# )

# # print(my_db)

# my_cursor = my_db.cursor()

# Create a database
def create_database(db_name: str, my_cursor):
  my_cursor.execute(f'CREATE DATABASE {db_name}')
  my_cursor.execute(f'USE {db_name}')

  return 'Done!'

# Create table
def create_table(my_cursor, table_name: str, column1: str, column2: str):
  my_cursor.execute(f"CREATE TABLE {table_name} ({column1} VARCHAR(255), {column2} VARCHAR(255))")

  return 'Done!'

# Add data

def add_data(my_db, my_cursor, table_name: str, column1: str, column2: str, value1: str, value2: str):
  sql = f"INSERT INTO {table_name} ({column1}, {column2}) VALUES (%s, %s)"
  val = (value1, value2)
  my_cursor.execute(sql, val)
  
  my_db.commit()

  return f'Rows: {my_cursor.rowcount}, record inserted.'


# Read data
def read_data(my_cursor, table_name: str, column1: str, column2: str):
    my_cursor.execute(f"SELECT {column1}, {column2} FROM {table_name}")

    myresult = my_cursor.fetchall()

    for x in myresult:
        print(x)

# Update data
def update_data(my_db, my_cursor, table_name: str, column: str, initial_data: str, new_data: str):
    sql = f"UPDATE {table_name} SET {column} = {initial_data} WHERE {column} = {new_data}"

    my_cursor.execute(sql)

    my_db.commit()

    return f'Rows: {my_cursor.rowcount}, "record(s) affected"'

# Delete data
def delete_data(my_db, my_cursor, table_name: str, column: str, data: str):
    '''
    Delete data from whose primary key is data from column
    '''
    sql = f"DELETE FROM {table_name} WHERE {column} = {data}"

    my_cursor.execute(sql)

    my_db.commit()

    return f'Rows: {my_cursor.rowcount}, "record(s) deleted"'

# Delete table
def delete_table(my_db, my_cursor, table_name: str):
    sql = f"DROP TABLE {table_name}"

    my_cursor.execute(sql)

# Delete database
def delete_database(my_cursor, db_name: str):
    sql = f"DROP DATABASE {db_name}"

    my_cursor.execute(sql)


# close connection

# my_db.close()
