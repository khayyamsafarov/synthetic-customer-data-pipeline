import mysql.connector
from faker import Faker
import random
import time

fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="your database password",
    database="pproject"
)

cursor = conn.cursor()
print("Successfully connected to Mysql!")

genders = ["Male", "Female", "Other"]
regions = ["North America", "South America", "Europe", "Asia", "Africa", "Middle East", "Oceania"]
countries = [
    "United States", "United Kingdom", "Germany", "France", "Japan",
    "Brazil", "Canada", "Australia", "India", "China",
    "Mexico", "Italy", "Spain", "South Korea", "Netherlands",
    "Turkey", "Saudi Arabia", "Argentina", "South Africa", "Sweden"
]


# insert into function

def insert_record(row_num):
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randint(18, 70)
    gender = random.choice(genders)
    region = random.choice(regions)
    country = random.choice(countries)

    query = """
    insert into customers(first_name, last_name, age, gender, region, country)
    values (%s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (first_name, last_name, age, gender, region, country))
    conn.commit()
    print(
        f"[{row_num}/100] Successfully added: {first_name} {last_name} | Age: {age} | Gender: {gender} | {region} | {country}")


print("\n Starting data generation...\n")

for i in range(1, 101):
    insert_record(i)

    if i == 100:
        print("\n 100 rows added! script ")
        break

    wait = random.randint(10, 30)
    print(f" Next record in {wait} seconds...\n")
    time.sleep(wait)

cursor.close()
conn.close()
print("Database connection closed.")
print("Ready to connect to MySql to Excel!")










