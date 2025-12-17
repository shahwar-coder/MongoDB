# > show collections
# < students

'''
1. show collections
   - Lists all collections in the current database
   - Shows only collections that actually exist

(Requires that a database is already selected using `use dbName`)
'''

# ===============

'''QUESTIONS
Q1. Does `show collections` work across all databases?
Ans. No. It works ONLY for the database you are currently in.
'''
# Example
# db → school
# show collections → shows collections inside `school` only

'''
Q2. How can you be sure which database `show collections` is using?
Ans. Run `db` first to check the current database context.
'''
# Example
# db
# Output: school
# show collections → collections inside school

'''
Q3. How does a collection become visible to `show collections`?
Ans. When you either create it explicitly or insert a document into it.
'''
# Example
# db.createCollection("students")
# OR
# db.students.insertOne({ name: "Ali" })
