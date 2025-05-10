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
    UPDATE menu_meal
    SET raw_cost = (
        SELECT SUM(mi2.price)
        FROM meal_item mi
        JOIN menu_item mi2 ON mi.item_id = mi2.item_id
        WHERE mi.meal_id = 3
    )
    WHERE meal_id = 3;
    """)

    mydb.commit()
   
    cursor.close()
    mydb.close()
