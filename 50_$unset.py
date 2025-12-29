# 1️⃣ updateOne() with $unset
# > db.students2.updateOne(
#     { name: "Rahul Verma" },
#     { $unset: { class: "" } }
# )

# <{
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }


# 2️⃣ find()
# > db.students2.find({ name: "Rahul Verma" })

# <{
#   _id: ObjectId('695266f059b327ea6f973ec0'),
#   name: 'Rahul Verma',
#   age: 21,
#   skills: [
#     'C',
#     'C++',
#     'Data Structures'
#   ]
# }



'''
Q1. What does `$unset` do in MongoDB?
Ans. `$unset` removes a field completely from a document.
'''
# Example
# $unset deletes the field, not just its value


'''
Q2. What happens in this command?
db.students2.updateOne(
  { name: "Rahul Verma" },
  { $unset: { class: "" } }
)
Ans. MongoDB finds Rahul Verma and removes the `class` field from his document.
'''
# Important
# Value "" is ignored → field name is what matters


'''
Q3. Does `$unset` set the field to null?
Ans. No. `$unset` removes the field entirely.
'''
# Example
# Before: { name: "Rahul", class: "BSc" }
# After : { name: "Rahul" }


'''
Q4. Why is `$unset` safer than replacing the document?
Ans. Because it removes only one field and keeps the rest of the document intact.
'''
# Example
# _id, age, skills remain unchanged


'''
Q5. What does `matchedCount: 1` mean in the result?
Ans. It means exactly one document matched the filter condition.
'''
# Example
# name: "Rahul Verma" → found 1 document


'''
Q6. What does `modifiedCount: 1` indicate?
Ans. It means the document was actually changed.
'''
# Example
# Field `class` existed → removed successfully


'''
Q7. Why is `insertedId` null here?
Ans. Because this was an update, not an insert or upsert.
'''
# Example
# upsertedCount: 0 → no new document created


'''
Q8. How do you verify that `$unset` worked?
Ans. Use `find()` to read the updated document.
'''
# Example
db.students2.find({ name: "Rahul Verma" })
# Output shows:
# - name
# - age
# - skills
# ❌ class field is gone


'''
Q9. What does `find()` return in this case?
Ans. It returns the document without the `class` field, proving it was removed.
'''
# Example
# Missing field ≠ null field
# Field no longer exists


'''
Q10. What is the key difference between `$unset` and `$set: { field: null }`?
Ans. `$unset` removes the field, `$set: null` keeps the field with a null value.
'''
# Memory lock 🔒
# $unset → field deleted
# $set: null → field exists but empty
