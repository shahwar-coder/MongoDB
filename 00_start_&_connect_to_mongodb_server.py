'''
1. Terminal Home
'''

'''
2. Check if mongodb is there:
>> which mongodb
'''
# /usr/local/mongodb/mongodb-macos-aarch64--8.2.2/bin/mongod

'''
3. Start the server:
>> mongod --dbpath /usr/local/var/mongodb
'''
# ⚠️ Important
# - Keep this terminal open
# - This terminal = MongoDB server running

'''
4. Connect using MongoDB Compass
Open MongoDB Compass
Click New Connection
Keep URI as: mongodb://localhost:27017
Click Connect
'''

# Observe:
# You should see:
# admin
# config
# local

# ✅ MongoDB is now usable.
