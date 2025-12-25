# ISODate("...Z")   -> Mongo shell date helper
# new Date("...Z")  -> JavaScript Date
# new Date()        -> current date & time

# All are stored as UTC Date internally

'''
Q1. Are `ISODate()` and `new Date()` different in MongoDB storage?
Ans. No. Both create the SAME MongoDB Date type and are stored as UTC milliseconds.
'''
# Example
ISODate("2024-10-18T18:30:00Z")
new Date("2024-10-18T18:30:00Z")
# Both → stored identically (UTC)


'''
Q2. What does `new Date("2024-10-18T18:30:00Z")` do?
Ans. It creates a JavaScript Date with explicit UTC time and MongoDB stores it in UTC.
'''
# Example
{ dob: new Date("2024-10-18T18:30:00Z") }


'''
Q3. What does `new Date()` (without arguments) do?
Ans. It captures the current system time and MongoDB stores it in UTC.
'''
# Example
{ createdAt: new Date() }
# Same idea as ISODate()


'''
Q4. When should you prefer `ISODate()` vs `new Date()`?
Ans. Use `ISODate()` in the Mongo shell and `new Date()` in applications (Node.js).
'''
# Example
# Shell → ISODate()
# App   → new Date()


'''
Q5. What happens if you store a date as a string?
Ans. It is stored as text, not a Date, which breaks sorting and comparisons.
'''
# Example
{ dob: "2024-10-18T18:30:00Z" }  # ❌ string, not Date


'''
Q6. What is the golden rule for dates in MongoDB?
Ans. Always store dates as Date type in UTC and convert to local time in the UI.
'''
# Example (lock it 🔒)
# Store → UTC Date
# Display → local timezone


'''
Q7. One-line takeaway?
Ans. `ISODate()` and `new Date()` are equivalent for storage; both save UTC Dates.
'''
