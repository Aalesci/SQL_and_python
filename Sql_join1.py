import sqlite3

try: 
    Connection = sqlite3.connect("Ana.db")
    cursor = Connection.cursor()
    print('Connected!')

    create_table = "CREATE TABLE Ana (CF text, name text , surname text , age int)"
    cursor.execute(create_table) 
    
    insert_query =  """INSERT INTO Ana
                        (CF, name , surname, age)
                        VALUES
                        ('LSCLRT94A15G22T', 'Alberto', 'Alesci', '28') """ 

    cursor.execute(insert_query)
    Connection.commit()
    print('Commit ok!')
    cursor.close()

except sqlite3.Error as error:
    print('Problem with Insert',error) 



Connection = sqlite3.connect("Ana.db")
cursor = Connection.cursor()
print('Connected!')
select = "SELECT * FROM Ana "
selct_print = cursor.execute(select)
records = cursor.fetchall()
print('total number are ', len(records))
for row in records: 
    print("CF: ", row[0], "name: ", row[1] ,"Surname: ", row[2], "Age: ", row[3])
cursor.close()
print(selct_print)

