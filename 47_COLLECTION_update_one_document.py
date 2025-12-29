# Commands ran by me...
# 1️⃣ Switching database
# > use school
# switched to db school
# > db
# school


# 2️⃣ Creating collection
# > db.createCollection("student2")
# { ok: 1 }


# 3️⃣ insertMany()
# > db.students2.insertMany([
#     {
#         "name": "Shahid Kapoor",
#         "age": 20,
#         "class": "BSc",
#         "skills": ["HTML", "Python", "JavaScript"]
#     },
#     {
#         "name": "Aisha Khan",
#         "age": 22,
#         "class": "BTech",
#         "skills": ["Python", "Django", "MongoDB"]
#     },
#     {
#         "name": "Rahul Verma",
#         "age": 21,
#         "class": "BCA",
#         "skills": ["C", "C++", "Data Structures"]
#     },
#     {
#         "name": "Sara Ali",
#         "age": 23,
#         "class": "MSc",
#         "skills": ["Machine Learning", "Python", "NumPy"]
#     },
#     {
#         "name": "Arjun Mehta",
#         "age": 24,
#         "class": "MCA",
#         "skills": ["Node.js", "Express", "MongoDB"]
#     }
# ])
# <{
#   acknowledged: true,
#   insertedIds: {
#     '0': ObjectId('695266f059b327ea6f973ebe'),
#     '1': ObjectId('695266f059b327ea6f973ebf'),
#     '2': ObjectId('695266f059b327ea6f973ec0'),
#     '3': ObjectId('695266f059b327ea6f973ec1'),
#     '4': ObjectId('695266f059b327ea6f973ec2')
#   }
# }


# 4️⃣ find()
# > db.students2.find()
# <{
#   _id: ObjectId('695266f059b327ea6f973ebe'),
#   name: 'Shahid Kapoor',
#   age: 20,
#   class: 'BSc',
#   skills: [
#     'HTML',
#     'Python',
#     'JavaScript'
#   ]
# }
# {
#   _id: ObjectId('695266f059b327ea6f973ebf'),
#   name: 'Aisha Khan',
#   age: 22,
#   class: 'BTech',
#   skills: [
#     'Python',
#     'Django',
#     'MongoDB'
#   ]
# }
# {
#   _id: ObjectId('695266f059b327ea6f973ec0'),
#   name: 'Rahul Verma',
#   age: 21,
#   class: 'BCA',
#   skills: [
#     'C',
#     'C++',
#     'Data Structures'
#   ]
# }
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


# 5️⃣ updateOne()
# > db.students2.updateOne(
#     { _id: ObjectId('695266f059b327ea6f973ebe') },
#     { $set: { name: "SHAHID KAPOOR", age: 44, class: "B Tech", skills: ["DevOps", "AWS", "GenAI"] } }
# )
# <{
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }


'''
updateOne(filter, update)
- filter → which document
- update → uses operators ($set, $inc, etc.)

$set
- Updates only specified fields
- Keeps rest of document intact

matchedCount → how many matched
modifiedCount → how many changed
'''
