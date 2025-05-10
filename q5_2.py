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
      (
        SELECT COUNT(*) FROM order_item
        WHERE item_id = 6 AND is_meal = 1
      ) -
      (
        SELECT COUNT(DISTINCT oi1.order_id)
        FROM order_item oi1
        WHERE oi1.is_meal = 0
          AND NOT EXISTS (
            SELECT mi.item_id
            FROM meal_item mi
            WHERE mi.meal_id = 6
            EXCEPT
            SELECT oi2.item_id
            FROM order_item oi2
            WHERE oi2.order_id = oi1.order_id AND oi2.is_meal = 0
          )
      ) AS difference
    FROM menu_meal mm
    WHERE mm.meal_id = 6;
    """)

    result = cursor.fetchone()
    print(f"Meal: {result[0]}, Difference: {result[1]}")

    cursor.close()
    mydb.close()
