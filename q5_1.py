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
    SELECT
        mm.meal_name,
        COUNT(*) AS times_sold
    FROM order_item oi
    JOIN menu_meal mm ON oi.item_id = mm.meal_id
    WHERE oi.is_meal = 1
    GROUP BY mm.meal_id
    ORDER BY times_sold DESC;
    """)

    results = cursor.fetchall()
    for row in results:
        print(f"Meal: {row[0]}, Sold: {row[1]}")

    cursor.close()
    mydb.close()
