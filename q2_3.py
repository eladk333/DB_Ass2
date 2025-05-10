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
   CREATE TABLE meal_item (
    meal_id INT NOT NULL,
    item_id INT NOT NULL,
    FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id),
    FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
);

    """)
    
