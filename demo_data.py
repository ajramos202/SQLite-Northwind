import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()
DROP_DEMO_TABLE = "DROP TABLE IF EXISTS demo"
curs.execute(DROP_DEMO_TABLE)


curs.execute('''
            CREATE TABLE IF NOT EXISTS demo
            (s TEXT,
            x INTEGER,
            y INTEGER); ''')

# Write and execute INSERT INTO statements
curs.execute("INSERT INTO demo (s,x,y) VALUES ('g', 3, 9);")
curs.execute("INSERT INTO demo (s,x,y) VALUES ('v', 5, 7);")
curs.execute("INSERT INTO demo (s,x,y) VALUES ('f', 8, 7);")

conn.commit()

# Queries
# Count of rows in DF
row_count = curs.execute('SELECT COUNT(*) FROM demo;').fetchall()


# How many rows are there where both x and y are at least 5?
xy_at_least_5 = curs.execute('''SELECT COUNT(*) FROM demo
                                WHERE x >= 5 AND y >= 5;''').fetchall()

# Unique values of y
unique_y = curs.execute('''SELECT COUNT(DISTINCT y) FROM demo;''').fetchall()

# Fetching queries
print('row_count:', row_count)
print('xy_at_least_5:', xy_at_least_5)
print('unique_y:', unique_y)

# Closing conn
curs.close()
conn.close()
