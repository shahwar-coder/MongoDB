# > use school
# < switched to db school
  
# > show dbs
#   admin   40.00 KiB
#   config  96.00 KiB
#   local   72.00 KiB
    
# > db
# < school
    
# > db.createCollection("students")
# < { ok: 1 }
    
# > db.students.insertOne({name: "Rahul", age: 51})
# < {
#   acknowledged: true,
#   insertedId: ObjectId('693fcf19d4efc530b134b40c')
#   }

# > show dbs
# < admin   40.00 KiB
#   config  36.00 KiB
#   local   72.00 KiB
#   school  40.00 KiB

'''
1. use school
   - Switches context to "school"
   - Does NOT create the database

2. show dbs
   - Shows only databases that have data
   - "school" not shown yet

3. db
   - Confirms current database context is "school"

4. db.createCollection("students")
   - Creates the collection
   - Triggers actual database creation

5. db.students.insertOne({ name: "Rahul", age: 51 })
   - Inserts data into the collection
   - Database is now persisted

6. show dbs
   - "school" database is now visible
'''
