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
    SELECT mm.meal_name
    FROM menu_meal mm
    JOIN meal_item mi ON mm.meal_id = mi.meal_id
    JOIN menu_item i ON mi.item_id = i.item_id
    GROUP BY mm.meal_id, mm.meal_name, mm.price
    HAVING mm.price >= SUM(i.price);
    """)

    results = cursor.fetchall()
    print("Meals that are NOT cheaper than their items:")
    for row in results:
        print("-", row[0])

    cursor.close()
    mydb.close()
