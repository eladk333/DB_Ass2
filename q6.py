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

    # Add raw_cost column to menu_meal table
    cursor.execute("""
    ALTER TABLE menu_meal
    ADD COLUMN raw_cost INT;
    """)

    mydb.commit()
   

    cursor.close()
    mydb.close()
 