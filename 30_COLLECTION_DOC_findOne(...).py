# > db.users.findOne({name : "Rahul"})
# < {
#   _id: ObjectId('6941ecad15141273c307729a'),
#   name: 'Rahul',
#   age: 51,
#   city: 'Delhi'
# }

# > db.users.findOne({name : "Adam"})
# < null

'''
db.users.findOne({ field: value })
- Returns the first matching document
- Returns null if no match
'''

# ==========

'''
Q1. What does `db.users.findOne()` do?
Ans. It finds and returns ONE document from the `users` collection that matches the given condition.
'''
# Example
# db.users.findOne({ name: "Rahul" })

'''
Q2. Why does `findOne()` return only one document?
Ans. Because it stops searching after the first match is found.
'''
# Example
# Even if multiple users are named "Rahul",
# findOne() returns only one document.

'''
Q3. Is it guaranteed which document `findOne()` returns if many match?
Ans. No. There is no guarantee — it returns the first match MongoDB finds internally.
'''
# Example
# Order is not guaranteed unless explicitly sorted.
# ---------
# findOne() returns the first document MongoDB encounters
# according to its internal execution plan.

'''
Q4. What happens if no document matches the condition?
Ans. MongoDB returns `null`.
'''
# Example
# db.users.findOne({ name: "Unknown" })
# Output: null

'''
Q5. Why does `_id` appear in the result?
Ans. Because MongoDB always includes `_id` by default in query results.
'''
# Example
# _id is auto-added and always returned unless excluded.

'''
Q6. How is `findOne()` different from `find()`?
Ans. `findOne()` returns a single document or null, while `find()` returns a cursor of documents.
'''
# Example
# find()    → many documents
# findOne() → one document
