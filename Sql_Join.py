import sqlite3

def creation(): 
    try: 
        Connection = sqlite3.connect("My_db.db")
        cursor = Connection.cursor()
        print('Connected My_db.db !')
        create_table1 = "CREATE TABLE Anagrafica (CF text, name text , surname text , age int)"
        cursor.execute(create_table1) 
        Connection.commit()
        print('Commit Anagrafica ok!')
        cursor.close()
        
        Connection = sqlite3.connect("My_db.db")
        cursor = Connection.cursor()
        print('Connected My_db.db !')
        create_table2 = "CREATE TABLE Transactions (CF text, key2 text, importo text , data text , time text)"
        cursor.execute(create_table2) 
        Connection.commit()
        print('Commit Transaction ok!')
        cursor.close()

    except sqlite3.Error as error:
        print('Error in creation',error) 


def insert_anagrafica(task):
    try: 
        Connection = sqlite3.connect("My_db.db")
        cursor = Connection.cursor()
        print('Connected to My_db !')
        insert_query= ''' INSERT INTO Anagrafica (CF, name , surname, age)
                       VALUES(?,?,?,?) '''
        cursor.execute(insert_query, task)
        Connection.commit()
        print('Commit ok!')
        cursor.close()

    except sqlite3.Error as error: 
        print('Error in insertion: ')   



def show(nome_tab): 
    Connection = sqlite3.connect("My_db.db")
    cursor = Connection.cursor()
    print('Connected!')
    select = "SELECT * FROM " + nome_tab
    cursor.execute(select)  
    records = cursor.fetchall()
    print('Total number are ', len(records)) 

    for i in range(0,len(records)):
        print(records[i])
    cursor.close()


def insert_trans(task):
    try: 
        Connection = sqlite3.connect("My_db.db")
        cursor = Connection.cursor()
        print('Connected to My_db !')
        insert_query2= ''' INSERT INTO Transactions (CF , key2 , importo , data , time )
                          VALUES(?,?,?,?,?) '''
        cursor.execute(insert_query2, task)
        Connection.commit()
        print('Commit ok!')
        cursor.close()

    except sqlite3.Error as error: 
        print('Error in insertion: ')  



def join_and_show(tab1, tab2, join): 
    try: 
        Connection = sqlite3.connect("My_db.db")
        cursor = Connection.cursor()
        print('Connected to My_db for JOIN!')
        join_query = " SELECT  * FROM " + tab1 + " INNER JOIN " + tab2 + " on " + tab2 +"."+ join + " = " + tab1 +"."+ join 
        cursor.execute(join_query)
        records = cursor.fetchall()
        for i in range(0,len(records)):
            print(records[i])
        cursor.close()
        return records

    except sqlite3.Error as error: 
        print('Error in insertion: ')  



#Creo i record che poi inserirò nelle mie tabelle.
#Nella tabella transazioni inserisco volontariamnete un record doppio. 

#CF, nome , cognome , età. 
Matrix_Ana = [['LSCLRT90A15G22TJ', 'Alberto', 'Alesci', '28'],
              ['DRGMRA80A10G224Z','Mario', 'Draghi', '74'],
              ['PWLJRM77E16G224Z', 'JEROME', 'POWELL' , '69']]

#CF , key2 , importo , data , tempo . 
Matrix_trans = [['DRGMRA80A10G224Z', '1659857897.0', '10', '07.08.2022', '09:38:17' ], 
                ['DRGMRA80A10G224Z', '1659857897.0', '10', '07.08.2022', '09:38:17' ],
                ['DRGMRA80A10G224Z', '1659861621.0', '15', '07.08.2022', '10:40:21' ],
                ['LSCLRT90A15G22TJ', '1659865821.0', '9' , '07.08.2022', '11:50:21' ],
                ['PWLJRM77E16G224Z', '1659867051.0', '16', '07.08.2022', '12:10:51' ], 
                ]


#Nota per creare la seconda chiave >> key2 << nella seconda tabella ho convertito
#data e ora in timestamps secondo la seguente funzione. in modo da avere una chiave univoca. 
#import time
#print(time.mktime(time.strptime("07.08.2022 12:10:51", "%d.%m.%Y %H:%M:%S")))
# in questo modo ho due campi (CF e Timestamp) che mi identificano 
# univocamnete un singolo record nella join. 


# Creo le tabelle 
# Nota se il programma viene eseguito più volte senza cancellare My_db.db 
# Allora la funzione creation() cade nell' exception. Non puo' creare una
# tabella che già esiste. 
creation()

# Inserisco i dati in Anagrafica è transaction 
for i in range(0,len(Matrix_Ana)):          
    insert_anagrafica( Matrix_Ana[i])

for i in range(0,len(Matrix_trans)):
    insert_trans(Matrix_trans[i])

#Mostro i dati di Anagrafica è transaction 
show('Anagrafica')
show('Transactions')

matrix_list_join = join_and_show('Anagrafica','Transactions','CF') 

# Abbiamo una matrice di liste con tutti i dati necessari per controllare se ci sono 
# due righe uguali. Controlliamo per chiave quindi per CF e key2 che insieme formano 
# la chiave primaria della nostra tabella.  

cont = 0
for i in range(0,len(matrix_list_join)):
    if cont == 2: break 
    cont = 0
    for s in range(0,len(matrix_list_join)):
        if matrix_list_join[i][4] == matrix_list_join[s][4] and matrix_list_join[i][5] == matrix_list_join[s][5]: 
           cont = cont + 1 
        if cont >= 2: 
            print('La riga', s+1 ,'é un duplicato della riga ', i+1, '!' )
            break 
        
#Appena viene trovata una riga doppia il controllo si interrompe e riporta il numero delle righe. 

# Programma creato da Alberto Alesci per CherryBank in data 7/8/2022.          
    






