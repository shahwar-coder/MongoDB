'''
Q1. What does `updateOne()` do in MongoDB?
Ans. It finds ONE document that matches a filter and updates specific fields in it.
'''
# Syntax
# db.collection.updateOne(filter, update, options)


'''
Q2. What is the role of the filter in `updateOne()`?
Ans. The filter decides WHICH document should be updated.
Usually `_id` is used because it is unique and safe.
'''
# Example
# { _id: ObjectId("...") }
# Only one document can match this


'''
Q3. Why must update operations use operators like `$set`?
Ans. Because MongoDB needs to know HOW to update, not replace, the document.
'''
# Correct
# { $set: { age: 44 } }

# Wrong ❌ (replaces whole document)
# { age: 44 }


'''
Q4. What does `$set` exactly do?
Ans. `$set` updates or adds only the specified fields and keeps the rest unchanged.
'''
# Example
# $set: { name: "SHAHID", skills: ["AWS", "GenAI"] }
# Other fields remain untouched


'''
Q5. What do `matchedCount` and `modifiedCount` mean?
Ans. `matchedCount` shows how many documents matched the filter.
`modifiedCount` shows how many documents were actually changed.
'''
# Example result
# matchedCount: 1  → document found
# modifiedCount: 1 → document updated


'''
Q6. What is a common beginner mistake with `updateOne()`?
Ans. Forgetting `$set`, which causes the entire document to be replaced.
'''
# Example (dangerous ❌)
# updateOne({ _id: ... }, { name: "New Name" })


'''
Q7. Name some basic update operators every beginner must know.
Ans. `$set`, `$inc`, `$push`, `$pull`, `$unset`.
'''
# Example
# $inc   → increase number
# $push  → add to array
# $unset → remove field


'''
Q8. What is the mental model to remember for updates?
Ans. Always think: target first, then modify safely using operators.
'''
# Memory lock 🔒
# updateOne = filter + operator + changes
