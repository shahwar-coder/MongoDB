'''
> show databases
'''
# > show dbs
# admin    40.00 KiB
# config  108.00 KiB
# local    72.00 KiB

'''
Q1. What does the `show dbs` command do in MongoDB?
Ans. It asks MongoDB to list all databases that currently exist on the server.
'''
# Example
# Command:
# show dbs
# Meaning:
# “Show me all existing databases.”


'''
Q2. What does “exist” mean for a database in MongoDB?
Ans. A database exists only if it has at least ONE document stored in it.
'''
# Example
# Database with data → shown in `show dbs`
# Database with NO data → NOT shown


'''
Q3. Why doesn’t MongoDB show empty databases?
Ans. Because MongoDB creates databases lazily — only when data is actually stored.
'''
# Example
# use mydb
# show dbs
# mydb ❌ not visible (no data yet)


'''
Q4. Why is this different from SQL databases?
Ans. SQL databases exist even when empty, but MongoDB hides databases until they contain data.
'''
# Example
# SQL: CREATE DATABASE school; → exists immediately
# MongoDB: use school → exists only after insert


'''
Q5. Why do system databases like admin, config, and local always appear?
Ans. Because MongoDB itself stores internal data in them, so they always contain documents.
'''
# Example
# admin   → authentication & system info
# config  → cluster metadata
# local   → local server data


'''
Q6. What does the size shown next to a database mean?
Ans. It shows how much disk space the database is using (data + indexes).
'''
# Example
# admin   40.00 KiB
# Size > 0 ⇒ database truly exists


'''
Q7. What is the one rule you must always remember about `show dbs`?
Ans. `show dbs` lists ONLY databases that contain at least one document.
'''
# Example (lock it 🔒)
# No data → no database (as far as MongoDB is concerned)
