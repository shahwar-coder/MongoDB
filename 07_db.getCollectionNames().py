# > db.getCollectionNames()
# < ['students']

'''
db.getCollectionNames()
- Returns an array of all collections in the current database
- Programmatic version of `show collections`
- Shows only collections that actually exist
'''

# ============

'''QUESTIONS
Q1. How is `db.getCollectionNames()` different from `show collections`?
Ans. Both show the same information, but `db.getCollectionNames()` is used in code, while `show collections` is for humans.
'''
# Example
# show collections        → shell-friendly
# db.getCollectionNames() → programmatic

'''
Q2. Why is `db.getCollectionNames()` called a programmatic version?
Ans. Because it returns an array that can be used in scripts, conditions, or logic.
'''
# Example
# if ("students" in db.getCollectionNames()):
#     print("Collection exists")

'''
Q3. Which database does `db.getCollectionNames()` run on?
Ans. It runs on the CURRENT database context.
'''
# Example
# db
# Output: school
# db.getCollectionNames() → collections inside school only

'''
Q4. What does the output `['students']` tell you for sure?
Ans. It confirms that the `students` collection exists in the current database.
'''
# Example
# ['students'] → collection exists + has storage
