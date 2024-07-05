import mysql.connector

# Replace with your actual database credentials and IP address
host = ""
user = ""
password = ""
dbName = ""

config = {
    "user": user,
    "password": password,
    "host": host,
    "database": dbName,
}

try:
    conn = mysql.connector.connect(**config)
    if conn.is_connected():
        print("Connected to MySQL database")
    else:
        print("Connection failed")

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    if "conn" in locals() and conn.is_connected():
        conn.close()
        print("MySQL connection closed")
