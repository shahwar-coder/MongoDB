# > use people
# < switched to db people
# > db
# < people

# > db.createCollection("persons")
# < { ok: 1 }
# > show collections
# < persons

# db.persons.insertMany([
#   {
#     name: "Ali",
#     age: 25,
#     height: 5.9,
#     isMarried: false,
#     skills: ["Python", "MongoDB", "DSA"],
#     address: {
#       city: "Hyderabad",
#       country: "India",
#       pincode: 500001
#     },
#     joinedAt: new Date("2023-06-15"),
#     score: NumberInt(90),
#     salary: NumberLong(850000),
#     rating: null
#   },
#   {
#     name: "Fatima",
#     age: 28,
#     height: 5.4,
#     isMarried: true,
#     skills: ["Frontend", "React"],
#     address: {
#       city: "Bangalore",
#       country: "India",
#       pincode: 560001
#     },
#     joinedAt: new Date(),
#     score: NumberInt(95),
#     salary: NumberLong(1200000),
#     rating: 4.8
#   },
#   {
#     name: "Yusuf",
#     age: 32,
#     height: 6.1,
#     isMarried: true,
#     skills: [],
#     address: {
#       city: "Delhi",
#       country: "India",
#       pincode: 110001
#     },
#     joinedAt: new Date("2020-01-01"),
#     score: NumberInt(88),
#     salary: NumberLong(1500000),
#     rating: undefined
#   }
# ])

# < {
#   acknowledged: true,
#   insertedIds: {
#     '0': ObjectId('694cd43e183d77e6b0add89'),
#     '1': ObjectId('694cd43e183d77e6b0add8a'),
#     '2': ObjectId('694cd43e183d77e6b0add8b')
#   }
# }
# people>


'''
• insertMany() inserts multiple documents at once into the "persons" collection.
• Documents demonstrate common MongoDB data types:
  - String       → name, city, country
  - Int32        → age, score (NumberInt)
  - Double       → height, rating
  - Boolean      → isMarried
  - Array        → skills
  - Object       → address (embedded document)
  - Date         → joinedAt
  - Null         → rating
  - Int64 (Long) → salary (NumberLong)
'''


'''
⚠️ Issues & Caveats in the Given MongoDB Data

• NumberLong(850000)
  ❌ JS number passed to NumberLong
  ⚠️ MongoDB warns about possible precision loss
  ✅ Correct usage → NumberLong("850000")

• rating: undefined
  ❌ undefined is NOT stored in MongoDB
  ⚠️ Field will be omitted completely
  ✅ Use null if field presence is required

• Mixed data types for "rating"
  - null      → Ali
  - 4.8       → Fatima (Double)
  - undefined → Yusuf (field removed)
  ⚠️ Causes inconsistent schema
  ❗ Bad for queries, indexing, analytics

• height stored as Double
  ✅ Valid for measurements
  ⚠️ Floating-point precision issues possible
  ❗ Never use Double for money values

• pincode stored as Number
  ⚠️ Pin codes are identifiers, not numeric values
  ❗ Leading zeros can be lost
  ✅ Prefer String → "500001"

• joinedAt uses mixed date styles
  - Fixed date string → new Date("2023-06-15")
  - Current date     → new Date()
  ⚠️ Valid but may cause inconsistent test data

• skills: [] (empty array)
  ✅ Valid MongoDB data type
  ⚠️ $in, $size, $exists behave differently on empty arrays
  ℹ️ Awareness needed, not an error
'''
