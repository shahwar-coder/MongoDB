'''
1. Go to MongoDB official website
>> https://www.mongodb.com/

2. Go to Products > Community Edition

3. Click Download Community > Select the Package > Download

4. Go to Downloads folder and Extract the tgz file,
you will see the folder having binary files

5. Open Terminal

6. Go to Downloads (where tgz and extracted folder exist)
>> cd Downloads

7. Check if files are there in Downloads
>> ls -la | egrep "mongodb|tgz"

8. Create Target folder (here binaries will live)
>> sudo mkdir -p /usr/local/mongodb

9. Move Extracted MongoDB folder to new main folder we just created
>> sudo mv mongodb-macos-*/ /usr/local/mongodb

10. Check if the file(s) came in the main created folder
>> ls /usr/local/mongodb

11. Check what’s inside the bin folder
(You should see: mongod, mongos, install_compass)
>> ls /usr/local/mongodb/mongodb-macos-aarch64--8.2.2/bin

12. Add MongoDB BIN to your PATH permanently
>> echo 'export PATH=/usr/local/mongodb/mongodb-macos-aarch64--8.2.2/bin:$PATH' >> ~/.zshrc
>> source ~/.zshrc

13. Verify PATH works (should show actual path, not "not found")
>> which mongod

14.
# Create MongoDB DATA DIRECTORY (REQUIRED)
# macOS prevents writing to /data/db, so use:
# /usr/local/var/mongodb
>> sudo mkdir -p /usr/local/var/mongodb
>> sudo chown -R $USER /usr/local/var/mongodb

15. Verify the data directory exists
>> ls -ld /usr/local/var/mongodb

16. Run the server:
>> mongod --dbpath /usr/local/var/mongodb

17. Go to MongoDB website, Products > Tools > MongoDB Compass
and Download suitable package for your system.
(Compass includes mongosh shell built-in, 
but if you want a standalone command-line shell, 
install it via: brew install mongosh)

18. Go to downloads, open the dmg file (that was downloaded),
drag the mongodb compass icon to Applications folder, 
now it will be in Applications

19. MongoDB server (mongod, the daemon) 
must stay running in the terminal. Do not close this tab.

20. Open the MongoDB Compass -> Create new connection,
you can keep default URI : mongodb://localhost:27017

21. Then you see admin, config, local options after the connection is made
'''
