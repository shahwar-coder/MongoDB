'''
📘 DOCUMENTED STEPS — What Happened (Line by Line)

Step 1️⃣ Switch database context
Command:
use people

What it does:
- Switches the shell context to a database named "people"
- Does NOT create the database yet (no data written)

Verification:
db
→ confirms current context is "people"


Step 2️⃣ Create a collection
Command:
db.createCollection("persons")

What it does:
- Creates the "persons" collection
- Triggers actual creation of the "people" database on disk

Verification:
show collections
→ shows: persons


Step 3️⃣ Insert multiple documents
Command:
db.persons.insertMany([...])

What it does:
- Inserts 3 documents into the "persons" collection
- Automatically generates `_id` for each document
- Persists data to disk
- Demonstrates multiple MongoDB data types

Output:
acknowledged: true
insertedIds:
  0 → Ali
  1 → Fatima
  2 → Yusuf

This confirms:
✔ Database exists
✔ Collection exists
✔ Documents stored successfully
'''


'''
📘 DATA TYPES USED — What You Practiced Correctly

• String
  → name, city, country

• Int32
  → age, score (NumberInt)

• Double
  → height, rating

• Boolean
  → isMarried

• Array
  → skills

• Embedded Object
  → address

• Date
  → joinedAt (new Date())

• Null
  → rating (Ali)

• Int64 (Long)
  → salary (NumberLong)

This is an excellent real-world style document structure.
'''
