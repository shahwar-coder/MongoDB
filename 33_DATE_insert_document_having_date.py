# > use office
# < switched to db office
# > show collections
# < employees
# > db.createCollection("departments")
# < { ok: 1 }
# > show collections
# < departments
#   employees
# > db.departments.insertOne({name: "DevOps", date_of_creation: ISODate("2012-06-15T00:00:00Z")})
# < {
#   acknowledged: true,
#   insertedId: ObjectId('694cc35a183d77e6b0add88')
# }
# office>

'''
use office
- Switches to office database

db.createCollection("departments")
- Creates a new collection

show collections
- Verifies existing collections

db.departments.insertOne({
  name: "DevOps",
  date_of_creation: ISODate("2012-06-15T00:00:00Z")
})
- Inserts a document with a UTC date field
'''

# Inserted one document into departments
# ISODate(...) stored as UTC Date
# MongoDB auto-added _id
# Database + collection are now persisted with data
# ✔️ This is the correct and recommended way to store dates.

