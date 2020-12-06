import os
import pymysql

def crud_to_mysql(user: str, password: str, database: str, host: str, ssl: str):
    conn = pymysql.connect(
        user=user,
        password=password,
        database=database,
        host=host,
        ssl={'ca': ssl_ca}
        )
        
    try:
        # prepare a cursor object using cursor() method
        with conn.cursor() as cur:
            # execute SQL query using execute() method.
            cur.execute("SELECT VERSION()")
            # Fetch a single row using fetchone() method.
            data = cur.fetchone()
            print ("Database version : %s " % data)

            # Creating database table
            cur.execute("DROP TABLE IF EXISTS GENERAL_PRACTITIONER")
            sql_table = """ CREATE TABLE GENERAL_PRACTITIONER (
                FIRST_NAME  CHAR(20) NOT NULL,
                LAST_NAME  CHAR(20),
                AGE INT,  
                SEX CHAR(1),
                INCOME FLOAT)
                """
            cur.execute(sql_table)
            
            # Creating an INSERT
            
            sql_insert = """INSERT INTO GENERAL_PRACTITIONER(FIRST_NAME,
                            LAST_NAME, AGE, SEX, INCOME)
                            VALUES ('Bernardo', 'Garcia', 36, 'M', 2000)
                        """
            cur.execute(sql_insert)
            conn.commit()

            sql_read = "SELECT * FROM GENERAL_PRACTITIONER \
                    WHERE INCOME > '%d'" % (1000)
                    
            try:
                cur.execute(sql_read)
                # conn.commit()
                results = cur.fetchall()
                for row in results:
                    fname = row[0]
                    lname = row[1]
                    age = row[2]
                    sex = row[3]
                    income = row[4]
                        
                    # Printing the results
                    print ("fname = %s,lname = %s,age = %d,sex = %s,income = %d" % \
                        (fname, lname, age, sex, income))
            except:
                print ("Error: unable to fetch data")
            sql_update = "UPDATE GENERAL_PRACTITIONER SET INCOME = INCOME + 3 \
                          WHERE FIRST_NAME = '%f'" % ('Bernardo')
            try:
                cur.execute(sql_update)
                conn.commit()
            except:
               # Rollback in case there is any error
                conn.rollback() 
    except:
        # Rollback in case there is any error
         conn.rollback()
    finally:
        # disconnect from server
        conn.close()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
database = os.environ['MYSQL_DATABASE']
host = os.environ['MYSQL_HOST']
ssl_ca = os.environ['MYSQL_SSL_CA']

crud_to_mysql(user, password, database, host, ssl_ca)