import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

# QUERIES
# Ten most expensive items
expensive_items = '''SELECT * FROM product
                    ORDER BY UnitPrice DESC
                    LIMIT 10;'''

# Average age of an employee at the time of hiring
avg_hire_age = '''SELECT AVG(HireDate - Birthdate)
                                FROM Employee;'''

# Ten most expensive items per unit price and their suppliers
ten_most_expensive = '''SELECT CompanyName, ProductName, UnitPrice
                                    FROM Product JOIN Supplier
                                    ON Product.SupplierId = Supplier.Id
                                    ORDER BY UnitPrice LIMIT 10;'''

# the largest category (by number of unique products in it)
largest_category = '''SELECT CategoryName, COUNT(DISTINCT Product.Id)
                    AS product_id FROM Product JOIN Category
                    ON Product.CategoryId = Category.id
                    GROUP BY CategoryName
                    ORDER BY product_id DESC LIMIT 1;'''

# Fetching queries
print('expensive_items:', expensive_items)
print('avg_hire_age:', avg_hire_age)
print('ten_most_expensive:', ten_most_expensive)
print('largest_category:', largest_category)

# Closing conn
curs.close()
conn.close()
