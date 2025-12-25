# example schema:
# db.createCollection("students", {
#   validator: {
#     $jsonSchema: {
#       title: "Student Object Validation",
#       required: ["name", "age", "course"],
#       properties: {
#         name: {
#           bsonType: "string",
#           description: "Name must be a string and is required"
#         },
#         age: {
#           bsonType: "int",
#           minimum: 5,
#           maximum: 20,
#           description: "Age must be an integer and is required"
#         },
#         course: {
#           bsonType: "string",
#           enum: ["BCA", "BTech", "BSc"],
#           description: "Name must be a string and is required"
#         }
#       }
#     }
#   }
# })

'''
Q1. What is JSON Schema Validation in MongoDB?
Ans. It is a way to enforce basic rules on documents, even though MongoDB is schema-less.
It makes MongoDB schema-controlled, not schema-less.
'''
# Example
# MongoDB allows flexibility,
# but validation ensures minimum structure.


'''
Q2. Where does JSON Schema validation live?
Ans. Validation is attached to a COLLECTION, not the database or individual documents.
'''
# Example
db.createCollection("students", {
  validator: {
    $jsonSchema: {
      required: ["name", "age"]
    }
  }
})


'''
Q3. What does `required` mean in JSON Schema?
Ans. It lists fields that MUST be present in every document.
'''
# Example
# required: ["name", "age"]
# Missing either → insert/update fails ❌


'''
Q4. What is `properties` used for?
Ans. `properties` defines rules for each field like type and allowed range.
'''
# Example
age: {
  bsonType: "int",
  minimum: 5,
  maximum: 20
}


'''
Q5. What is `bsonType` and why is it important?
Ans. MongoDB validates BSON types, not JavaScript types.
'''
# Example
# age: 10        ❌ (double)
# age: NumberInt(10) ✅ (int)


'''
Q6. What does `enum` do in schema validation?
Ans. It restricts a field to a fixed set of allowed values.
'''
# Example
course: {
  bsonType: "string",
  enum: ["BCA", "Btech", "BSc"]
}


'''
Q7. How are arrays validated in JSON Schema?
Ans. You define the field as an array and specify the type of each item.
'''
# Example
skills: {
  bsonType: "array",
  items: { bsonType: "string" }
}


'''
Q8. What happens if a document violates the schema?
Ans. MongoDB rejects the insert or update and does not store the data.
'''
# Example
# Invalid data → operation fails ❌


'''
Q9. What is the SQL equivalent of MongoDB schema validation concepts?
Ans. MongoDB schema rules map closely to SQL constraints.
'''
# Example
# NOT NULL  → required
# CHECK     → minimum / maximum
# ENUM      → enum


'''
Q10. What is the one-line takeaway?
Ans. JSON Schema Validation enforces structure in MongoDB while keeping flexibility.
'''
# Example (lock it 🔒)
# Flexible DB + basic rules = safe data
