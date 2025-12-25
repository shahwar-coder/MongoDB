# > db.students.insertOne({name: "Raju", age: 19, course: "BCA"})
# < {
#   acknowledged: true,
#   insertedId: ObjectId('694d15dc1833d77e6b0add8c')
# }
# > students


# > db.students.find()
# < {
#   _id: ObjectId('694d15dc1833d77e6b0add8c'),
#   name: 'Raju',
#   age: 19,
#   course: 'BCA'
# }
# school>


'''
MongoDB JSON Schema Validation — Key Points

- Validation is applied at the COLLECTION level
- validator.$jsonSchema defines the rules
- required[] → fields that must exist in every document
- properties → rules for each field

- bsonType is enforced strictly (MongoDB checks BSON, not JS)
- "int" ≠ "double" → NumberInt matters
- minimum / maximum → numeric range checks
- enum → restricts values to a fixed set

- Invalid inserts/updates are REJECTED
- Valid data is stored normally
- MongoDB stays flexible but prevents bad data

- Validation happens at WRITE time, not READ time
'''
