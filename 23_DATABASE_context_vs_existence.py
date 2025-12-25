'''
Q1. What is the difference between context and existence in MongoDB?
Ans. Context is the name you’re pointing at; existence means data actually lives on disk.
'''
# Example
# school>        → context (name only)
# show dbs       → actual databases on disk

'''
Q2. Why does MongoDB separate context from existence?
Ans. To allow flexible scripting and future databases without forcing existence checks.
'''
# Example
# Scripts can safely do:
# use logs
# db.dropDatabase()
# even if logs never existed.

'''
Q3. What is the one-line rule to lock this concept?
Ans. MongoDB separates “context” from “existence”; you can be in a DB context even if the DB doesn’t exist.
'''
# Example (lock it 🔒)
# Prompt name ≠ real database
