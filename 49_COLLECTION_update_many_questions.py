'''
Q1. What is `updateMany()` in MongoDB?
Ans. `updateMany()` updates ALL documents that match a given filter.
'''
# Syntax
# db.collection.updateMany(filter, update)


'''
Q2. What is the main difference between `updateOne()` and `updateMany()`?
Ans. `updateOne()` updates only the first matching document,
while `updateMany()` updates all matching documents.
'''
# Example
# updateOne()  → 1 document
# updateMany() → many documents


'''
Q3. What does the filter do in `updateMany()`?
Ans. The filter decides WHICH documents should be updated.
'''
# Example
{ "class": { "$in": ["BTech", "BSc"] } }
# Matches all students in BTech or BSc


'''
Q4. What does the `$inc` operator do?
Ans. `$inc` increases (or decreases) a numeric field by a given value.
'''
# Example
{ "$inc": { "age": 1 } }
# Increases age by 1 for each matched document


'''
Q5. What happens internally when `updateMany()` runs?
Ans. MongoDB finds all matching documents and applies the update to each one.
'''
# Example
# 2 matches → 2 updates performed


'''
Q6. What do `matchedCount` and `modifiedCount` mean?
Ans. `matchedCount` is how many documents matched the filter.
`modifiedCount` is how many were actually changed.
'''
# Example result
# matchedCount: 2
# modifiedCount: 2


'''
Q7. Why must update operators like `$set` or `$inc` be used?
Ans. Without operators, MongoDB would replace the entire document.
'''
# Correct
{ "$set": { "status": "active" } }

# Wrong ❌
{ "status": "active" }


'''
Q8. What does an empty filter `{}` mean in `updateMany()`?
Ans. It matches ALL documents in the collection.
'''
# Example
# Add a field to every document
db.students2.updateMany({}, { "$set": { "status": "active" } })


'''
Q9. Give one real-life use case for `updateMany()`.
Ans. Bulk updates like marking all users active, increasing age, or adding flags.
'''
# Example
# Increase age for all students in a class


'''
Q10. What is the one-line mental model to remember?
Ans. `updateMany()` = filter everyone first, then update them safely.
'''
# Memory lock 🔒
# updateMany → bulk update with operators
