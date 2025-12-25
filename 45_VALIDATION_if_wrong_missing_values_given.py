'''
Q1. When does MongoDB apply JSON Schema validation?
Ans. MongoDB validates a document BEFORE inserting or updating it.
'''
# Example
# Insert request → validation → store OR reject


'''
Q2. What happens if a required field is missing?
Ans. MongoDB rejects the operation and does not store the document.
'''
# Example
# required: ["name", "age", "course"]
# Missing "course" ❌ → insert fails


'''
Q3. What happens if a field has the wrong data type?
Ans. MongoDB rejects the document because bsonType rules are violated.
'''
# Example
# age expects int
# age: "18" ❌ string → rejected
# age: NumberInt(18) ✅ accepted


'''
Q4. What happens if a value is outside the allowed range?
Ans. MongoDB blocks the insert or update.
'''
# Example
# age minimum = 5
# age: 3 ❌ → rejected
# age: 10 ✅ → accepted


'''
Q5. What happens if an enum rule is violated?
Ans. MongoDB rejects the document if the value is not in the enum list.
'''
# Example
# enum: ["BCA", "BTech", "BSc"]
# course: "MBA" ❌ → rejected


'''
Q6. Are extra (unknown) fields allowed by default?
Ans. Yes. MongoDB allows extra fields unless you explicitly restrict them.
'''
# Example
# { name, age, course, hobby }
# "hobby" is allowed by default ✅


'''
Q7. What kind of error does MongoDB throw on validation failure?
Ans. A write error saying “Document failed validation”.
'''
# Example
# Error includes:
# - field name
# - rule violated


'''
Q8. What is the one-line rule to remember?
Ans. If a document violates the schema, MongoDB blocks the write and stores nothing.
'''
# Example (lock it 🔒)
# Validate first → store only if valid
