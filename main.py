import psycopg2

DB_HOST = 'localhost'
DB_NAME = 'test_python'
DB_USER = 'postgres'
DB_PASS = 'admin'
PORT = 5432
connect = None
cur = None

if __name__ == '__main__':

    try:
        connect = psycopg2.connect(
            host = DB_HOST,
            dbname = DB_NAME,
            user = DB_USER,
            password = DB_PASS,
            port = PORT
        )
        # Open a SQL transaction with a cursor 
        cur = connect.cursor()

        # Create a table
        create_employee_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                        id      int PRIMARY KEY,
                                        name    varchar(50) NOT NULL,
                                        salary  int,
                                        dept_id varchar(30))'''
        
        cur.execute(create_employee_script)

        # Insert data into a table
        insert_employee_script = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
        insert_value = (1, 'Mike', 14500, '69')
        cur.execute(insert_employee_script, insert_value)

        # Commit modifications into the table
        connect.commit()

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if connect is not None : 
            connect.close()