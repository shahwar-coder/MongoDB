# > db
# < school

# > show collections
# < students

# > db.students.drop()
# < true

# > show collections
# < <empty>

'''
1. db.students.drop()
   - Drops the "students" collection from the current database

2. show collections
   - Verifies that the collection is removed
   - "students" will no longer be listed
'''

# ================

'''QUESTIONS
Q1. What happens to the data after dropping a collection?
Ans. All documents inside that collection are permanently deleted.
'''
# Example
# students collection → ❌ gone
# documents inside → ❌ gone

'''
Q2. Why does `show collections` show nothing after dropping?
Ans. Because there are no collections left that actually exist in the current database.
'''
# Example
# show collections
# Output: <empty>

'''
Q3. What does the return value `true` from `drop()` mean?
Ans. It confirms that the collection was successfully dropped.
'''
# Example
# true → operation successful
# false → collection did not exist

'''
Q4. Does dropping the last collection delete the database?
Ans. Yes, effectively. If a database has no collections and no data, MongoDB no longer treats it as existing.
'''
# Example
# Drop last collection → database disappears from `show dbs`
# eg.
# > show dbs
# < admin
  # config
  # local
# school is not appearing anymore.

'''
Q5. What is the one-line rule to remember?
Ans. Dropping a collection removes its data, and if it was the last one, the database becomes invisible.
'''
# Example (lock it 🔒)
# No collections → no database (MongoDB’s view)
