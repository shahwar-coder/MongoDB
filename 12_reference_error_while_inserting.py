# > db.users.insertOne({name: "Rahul", age: 51, city: Delhi})
# ReferenceError: Delhi is not defined

'''
ReferenceError happened because:
- mongosh uses JavaScript
- Unquoted words are treated as variables
- "Delhi" must be a string, not an identifier
'''
