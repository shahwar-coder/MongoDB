'''
db.createCollection("students", {
  validator: {
    $jsonSchema: {
      title: "Student Object Validation",
      required: ["name", "age", "course"],
      properties: {
        name: {
          bsonType: "string",
          description: "Name must be a string and is required"
        },
        age: {
          bsonType: "int",
          minimum: 5,
          maximum: 20,
          description: "Age must be an integer and is required"
        },
        course: {
          bsonType: "string",
          enum: ["BCA", "BTech", "BSc"],
          description: "Name must be a string and is required"
        }
      }
    }
  }
})

< { ok: 1 }
'''
