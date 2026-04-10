import streamlit as st
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",  
    user="root",
    password="",       
    database="food_waste_db"
)
cursor = conn.cursor()

st.title("🍽️ Food Waste Analytics Dashboard")


st.header("Add Food Item")
name = st.text_input("Food Name")
category = st.text_input("Category")

if st.button("Add Food"):
    cursor.execute(
        "INSERT INTO food_items (item_name, category) VALUES (%s, %s)",
        (name, category)
    )
    conn.commit()
    st.success("Food added successfully!")


st.header("Add Preparation")
item_id = st.number_input("Item ID (Preparation)", min_value=1)
date = st.date_input("Date (Preparation)")
prep_qty = st.number_input("Quantity Prepared", min_value=0.0)

if st.button("Add Preparation"):
    cursor.execute(
        "INSERT INTO daily_preparation (item_id, date, quantity_prepared) VALUES (%s, %s, %s)",
        (item_id, str(date), prep_qty)
    )
    conn.commit()
    st.success("Preparation added!")


st.header("Add Consumption")
item_id_c = st.number_input("Item ID (Consumption)", min_value=1, key="c")
date_c = st.date_input("Date (Consumption)", key="d")
cons_qty = st.number_input("Quantity Consumed", min_value=0.0, key="q")

if st.button("Add Consumption"):
    cursor.execute(
        "INSERT INTO daily_consumption (item_id, date, quantity_consumed) VALUES (%s, %s, %s)",
        (item_id_c, str(date_c), cons_qty)
    )
    conn.commit()
    st.success("Consumption added! 🔥 Trigger executed")

# ---------------- WASTE LOG ----------------
st.header("Waste Log")
if st.button("Show Waste Log"):
    cursor.execute("SELECT * FROM waste_log")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Item ID", "Date", "Waste"])
    st.dataframe(df)


st.header("Alerts")
if st.button("Show Alerts"):
    cursor.execute("SELECT * FROM alerts")
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Item ID", "Date", "Message"])
    st.dataframe(df)


st.header("Analytics")

if st.button("Highest Waste Day"):
    cursor.execute("""
        SELECT date, SUM(waste_quantity) AS total_waste
        FROM waste_log
        GROUP BY date
        ORDER BY total_waste DESC
        LIMIT 1
    """)
    st.write(cursor.fetchall())

if st.button("Most Wasted Items"):
    cursor.execute("""
        SELECT f.item_name, SUM(w.waste_quantity) AS waste
        FROM waste_log w
        JOIN food_items f ON w.item_id = f.item_id
        GROUP BY f.item_name
        ORDER BY waste DESC
    """)
    st.write(cursor.fetchall())