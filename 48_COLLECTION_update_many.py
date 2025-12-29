# 1️⃣ updateMany()
# > db.students2.updateMany(
#     { class: { $in: ["BTech", "BSc"] } },
#     { $inc: { age: 1 } }
# )

# Output:

# {
#   acknowledged: true,
#   insertedId: null,
#   matchedCount: 1,
#   modifiedCount: 1,
#   upsertedCount: 0
# }

'''
Here it would have updated more than one documents, but it happened so that none had class as Bsc and BTech, shahid had B Tech others had Msc etc...
'''



# 2️⃣ find() with $in
# > db.students2.find({ class: { $in: ["BTech", "BSc"] } })

# {
#   _id: ObjectId('695266f059b327ea6f973ebf'),
#   name: 'Aisha Khan',
#   age: 23,
#   class: 'BTech',
#   skills: [
#     'Python',
#     'Django',
#     'MongoDB'
#   ]
# }

# school>


'''
updateMany(filter, update)
- Updates all matching documents
- Uses operators like $set, $inc
- matchedCount → how many matched
- modifiedCount → how many updated
'''
