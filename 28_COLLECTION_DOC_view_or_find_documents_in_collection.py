# > show collections
# < users
  
# > db.users.find()
# < {
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

# > db.users.find().pretty()
# ...
# ...
# ...


'''
db.users.find()
- Returns all documents in the collection

db.users.find().pretty()
- Same result, formatted for readability
'''

# ======================

'''
Q1. What does `db.users.find()` do?
Ans. It returns ALL documents stored in the `users` collection.
'''
# Example
# db.users.find()
# Output:
# { _id: ..., name: "Rahul", age: 51 }
# { _id: ..., name: "Sonia", age: 79 }
# { _id: ..., name: "Priyanka", age: 48 }


'''
Q2. Why does `find()` show every document one by one?
Ans. Because `find()` returns a cursor, and MongoDB prints each document from that cursor.
'''
# Example
# Cursor → list-like result
# Each document is displayed separately
# -------------------------------------
# In MongoDB terms

# db.users.find()

# This does NOT return all documents immediately.

# It returns a cursor → a result iterator.

# Mongo shell then:

# Takes that cursor

# Iterates it

# Prints each document one by one

# That's why you see:

# { ... }
# { ... }
# { ... }

# Not wrapped in a list.


'''
Q3. Why does `_id` appear in every result?
Ans. Because MongoDB always includes `_id` by default, and every document must have it.
'''
# Example
# You didn’t add _id
# MongoDB added it automatically


'''
Q4. Is the output of `find()` pure JSON?
Ans. No. It is JavaScript-style output optimized for the MongoDB shell.
'''
# Example
# Looks like JSON
# But technically JavaScript objects (shell-friendly)


'''
Q5. What does `db.users.find().pretty()` do?
Ans. It formats the same results with better spacing and indentation.
'''
# Example
# db.users.find().pretty()
# Same data, easier to read

'''
Q6. What is find() output exactly, if not JSON?
Ans. It is BSON documents printed as JavaScript object literals by the MongoDB shell.
'''

'''
Q7. ----> CHRONOLOGICAL ORDER FLOW.....
MongoDB find() – chronological flow

1. Data is stored in MongoDB as BSON (Binary JSON), not JSON.

2. You run a query:
   db.users.find()

3. MongoDB executes the query and identifies matching documents.

4. MongoDB returns a CURSOR, not the documents themselves.
   - Cursor = iterator/handle to the results

5. The cursor fetches BSON documents in small batches
   - Improves performance
   - Saves memory

6. MongoDB shell iterates over the cursor
   - One document at a time

7. Each BSON document is converted into a JavaScript object
   - For shell-friendly display
   - Uses helpers like ObjectId()

8. The shell prints each document separately
   { ... }
   { ... }
   { ... }

End result:
Stored: BSON
Returned: Cursor
Displayed: JavaScript-style objects
'''



'''
Q8. Does `pretty()` change the data or performance?
Ans. No. It only changes how the output looks.
'''
# Example
# Data = same
# Speed = same
# Only readability improves


'''
Q9. What is the difference between `find()` and `find().pretty()`?
Ans. There is no difference in results — only formatting is different.
'''
# Example
# find()          → compact output
# find().pretty() → readable output


'''
Q10. What is the one-line rule to remember?
Ans. `find()` reads documents; `pretty()` only improves readability.
'''
# Example (lock it 🔒)
# Read ≠ format

