import psycopg2
import random
import time

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="iot_data", 
    user="postgres", 
    password="abc321", 
    host="localhost", 
    port="5432"
)
cursor = conn.cursor()

while True:
    # Generate random data points
    power_output = random.uniform(100, 150)  # Example: Power output in kW
    temperature = random.uniform(25, 40)    # Example: Temperature in °C

    # Insert data into the table
    cursor.execute(
        "INSERT INTO solar_data (power_output, temperature) VALUES (%s, %s)", 
        (power_output, temperature)
    )
    conn.commit()

    print(f"Inserted data: Power={power_output:.2f} kW, Temp={temperature:.2f} °C")
    time.sleep(20)  # Generate data every 20 seconds
