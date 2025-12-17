# > db.users.countDocuments()
# < 3

'''
db.users.countDocuments()
- Returns total number of documents in the collection
'''

# ==========

'''
Q1. What does `db.users.countDocuments()` do?
Ans. It returns the total number of documents present in the `users` collection.
''' 
# -my-case-
# Example
# db.users.countDocuments()
# Output: 3

'''
Q2. Can `countDocuments()` be used with a condition?
Ans. Yes. You can pass a filter to count only matching documents.
'''
# Example
# db.users.countDocuments({ age: { $gt: 50 } })
# Counts users older than 50

'''
Q3. Why is `countDocuments()` the recommended way to count?
Ans. Because it is accurate, safe, and respects filters correctly.
'''
# Example
# Preferred over old count() method

'''
Q4. Which collection does `countDocuments()` run on?
Ans. It runs on the collection you specify, inside the current database.
'''
# Example
# db → office
# db.users.countDocuments() → counts users in office DB only
