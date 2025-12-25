# > db.dropDatabase()
# < { ok: 1, dropped: 'school' }
# --------------------------------
# > db
# < school

# > db. dropDatabase()
# < { ok: 1, dropped: "school' }

# > db. dropDatabase()
# < { ok: 1, dropped: "school" }

# > db. dropDatabase()
# < { ok: 1, dropped: "school" }

# school›

'''
1. db.dropDatabase()
   - Deletes the current database and all its collections

2. show dbs
   - Verifies the database is removed
'''

# ====================

'''
Q1. What does this output mean?
Ans. It confirms the database was successfully deleted.
'''
# Example
# { ok: 1, dropped: 'school' }
# ok: 1        → command succeeded
# dropped name → database removed

'''
Q2. What happens to collections inside the database?
Ans. All collections and their documents are permanently deleted.
'''
# Example
# students, teachers, exams → ❌ all gone


'''
Q3. Why does the database disappear from `show dbs`?
Ans. Because MongoDB shows only databases that contain data.
'''
# Example
# No data + no collections → database is invisible

'''
Q4. Is `db.dropDatabase()` reversible?
Ans. No. Once dropped, the database and all its data are permanently lost.
'''
# Example
# Drop = final action

'''
Q5. Why can `db.dropDatabase()` be run multiple times without error?
Ans. Because MongoDB allows dropping a database even if it does not physically exist.
It treats the command as safe to repeat.
'''
# Example
# use school
# db.dropDatabase()  → { ok: 1 }
# db.dropDatabase()  → { ok: 1 } again
# No error both times (idempotent behavior)

'''
Q6. What does MongoDB actually do when you run `use school`?
Ans. It switches the shell context to the NAME `school`. It does not check or create the database.
'''
# Example
# use school
# Prompt shows: school>
# This is context only, not existence.

'''
Q7. Why does `db.dropDatabase()` return `{ ok: 1 }` even if the DB doesn’t exist?
Ans. MongoDB tries to drop the current database name; if nothing exists, it still reports success.
'''
# Example
# Internally:
# “Nothing to delete, but operation completed safely.”

'''
Q8. Why do you still see `school>` after dropping the database?
Ans. Because `school>` is just the current shell context, not the actual database.
'''
# Example
# db.dropDatabase()
# Prompt still shows: school>
# Context stays even though DB is gone.

'''
Q9. How can you prove the database does NOT exist anymore?
Ans. By running `show dbs` and confirming `school` is not listed.
'''
# Example
# show dbs
# admin
# config
# local
# school ❌ not present → DB truly deleted

'''
Q10. What is the difference between context and existence in MongoDB?
Ans. Context is the name you’re pointing at; existence means data actually lives on disk.
'''
# Example
# school>        → context (name only)
# show dbs       → actual databases on disk

'''
Q11. Why does MongoDB separate context from existence?
Ans. To allow flexible scripting and future databases without forcing existence checks.
'''
# Example
# Scripts can safely do:
# use logs
# db.dropDatabase()
# even if logs never existed.

'''
Q12. What is the one-line rule to lock this concept?
Ans. MongoDB separates “context” from “existence”; you can be in a DB context even if the DB doesn’t exist.
'''
# Example (lock it 🔒)
# Prompt name ≠ real database
