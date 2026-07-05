import mysql.connector
import random
import time
import datetime

# --- CONFIG ---
WAIT_MIN = 5
WAIT_MAX = 25

# --- CONNECT TO MYSQL ---
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="your database password",
    database="pproject"
)
cursor = conn.cursor()
print("✅ Connected to MySQL!")

# --- REAL SHIPPING COMPANIES ---
partners_data = [
    ("DHL Express",        "Germany",        "Europe"),
    ("FedEx",              "United States",  "North America"),
    ("UPS",                "United States",  "North America"),
    ("Aramex",             "Jordan",         "Middle East"),
    ("TNT Express",        "Netherlands",    "Europe"),
    ("Japan Post",         "Japan",          "Asia"),
    ("Australia Post",     "Australia",      "Oceania"),
    ("Correios",           "Brazil",         "South America"),
    ("South African Post", "South Africa",   "Africa"),
    ("Canada Post",        "Canada",         "North America"),
    ("Royal Mail",         "United Kingdom", "Europe"),
    ("China Post",         "China",          "Asia"),
    ("India Post",         "India",          "Asia"),
    ("Turkish Cargo",      "Turkey",         "Middle East"),
    ("MRW",                "Spain",          "Europe"),
    ("Chronopost",         "France",         "Europe"),
    ("Fastway",            "Ireland",        "Europe"),
    ("Blue Dart",          "India",          "Asia"),
    ("Sendle",             "Australia",      "Oceania"),
    ("Shiprocket",         "India",          "Asia"),
]

# --- INSERT DAILY STATS FOR ALL PARTNERS ---
def insert_daily_stats():
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(f"\n📦 Inserting daily partner stats for {today}...\n")

    for i, (name, country, region) in enumerate(partners_data, 1):
        shipments = random.randint(100, 500)
        avg_days  = round(random.uniform(1.5, 7.0), 1)
        cost      = round(random.uniform(5.0, 25.0), 2)
        status    = random.choices(["Active", "Inactive"], weights=[90, 10])[0]
        rating    = round(random.uniform(3.0, 5.0), 1)

        # Parameterized query - prevents SQL injection
        query = """
            INSERT INTO partners
            (partner_name, country, region, shipments_count,
             average_delivery_days, cost_per_shipment, 
             status, rating, contract_start)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            name, country, region,
            shipments, avg_days, cost,
            status, rating, today
        ))
        conn.commit()

        print(f"[{i}/{len(partners_data)}] ✅ {name}")
        print(f"     Region: {region} | Country: {country}")
        print(f"     📦 Shipments: {shipments} | ⭐ Rating: {rating}")
        print(f"     🚚 Avg Days: {avg_days} | 💰 Cost: ${cost} | Status: {status}")

        if i < len(partners_data):
            wait = random.randint(WAIT_MIN, WAIT_MAX)
            print(f"⏳ Next partner in {wait} seconds...\n")
            time.sleep(wait)

    print(f"\n🎉 All {len(partners_data)} partners inserted for {today}!")

# --- MAIN ---
print("\n🚀 VMX Store Partner Management System Started!")
print(f"⏰ Date: {datetime.date.today()}")
print(f"⏱️  Interval: {WAIT_MIN}-{WAIT_MAX} seconds between each insert\n")

insert_daily_stats()

print("\n🔒 Closing connection...")
cursor.close()
conn.close()
print("✅ All done! Run again tomorrow for next day's stats.")