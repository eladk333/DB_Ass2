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
        c.city_name,
        SUM(CASE WHEN mm.served_at = 'morning' THEN 1 ELSE 0 END) AS breakfast_count,
        SUM(CASE WHEN mm.served_at = 'all day' THEN 1 ELSE 0 END) AS regular_count
    FROM city c
    JOIN street s ON s.in_city = c.city_id
    JOIN address a ON a.in_street = s.street_id
    JOIN client cl ON cl.client_address = a.address_id
    JOIN full_order fo ON fo.by_client = cl.client_id
    JOIN order_item oi ON oi.order_id = fo.order_id
    JOIN meal_item mi ON mi.meal_id = oi.item_id
    JOIN menu_meal mm ON mm.meal_id = mi.meal_id
    WHERE oi.is_meal = 1
    GROUP BY c.city_name
    ORDER BY c.city_name ASC;
    """)

  
    results = cursor.fetchall()
    for row in results:
        print(f"City: {row[0]}, Breakfasts: {row[1]}, Regular Meals: {row[2]}")

    cursor.close()
    mydb.close()
