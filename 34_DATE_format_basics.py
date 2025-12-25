# ISODate("...Z")        -> UTC (recommended)
# ISODate("+02:00")     -> converted to UTC
# ISODate("-05:00")     -> converted to UTC
# ISODate("no zone")    -> uses local timezone (avoid)

# ========

'''
Q1. What is `ISODate` in MongoDB?
Ans. `ISODate` is MongoDB’s built-in Date type used to store date and time values.
'''
# Example
ISODate("2024-10-18T18:30:00Z")


'''
Q2. How does MongoDB store dates internally?
Ans. MongoDB stores all dates in UTC as milliseconds since the Unix epoch.
'''
# Example
# Stored internally → UTC milliseconds
# Timezone is NOT stored, only used for conversion


'''
Q3. What does the `Z` mean in `ISODate("...Z")`?
Ans. `Z` means UTC time (also called Zulu time).
'''
# Example
ISODate("2024-10-18T18:30:00Z")
# Explicit UTC → safest format


'''
Q4. What happens if a timezone offset like `+02:00` is used?
Ans. MongoDB converts the given time to UTC before storing it.
'''
# Example
ISODate("2024-10-18T18:30:00+02:00")
# Stored as → 16:30 UTC


'''
Q5. What happens with a negative offset like `-05:00`?
Ans. MongoDB again converts it to UTC internally.
'''
# Example
ISODate("2024-10-18T18:30:00-05:00")
# Stored as → 23:30 UTC


'''
Q6. What happens if no timezone is specified?
Ans. MongoDB treats the time as the local system timezone.
This can cause bugs.
'''
# Example
ISODate("2024-10-18T18:30:00")
# Uses machine’s local timezone ❌


'''
Q7. Why does MongoDB always use UTC?
Ans. UTC avoids timezone confusion, makes sorting correct, and works globally.
'''
# Example
# Servers in different countries → same stored time


'''
Q8. What is the golden rule when using dates in MongoDB?
Ans. Always store dates in UTC (`Z`) and convert to local time in the application.
'''
# Example (lock it 🔒)
db.users.insertOne({
    name: "Rahul",
    dob: ISODate("1995-06-15T00:00:00Z")
})
