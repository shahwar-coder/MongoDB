'''
Q1. What is SQL in simple words?
Ans. SQL is a relational database system that stores data in tables with rows and columns using a fixed schema.
'''
# Example (SQL query)
# SELECT name FROM users WHERE id = 1;


'''
Q2. Why is SQL good for structured data?
Ans. Because it uses strict schemas and supports powerful joins, making it perfect for organized, predictable data.
'''
# Example
# Tables: users, orders → join them using user_id.
# Detailed Example:
# users table:
# | id | name  |
# |----|-------|
# | 1  | Alice |
# | 2  | Bob   |    

# orders table:
# | id | user_id | product  |
# |----|---------|----------|
# | 1  | 1       | Laptop   |
# | 2  | 2       | Smartphone|

# SQL Join Query:
# SELECT users.name, orders.product
# FROM users
# JOIN orders ON users.id = orders.user_id;

# Result:
# | name  | product   |
# |-------|-----------|
# | Alice | Laptop    |
# | Bob   | Smartphone|


'''
Q3. What is NoSQL in simple words?
Ans. NoSQL is a non-relational database system with flexible schemas that can store data as documents, key-values, or graphs.
'''
# Example (MongoDB document)
# {"_id": "u1", "name": "Ali", "skills": ["Python", "AI"]}


'''
Q4. Why is NoSQL good for large or fast-changing data?
Ans. It scales across many servers easily and lets you change data shapes without strict rules.
'''
# Example
# Add a new field "age" anytime → no migration needed.
# But in case of SQL, you would need to ALTER the table schema.


'''
Q5. What is the biggest difference between SQL and NoSQL?
Ans. SQL uses fixed schemas and tables; NoSQL uses flexible schemas like JSON, key-value, or graphs.
'''
# Example
# SQL → table row
# NoSQL → JSON document


'''
Q6. How do SQL and NoSQL differ in scalability?
Ans. SQL scales vertically (bigger server), while NoSQL scales horizontally (more servers).
'''
# Let's understand with an example:
# SQL: Upgrade to a more powerful server to handle more load.
# NoSQL: Add more servers to distribute the load.
# ----------
# Which one is better? It depends on your needs!
#  - If you need complex queries and transactions, SQL's vertical scaling is better.
#  - If you need to handle massive amounts of data and high traffic, NoSQL's horizontal scaling is more effective.
# ----------
# Simple real life example:
# SQL: A small business database on a single server.
# NoSQL: A social media platform distributing data across many servers.


'''
Q7. When should you choose SQL?
Ans. When you need strong accuracy, consistency, joins, and structured data.
'''
# Example
# Banking, finance, inventory systems.


'''
Q8. When should you choose NoSQL?
Ans. When you have huge data, fast reads/writes, or constantly changing data structures.
'''
# Example
# Social media feed, IoT sensors, analytics dashboards.


'''
Q9. What should a developer learn first?
Ans. SQL is required for most jobs; NoSQL (like MongoDB) is great for modern backends and AI projects.
'''
# Example
# SQL for company systems → NoSQL for flexible APIs.


'''
Q10. What is the one-line takeaway?
Ans. SQL = structured + stable + relational.
     NoSQL = flexible + scalable + distributed.
'''
# Example (flashcard)
# SQL → Tables | NoSQL → JSON-like documents

# test change
