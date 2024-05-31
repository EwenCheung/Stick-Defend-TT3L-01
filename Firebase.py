import pyrebase

class Data:
    def __init__(self):
        self.username = "Guest"
        self.stage_level = 1
        self.money = 0
        self.troop_storage = {
            "warrior": [True, 1],
            "archer": [False, 1],
            "wizard": [False, 1],
            "sparta": [False, 1],
            "giant": [False, 1]
        }
        self.spell_storage = {
            "rage": [False, 1],
            "healing": [False, 1],
            "freeze": [False, 1]
        }
        self.castle_storage = {
            "default_castle": [False, 1, 1]  # two upgrades
        }

    def read_data(self):
        all_data = {
            "username": self.username,
            "stage_level": self.stage_level,  # can be list if you want else just integer
            "money": self.money,  # money that the user has
            "troop_storage": self.troop_storage,
            "spell_storage": self.spell_storage,
            "castle_storage": self.castle_storage,
        }
        return all_data


firebase = Data()
# print(firebase.read_data())
# firebase.username = "Ewen"
# print(firebase.read_data())


""" 以上信息是可以用改用增 等。。。
    如果你们要
    
    读信息：
    print(firebase.read_data())
    上面那个代码可以read 给你们知道 user 的实时信息
    
    改data ：
    firebase.username = "Ewen"
    firebase.stage_level = 1
    firebase.money = 1000
    # 如果你们要改storage （dictionary）
    Example： troop_storage["archer"] 的第一个 list variable 从 False 变True 可以这样
    firebase.troop_storage["archer"] = [True, 1] or firebase.troop_storage["archer"][0] = True
    
    还有什么东西自己msg 问我
"""








class FirebaseSetup:
    def __init__(self):
        self.firebaseConfig = {
            "apiKey": "AIzaSyBLS9T81kZgfIPhwHVykobtrh_Axu9Cvwg",
            "authDomain": "stick-defend.firebaseapp.com",
            "projectId": "stick-defend",
            "storageBucket": "stick-defend.appspot.com",
            "messagingSenderId": "556800375894",
            "appId": "1:556800375894:web:fe7c4468de816789258ff7",
            "measurementId": "G-GXZZTHEC67",
            "databaseURL": "https://stick-defend-default-rtdb.asia-southeast1.firebasedatabase.app/"
        }

        firebase = pyrebase.initialize_app(self.firebaseConfig)

        self.db = firebase.database()
        self.auth = firebase.auth()
        self.username = "Guest"
        self.stage_level = 1
        self.money = 0
        self.troop_storage = {
            "warrior": [False, 1],
            "archer": [False, 1],
            "wizard": [False, 1],
            "sparta": [False, 1],
            "giant": [False, 1]
        }
        self.spell_storage = {
            "rage": [False, 1],
            "healing": [False, 1],
            "freeze": [False, 1]
        }
        self.castle_storage = {
            "default_castle": [False, 1, 1]  # two upgrades
        }
        self.user_id = ""
        self.user_email = ""

    def push_user_data(self, user_id, user_data):
        self.db.child("users").child(user_id).set(user_data)

    def update_user(self):
        """
        Example of troop storage:
        {'warrior': [(boolean - unlocked?), (integer - level_of_troop)],
        'archer': [(boolean - unlocked?), (integer - level_of_troop)]...}
        Same for spell_storage, castle_storage, and other_storage.
        """
        all_data = {
            "username": self.username,
            "stage_level": self.stage_level,  # can be list if you want else just integer
            "money": self.money,  # money that the user has
            "troop_storage": self.troop_storage,
            "spell_storage": self.spell_storage,
            "castle_storage": self.castle_storage,
        }

        users = self.db.child("users").get()
        for user in users.each():
            if user.key() == self.user_id:
                self.push_user_data(self.user_id, all_data)

    def read_data(self, user_data):
        self.username = user_data["username"]
        self.stage_level = user_data["stage_level"]
        self.money = user_data["money"]
        self.troop_storage = user_data["troop_storage"]
        self.spell_storage = user_data["spell_storage"]
        self.castle_storage = user_data["castle_storage"]

    def create_new_user(self):
        """
        Example of troop storage:
        {'warrior': [(boolean - unlocked?), (integer - level_of_troop)],
        'archer': [(boolean - unlocked?), (integer - level_of_troop)]...}
        Same for spell_storage, castle_storage, and other_storage.
        """
        self.username = input("Enter the username you want. : ")
        all_data = {
            "username": self.username,
            "stage_level": 1,
            "money": 0,
            "troop_storage": {
                "warrior": [False, 1],
                "archer": [False, 1],
                "wizard": [False, 1],
                "sparta": [False, 1],
                "giant": [False, 1]
            },
            "spell_storage": {
                "rage": [False, 1],
                "healing": [False, 1],
                "freeze": [False, 1]
            },
            "castle_storage": {"default_castle": [True, 1, 1]}
        }
        return all_data

    def sign_up(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        confirm_pass = input("Confirm your password: ")
        if password == confirm_pass:
            try:
                self.auth.create_user_with_email_and_password(email, password)
                print("Success! Now you can login with your email!")
                return None
            except Exception as e:
                print("Error:", e)
                return None
        else:
            print("Passwords do not match.")
            return None

    def sign_in(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        try:
            self.auth.sign_in_with_email_and_password(email, password)
            print("Successfully signed in!")
            return email
        except Exception as e:
            print("Invalid user or password. Try again. Error:", e)
            return None

    def ask_signing(self):
        user_email = None
        while True:
            ask = input("\nWould you like to sign in or sign up: ")
            if ask == "signin":
                user_email = self.sign_in()
            elif ask == "signup":
                self.sign_up()
            else:
                print("Invalid input, please type 'signin' or 'signup'.")
                continue

            if user_email is not None:
                break
        return user_email

    def run(self):
        self.user_email = self.ask_signing()

        print(f"User Email: {self.user_email}")
        self.user_id = self.user_email.replace("@", "_").replace(".", "_")
        users = self.db.child("users").get()
        for user in users.each():
            if user.key() == self.user_id:
                user_data = user.val()
                break
        else:
            user_data = self.create_new_user()
            self.push_user_data(self.user_id, user_data)
            print(f"User data has been pushed to the database under email {self.user_email}.")

        self.read_data(user_data)






#     ask_save = input("save?")
#     if ask_save == "yes":
#         update_user()


# here is the sample format of how data look like , you can use and modify the data with dictionary function
# username = "Ewen"
# stage_level = 5
# money = 1000
# troop_storage = {
#     "warrior": [True, 2],
#     "archer": [True, 3],
#     "wizard": [False, 1],
#     "sparta": [True, 1],
#     "giant": [False, 2]
# }
# spell_storage = {
#     "rage": [True, 1],
#     "healing": [True, 2],
#     "freeze": [False, 1]
# }
# castle_storage = {
#     "default_castle": [True, 1, 1]  # two upgrades
# }


# down dont border
# run()
# user_email = ask_signing()
# user_data = update_user(username, stage_level, money, troop_storage, spell_storage, castle_storage)
# push_user_data("123456_mail_com", user_data)