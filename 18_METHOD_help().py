'''
help()           -> shell commands
db.help()        -> database commands
db.users.help()  -> collection commands
'''


# =====


'''
Q1. What information does `help()` (without anything before it) show?
Ans. It shows general shell help: database commands, collection commands, utilities, and shortcuts.
'''
# Example
# help()
# → overview of what you can do in mongosh

'''
Q2. What does `db.help()` do?
Ans. It shows all commands you can run on the current database.
'''
# Example
# db.help()
# → db.dropDatabase(), db.createCollection(), db.getCollectionNames(), etc.

'''
Q3. What does `db.employees.help()` do?
Ans. It lists all operations available on the `employees` collection.
'''
# Example
# db.employees.help()
# → find(), findOne(), insertOne(), insertMany(), updateOne(), deleteOne(), countDocuments()

'''
Q4. Can you use `find.help()` to get help for a method?
Ans. No. MongoDB does not support `.help()` on individual methods.
'''
# Example
# ❌ find.help()
# ✅ db.users.find   (prints usage/signature)
