import mysql.connector

def connect_to_database():
    try:
        # Establish a connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='prospa',
            database='prospa'
        )

        if connection.is_connected():
            print("Successfully connected to the database")

            # Create a cursor object
            cursor = connection.cursor()

            # Execute a query to retrieve data from the Employees table
            cursor.execute("SELECT * FROM Employees")

            # Fetch all results
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Database connection closed.")

# Call the function to connect and retrieve data
if __name__ == "__main__":
    connect_to_database()
