# 1️⃣ Existing document (before update)
# {
#   _id: ObjectId('695266f059b327ea6f973ec1'),
#   name: 'Sara Ali',
#   age: 23,
#   class: 'MSc',
#   skills: [
#     'Machine Learning',
#     'Python',
#     'NumPy'
#   ]
# }


# 2️⃣ updateOne() using $inc
# > db.students2.updateOne(
#     { name: "Sara Ali" },
#     { $inc: { age: 2 } }
# )

# Output:

# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }


# 3️⃣ find() after update
# > db.students2.find({ name: "Sara Ali" })

# {
#   _id: ObjectId('695266f059b327ea6f973ec1'),
#   name: 'Sara Ali',
#   age: 25,
#   class: 'MSc',
#   skills: [
#     'Machine Learning',
#     'Python',
#     'NumPy'
#   ]
# }


'''
Q1. What does the `$inc` operator do in MongoDB?
Ans. `$inc` increases or decreases a numeric field by a given value.
'''
# Example
# $inc: { age: 2 } → age = age + 2


'''
Q2. What happens in this command?
db.students2.updateOne(
  { name: "Sara Ali" },
  { $inc: { age: 2 } }
)
Ans. MongoDB finds Sara Ali and increases her age by 2.
'''
# Before: age = 23
# After : age = 25


'''
Q3. Does `$inc` replace the age field or modify it?
Ans. It modifies the existing value; it does NOT replace the document.
'''
# Example
# Only `age` changes
# name, class, skills remain unchanged


'''
Q4. What data types work with `$inc`?
Ans. `$inc` works only on numeric fields (int, long, double).
'''
# Example
# age: 23 → valid
# age: "23" ❌ invalid (string)


'''
Q5. What does `matchedCount: 1` mean here?
Ans. Exactly one document matched the filter `{ name: "Sara Ali" }`.
'''
# Example
# Filter found Sara Ali successfully


'''
Q6. What does `modifiedCount: 1` confirm?
Ans. It confirms the document was actually updated.
'''
# Example
# age changed from 23 → 25


'''
Q7. What happens if the field does NOT exist?
Ans. MongoDB creates the field and sets it to the increment value.
'''
# Example
# $inc: { score: 5 }
# score did not exist → score = 5


'''
Q8. Can `$inc` decrease a value?
Ans. Yes. Use a negative number.
'''
# Example
# $inc: { age: -1 } → age decreases by 1


'''
Q9. How do you verify the result of `$inc`?
Ans. Use `find()` to read the updated document.
'''
# Example
db.students2.find({ name: "Sara Ali" })
# Shows age = 25


'''
Q10. What is the one-line rule to remember?
Ans. `$inc` safely updates numeric fields without touching the rest of the document.
'''
# Memory lock 🔒
# $inc → change numbers only
