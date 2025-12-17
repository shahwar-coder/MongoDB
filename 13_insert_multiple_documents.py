# > db.users.insertMany([{name:"Sonia", age: 79}, 
#                        {name: "Priyanka", age: 48}])

# < {
#   acknowledged: true,
#   insertedIds: {
#     '0': ObjectId('694209f915141273c307729b'),
#     '1': ObjectId('694209f915141273c307729c')
#    }

'''
db.users.insertMany([...])
- Inserts multiple documents at once
- Each document gets a unique _id
- insertedIds maps index → _id
'''

# =========================

'''
Q1. How is `insertMany()` different from `insertOne()`?
Ans. `insertOne()` inserts one document, while `insertMany()` inserts many documents at once.
'''
# Example
# insertOne  → one document
# insertMany → list (array) of documents

'''
Q2. Does each document inserted by `insertMany()` get an `_id`?
Ans. Yes. MongoDB automatically assigns a unique `_id` to every document.
'''
# Example
# Document 0 → _id = ObjectId(...)
# Document 1 → _id = ObjectId(...)

'''
Q3. What is the one-line rule to remember?
Ans. `insertMany()` inserts an array of documents in one operation, giving each a unique `_id`.
'''
# Example (lock it 🔒)
# One command → many documents stored
