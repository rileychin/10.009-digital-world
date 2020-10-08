from libdw import pyrebase

projectid = "replace me"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "replace me"
email = "replace me"
password = "replace me"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)

db = firebase.database()
root = db.child("/").get(user['idToken'])
print(root.key(), root.val())

age = db.child("age").get(user['idToken'])
print(age.key(), age.val())

facts = db.child("facts_about_me").get(user['idToken'])
print(facts.key(), facts.val())


facts = db.child("facts_about_me").child("1").get(user['idToken'])
print(facts.val())

name = db.child("name").get(user['idToken'])
print(name.key(), name.val())

# to create a new node with our own key
db.child("pie").set(3.14, user['idToken'])
# to update existing entry
db.child("pie").set(3.1415, user['idToken'])
db.child("love_dw").set(True, user['idToken'])
