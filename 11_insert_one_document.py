# > db.createCollection("users")
# < { ok : 1 }

# > db.users.insertOne({name: "Rahul", age: 51, city: "Delhi"})
# < {
#   acknowledged: true,
#   insertedId: ObjectId('6941ecad15141273c307729a')
#   }

# office>

'''
db.users.insertOne({...})
- Inserts one document into a collection
- Auto-creates collection if missing
- Auto-adds _id
- Makes database persist on disk
'''

# ======================

'''
Q1. What happens if the collection does not exist?
Ans. MongoDB automatically creates the collection before inserting the document.
'''
# Example
# users collection did not exist
# insertOne() → creates `users` collection + inserts document

'''
Q2. Does `insertOne()` also create the database?
Ans. Yes. If the database does not exist, MongoDB creates it when the document is inserted.
'''
# Example
# use office
# db.users.insertOne({...})
# → office database now exists on disk

'''
Q3. What is the `_id` field and why is it added?
Ans. `_id` is a unique identifier automatically added by MongoDB to every document.
'''
# Example
# {
#   _id: ObjectId("64f..."),
#   name: "Rahul",
#   age: 51
# }

'''
Q4. What does `acknowledged: true` mean in the output?
Ans. It means MongoDB successfully accepted and saved the write operation.
'''
# Example
# acknowledged: true → write was successful

'''
Q5. What does `insertedId` represent?
Ans. It is the `_id` value of the newly inserted document.
'''
# Example
# insertedId: ObjectId("64f...")

'''
Q6. Why is `insertOne()` considered end-to-end?
Ans. Because it can create the database, create the collection, and store data in one step.
'''
# Example
# Context → Collection → Document
# All handled automatically

'''
Q7. What is the one-line rule to remember?
Ans. `insertOne()` inserts a single document and auto-creates the collection and database if needed.
'''
# Example (lock it 🔒)
# One command → full persistence
