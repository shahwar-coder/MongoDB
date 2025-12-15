'''
'''

'''
Q1. Does `use dbName` create a database in MongoDB?
Ans. No. `use dbName` only switches the current database context. It does NOT create a database.
'''
# Example
# use school
# Output: switched to db school
# ❌ No database created yet


'''
Q2. What does `use dbName` actually do then?
Ans. It tells MongoDB: “If I create data next, use this database name.”
'''
# Example
# use myDatabase
# MongoDB just remembers the name — nothing is stored on disk.


'''
Q3. When is a database actually created in MongoDB?
Ans. A database is created ONLY when data is written (or a collection is created).
'''
# Example
# db.users.insertOne({ name: "Ali" })
# 💥 Now MongoDB creates:
# - the database
# - the collection
# - storage on disk


'''
Q4. Why doesn’t a new database appear in `show dbs` after `use dbName`?
Ans. Because empty databases do not exist in MongoDB’s view.
'''
# Example
# use testdb
# show dbs
# ❌ testdb not listed (no data inside)


'''
Q5. Why does MongoDB behave this way?
Ans. MongoDB is lazy by design — it creates things only when needed to save space and scale better.
'''
# Example
# No data → no database
# Data inserted → database becomes real


'''
Q6. How is this different from SQL databases?
Ans. SQL creates databases immediately, MongoDB creates them only after data is inserted.
'''
# Example
# SQL: CREATE DATABASE school;  → exists instantly
# MongoDB: use school          → exists only after insert


'''
Q7. How can you check which database you are currently using?
Ans. Use the `db` command — it shows the current database context.
'''
# Example
# db
# Output: myDatabase
# (This shows context, not existence)


'''
Q8. What is the one-line rule to remember?
Ans. `use dbName` switches context; the database is created only when data is written.
'''
# Example (lock it 🔒)
# Switch ≠ Create
# Insert = Make it real
