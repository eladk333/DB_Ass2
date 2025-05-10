import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE TABLE menu_item (
            item_id INT PRIMARY KEY,
            item_name VARCHAR(255) NOT NULL,
            price SMALLINT NOT NULL
                   );
    """)
  
