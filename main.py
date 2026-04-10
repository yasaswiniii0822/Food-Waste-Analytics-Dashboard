import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="food_waste_db",
    port=3306
)

cursor = conn.cursor()

def add_food():
    name = input("Food name: ")
    category = input("Category: ")

    cursor.execute(
        "INSERT INTO food_items (item_name, category) VALUES (%s, %s)",
        (name, category)
    )
    conn.commit()
    print("Food added!")


def add_preparation():
    item_id = int(input("Item ID: "))
    date = input("Date (YYYY-MM-DD): ")
    qty = float(input("Quantity prepared: "))

    cursor.execute(
        "INSERT INTO daily_preparation (item_id, date, quantity_prepared) VALUES (%s, %s, %s)",
        (item_id, date, qty)
    )
    conn.commit()
    print(" Preparation added!")


def add_consumption():
    item_id = int(input("Item ID: "))
    date = input("Date (YYYY-MM-DD): ")
    qty = float(input("Quantity consumed: "))

    cursor.execute(
        "INSERT INTO daily_consumption (item_id, date, quantity_consumed) VALUES (%s, %s, %s)",
        (item_id, date, qty)
    )
    conn.commit()
    print(" Consumption added (trigger executed)")


def show_waste():
    cursor.execute("SELECT * FROM waste_log")
    results = cursor.fetchall()

    print("\n--- Waste Log ---")
    for row in results:
        print(row)


def show_alerts():
    cursor.execute("SELECT * FROM alerts")
    results = cursor.fetchall()

    print("\n--- Alerts ---")
    for row in results:
        print(row)

def highest_waste_day():
    cursor.execute("""
        SELECT date, SUM(waste_quantity) AS total_waste
        FROM waste_log
        GROUP BY date
        ORDER BY total_waste DESC
        LIMIT 1
    """)
    print("\n Highest Waste Day:")
    for row in cursor.fetchall():
        print(row)


def most_wasted_item():
    cursor.execute("""
        SELECT f.item_name, SUM(w.waste_quantity) AS waste
        FROM waste_log w
        JOIN food_items f ON w.item_id = f.item_id
        GROUP BY f.item_name
        ORDER BY waste DESC
    """)
    print("\n Most Wasted Items:")
    for row in cursor.fetchall():
        print(row)

while True:
    print("\n===== FOOD WASTE SYSTEM =====")
    print("1. Add Food")
    print("2. Add Preparation")
    print("3. Add Consumption")
    print("4. View Waste Log")
    print("5. View Alerts")
    print("6. Highest Waste Day")
    print("7. Most Wasted Item")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_food()
    elif choice == "2":
        add_preparation()
    elif choice == "3":
        add_consumption()
    elif choice == "4":
        show_waste()
    elif choice == "5":
        show_alerts()
    elif choice == "6":
        highest_waste_day()
    elif choice == "7":
        most_wasted_item()
    elif choice == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice")