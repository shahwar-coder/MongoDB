# 1️⃣ Existing document (before update)
# {
#   _id: ObjectId('695266f059b327ea6f973ec2'),
#   name: 'Arjun Mehta',
#   age: 24,
#   class: 'MCA',
#   skills: [
#     'Node.js',
#     'Express',
#     'MongoDB'
#   ]
# }


# 2️⃣ updateOne() using $mul
# > db.students2.updateOne(
#     { name: "Arjun Mehta" },
#     { $mul: { age: 2 } }
# )

# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }



# 3️⃣ find() after update
# > db.students2.find({ name: "Arjun Mehta" })
# {
#   _id: ObjectId('695266f059b327ea6f973ec2'),
#   name: 'Arjun Mehta',
#   age: 48,
#   class: 'MCA',
#   skills: [
#     'Node.js',
#     'Express',
#     'MongoDB'
#   ]
# }


'''
Q1. What does the `$mul` operator do in MongoDB?
Ans. `$mul` multiplies the value of a numeric field by a given number.
'''
# Example
# $mul: { age: 2 } → age = age × 2


'''
Q2. What happens in this command?
db.students2.updateOne(
  { name: "Arjun Mehta" },
  { $mul: { age: 2 } }
)
Ans. MongoDB finds Arjun Mehta and multiplies his age by 2.
'''
# Before: age = 24
# After : age = 48


'''
Q3. Does `$mul` replace the document?
Ans. No. `$mul` only modifies the specified numeric field.
'''
# Example
# name, class, skills remain unchanged
# Only age is updated


'''
Q4. Which data types are supported by `$mul`?
Ans. `$mul` works only on numeric fields (int, long, double).
'''
# Example
# age: 24 → valid
# age: "24" ❌ invalid (string)


'''
Q5. What does `matchedCount: 1` indicate here?
Ans. Exactly one document matched the filter condition.
'''
# Example
# name: "Arjun Mehta" → found successfully


'''
Q6. What does `modifiedCount: 1` confirm?
Ans. It confirms that the document was actually updated.
'''
# Example
# age changed from 24 → 48


'''
Q7. What happens if the field does NOT exist?
Ans. MongoDB creates the field and sets it to 0.
'''
# Example
# $mul: { score: 5 }
# score did not exist → score = 0


'''
Q8. Can `$mul` reduce a value?
Ans. Yes. Multiply by a number between 0 and 1.
'''
# Example
# $mul: { age: 0.5 } → age becomes half


'''
Q9. How do you verify that `$mul` worked?
Ans. Use `find()` to read the updated document.
'''
# Example
db.students2.find({ name: "Arjun Mehta" })
# Shows age = 48


'''
Q10. What is the one-line rule to remember?
Ans. `$mul` scales numeric values without touching the rest of the document.
'''
# Memory lock 🔒
# $mul → multiply numbers safely



