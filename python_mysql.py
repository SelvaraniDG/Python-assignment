import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def fetch_records_in_batches(cursor, batch_size=10):
    while True:
        records = cursor.fetchmany(batch_size)
        if not records:
            break
        yield records


def main():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    cursor = connection.cursor()

    select_query = "SELECT * FROM employees"
    cursor.execute(select_query)

    print("==============================================================================================================")
    print("Records before changes:")
    print("==============================================================================================================")
    for batch in fetch_records_in_batches(cursor):
        for record in batch:
            print(record)

    # #INSERT DATA
    # insert_query = "INSERT INTO `db`.`employees` (`emp_no`, `birth_date`, `first_name`, `last_name`, `gender`, `hire_date`) VALUES ('251', '2086-04-04', 'Jessy', 'joy', 'F', '2027-11-04')"        
    # cursor.execute(insert_query)

    # UPDATE DATA
    # update_query = "UPDATE employees SET first_name = 'Jane' WHERE emp_no = 101"
    # cursor.execute(update_query)

    # # DELETE DATA
    # delete_query = "DELETE FROM employees WHERE emp_no = 98"
    # cursor.execute(delete_query)

    # DROP TABLE
    # drop_query = "DROP TABLE IF EXISTS employees"
    # cursor.execute(drop_query)

    connection.commit()

    cursor.execute(select_query)

    # Display records after changes
    print("==============================================================================================================")
    print("Records after changes:")
    print("==============================================================================================================")
    for batch in fetch_records_in_batches(cursor):
        for record in batch:
            print(record)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
