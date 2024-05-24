import urllib.request

import pyrebase

firebaseConfig = {"apiKey": "AIzaSyBLS9T81kZgfIPhwHVykobtrh_Axu9Cvwg",
                  "authDomain": "stick-defend.firebaseapp.com",
                  "projectId": "stick-defend",
                  "storageBucket": "stick-defend.appspot.com",
                  "messagingSenderId": "556800375894",
                  "appId": "1:556800375894:web:fe7c4468de816789258ff7",
                  "measurementId": "G-GXZZTHEC67",
                  "databaseURL": "https://stick-defend-default-rtdb.asia-southeast1.firebasedatabase.app/"}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
# auth = firebase.auth()
# storage = firebase.storage()

# Authentication
# login
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# try:
#     auth.sign_in_with_email_and_password(email, password)
#     print("Successfully signed in! ")
# except:
#     print("Invalid user or password. Try again")

# # Signup
# email = input("Enter your email: ")
# password = input("Enter your password: ")
# confirmpass = input("Confirm your password: ")
# if password == confirmpass:
#     try:
#         auth.create_user_with_email_and_password(email,password)
#         print("Success! ")
#     except:
#         print("Email already exists")


# Storage
# upload file
# filename = input("Enter the name of the file you want to upload: ")  # file upload to storage
# cloudfilename = input("Enter the name of the file on the cloud: ")  # what should i named it in storage
# storage.child(cloudfilename).put(filename)

# print(storage.child(cloudfilename).get_url(None))

# Download a file ( input book/poem/poem1.txt )
# cloudfilename = input("Enter the name of the file you want to download")
# storage.child(cloudfilename).download("", "download.txt")


# Database
# data = {"age": 40, "address": "NewYork", "employed": False, "name": "John"}
# db.push(data)
# db.child("users").push(data)
# db.child("users").child("example").push(data)
# # to have own id without using the unique id
# db.child("users").child("myownid").set(data)

# update info
# db.child("users").child("myownid").update({"name":"Jane"})

# get everything in child
# users = db.child("users").get()
# for user in users.each():
#     print(user.val())
#     print(user.key())
#     if user.val()['name']=="Jane":
#         print(user.val())
#         print(user.key())
#         db.child("users").child(user.key()).update({"name":"Jay"})
#         print(user.val())
#
# users = db.child("users").get()
# for user in users.each():
#     print(user.val())


# Remove
# db.child("users").child("myownid").remove()

# users = db.child("users").get()
# for user in users.each():
#     if 'name' in user.val() and user.val()['name']=="John":
#         db.child("users").child(user.key()).child("age").remove()


# Read
# users = db.child("users").get()
# print(users.val())

# users = db.child("users").order_by_child("name").equal_to("John").get()  # go rules change the index of, have to add in what you want to search
# for user in users.each():
#     print(user.val())
#     print(user.val()["employed"])

# users = db.child("users").order_by_child("age").equal_to(32).limit_to_last(1).get()  # go rules change the index of, have to add in what you want to search
# for user in users.each():
#     print(user.val())
#     print(user.val()["employed"])
#
# users = db.child("users").order_by_child("age").start_at(30).get()
# for user in users.each():
#     print(user.val())
#     print(user.val()["employed"])