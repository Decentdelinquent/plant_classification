import sqlite3
from datetime import date

# Path to your SQLite database
database_path = "C:/Users/Sky/OneDrive - University of Jeddah/Desktop/FINAL/bloom_app.db"

try:
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path, check_same_thread=False)
    cursor = conn.cursor()

    # Enable foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON;")

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        profile_picture BLOB,
        bio TEXT
    );
    """)
    #plant info for the camera  
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PlantInformation (
        plant_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plant_name TEXT NOT NULL,
        scientific_name TEXT,
        care_instructions TEXT,
        sunlight_requirements TEXT,
        watering_frequency TEXT,
        environment TEXT,
        added_date DATE
    );
    """)
    # e-store
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EStoreProducts (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        size_amount TEXT NOT NULL,
        price REAL NOT NULL,
        is_for_sale BOOLEAN NOT NULL DEFAULT 1,
        location TEXT,
        contact_info TEXT,
        product_image BLOB,
        FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    """)
    # reminder
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Reminders (
        reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plant_name TEXT,
        task TEXT,
        frequency TEXT,
        time TEXT,
        notification INTEGER,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    """)
    #safe plant for the profile 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SafePlant (
        plant_id INTEGER PRIMARY KEY AUTOINCREMENT,
        plant_name TEXT NOT NULL,
        scientific_name TEXT,
        care_instructions TEXT,
        sunlight_requirements TEXT,
        watering_frequency TEXT,
        environment TEXT,
        added_date DATE,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    """)

    # Insert sample data into Users table
    cursor.execute("SELECT COUNT(*) FROM Users;")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO Users (username, email, password, bio) VALUES (?, ?, ?, ?);
        """, [
            ("user1", "user1@example.com", "password1", "Loves gardening."),
            ("user2", "user2@example.com", "password2", "Plant enthusiast."),
            ("user3", "user3@example.com", "password3", "Nature lover.")
        ])
        conn.commit()  # Commit changes

    # Insert sample data into PlantInformation
    cursor.execute("SELECT COUNT(*) FROM PlantInformation;")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO PlantInformation (plant_name, scientific_name, care_instructions, sunlight_requirements, 
                                      watering_frequency, environment, added_date)
        VALUES (?, ?, ?, ?, ?, ?, ?);
        """, [
            ('Apple___healthy', 'Malus domestica', 'Water regularly, especially during dry spells. Prune the tree to maintain shape and remove dead wood.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Blueberry___healthy', 'Vaccinium corymbosum', 'Requires acidic, well-drained soil. Water regularly, especially during fruiting.', 'Full sun to partial shade', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Cherry_(including_sour)___healthy', 'Prunus avium', 'Prune regularly to maintain shape. Water during dry periods.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Corn_(maize)___healthy', 'Zea mays', 'Plant in well-drained soil and water deeply. Requires full sun.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Grape___healthy', 'Vitis vinifera', 'Train vines along trellises. Prune in late winter. Requires well-drained soil and regular watering.', 'Full sun', 'Every 1-2 weeks', 'Mediterranean', date.today()),
        ('Peach___healthy', 'Prunus persica', 'Water regularly during the growing season. Prune for shape and health.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Pepper,_bell___healthy', 'Capsicum annuum', 'Requires warm soil and regular watering. Support stems as needed.', 'Full sun', 'Every 1-2 weeks', 'Warm', date.today()),
        ('Potato___healthy', 'Solanum tuberosum', 'Plant in well-drained, loose soil. Water moderately and avoid overwatering.', 'Full sun', 'Every 1-2 weeks', 'Cool', date.today()),
        ('Raspberry___healthy', 'Rubus idaeus', 'Needs well-drained soil and regular watering. Prune old canes to encourage new growth.', 'Full sun to partial shade', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Soybean___healthy', 'Glycine max', 'Plant in well-drained soil with moderate watering. Avoid overwatering.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Strawberry___healthy', 'Fragaria × ananassa', 'Requires well-drained soil and regular watering. Mulch to protect roots.', 'Full sun', 'Every 1-2 weeks', 'Temperate', date.today()),
        ('Tomato___healthy', 'Solanum lycopersicum', 'Water regularly and support the plant. Avoid water on leaves.', 'Full sun', 'Every 1-2 weeks', 'Warm', date.today())
        ])
        conn.commit()

    # Insert sample data into SafePlant
    cursor.execute("SELECT COUNT(*) FROM SafePlant;")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO SafePlant (plant_name, scientific_name, care_instructions, sunlight_requirements, 
                               watering_frequency, environment, added_date, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, [
            ('Tomato', 'Solanum lycopersicum', 'Water regularly.', 'Full sun', 'Every week', 'Warm', date.today(), 1)
        ])
        conn.commit()

    # Insert sample data into Reminders
    cursor.execute("SELECT COUNT(*) FROM Reminders;")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("""
        INSERT INTO Reminders (plant_name, task, frequency, time, notification, user_id)
        VALUES (?, ?, ?, ?, ?, ?);
        """, [
            ('Tomato', 'Water daily', 'Daily', '08:00 AM', 1, 1)
        ])
        conn.commit()

    print("All tables created and populated successfully!")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the database connection
    conn.close()
