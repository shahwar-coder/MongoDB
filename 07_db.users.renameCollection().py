'''
db.users.renameCollection("employees")
- Renames a collection
- Data and indexes remain unchanged

show collections
- Verifies the rename
'''

# > show collections
# users

# > db.getCollectionNames()
# [ 'users' ]

# > db.users.renameCollection("employee")
# { ok: 1 }

# > show collections
# employee

# > db.users.find()

# > db.employee.find()
# {
#   _id: ObjectId('6941ecad15141273c307729a'),
#   name: 'Rahul',
#   age: 51,
#   city: 'Delhi'
# }
# {
#   _id: ObjectId('694209f915141273c307729b'),
#   name: 'Sonia',
#   age: 79
# }
# {
#   _id: ObjectId('694209f915141273c307729c'),
#   name: 'Priyanka',
#   age: 48
# }

# office>


'''
Q1. Does renaming a collection affect the data?
Ans. No. All documents inside the collection remain exactly the same.
'''
# Example
# Before rename → 3 documents
# After rename  → same 3 documents

'''
Q2. Are indexes affected when a collection is renamed?
Ans. No. All indexes are preserved during the rename.
'''
# Example
# _id index and any custom indexes stay intact

'''
Q3. Is data copied during `renameCollection()`?
Ans. No. MongoDB only changes the collection name; no data copying happens.
'''
# Example
# Fast operation → metadata change only


'''
Q4. What happens if you try to access the old collection name?
Ans. It will not exist anymore, so queries on it will fail or return nothing.
'''
# Example
# db.users.find()      → ❌ no such collection
# db.employees.find() → ✅ documents returned

'''
Q5. Which database does `renameCollection()` apply to?
Ans. It applies only to the current database context.
'''
# Example
# db → office
# users → employees happens inside office DB only
