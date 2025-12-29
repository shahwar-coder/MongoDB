# 1️⃣ updateOne() with $rename
# > db.students2.updateOne(
#     { name: "Aisha Khan" },
#     { $rename: { class: "degree" } }
# )

# Output:

# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }



# 2️⃣ find()
# > db.students2.find({ name: "Aisha Khan" })

# {
#   _id: ObjectId('695266f059b327ea6f973ebf'),
#   name: 'Aisha Khan',
#   age: 23,
#   skills: [
#     'Python',
#     'Django',
#     'MongoDB'
#   ],
#   degree: 'BTech'
# }


'''QUESTIONS
Q1. What does the `$rename` operator do in MongoDB?
Ans. `$rename` changes the name of a field in a document without changing its value.
'''
# Example
# old field name → new field name


'''
Q2. What happens in this command?
db.students2.updateOne(
  { name: "Aisha Khan" },
  { $rename: { class: "degree" } }
)
Ans. MongoDB finds Aisha Khan and renames the field `class` to `degree`.
'''
# Important
# Field value ("BTech") stays the same


'''
Q3. Does `$rename` delete or recreate data?
Ans. No. It only renames the field and preserves the value.
'''
# Example
# class: "BTech" → degree: "BTech"


'''
Q4. What does `matchedCount: 1` indicate here?
Ans. Exactly one document matched the filter condition.
'''
# Example
# name: "Aisha Khan" → one match


'''
Q5. What does `modifiedCount: 1` confirm?
Ans. It confirms that the document was actually updated.
'''
# Example
# Field name changed successfully


'''
Q6. Why is `insertedId` null in the output?
Ans. Because this was an update operation, not an insert or upsert.
'''
# Example
# upsertedCount: 0 → no new document created


'''
Q7. How do you verify that `$rename` worked?
Ans. Use `find()` to check the updated document.
'''
# Example
db.students2.find({ name: "Aisha Khan" })
# Output shows:
# - degree field exists
# - class field is gone


'''
Q8. What happens to the old field name after `$rename`?
Ans. The old field (`class`) is completely removed.
'''
# Example
# No duplicate fields are kept


'''
Q9. Is `$rename` safer than replacing a document?
Ans. Yes. It changes only the field name and keeps all other fields intact.
'''
# Example
# _id, name, age, skills stay unchanged


'''
Q10. What is the key difference between `$rename` and `$set`?
Ans. `$rename` changes the field name, `$set` changes the field value.
'''
# Memory lock 🔒
# $rename → name change
# $set    → value change
