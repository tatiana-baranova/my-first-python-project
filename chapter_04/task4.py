# Else в циклі
# for i in "Hello world":
#     if i == "l":
#         print("Done")
#         break
# else:
#     print("Not found")

# numbers = [4, 8, 15, 16, 23, 42]

# for i in numbers:
#     if i == 15:
#         print("Found")
#         break
# else:
#         print("Not found number")


# products = ["milk", "bread", "eggs", "apple"]
# search = input("Enter the product: ").lower()
# for item in products:
#     if item == search:
#         print("Product in list")
#         break
# else:
#     print("Product is missing")

# users = ["admin", "tanya", "guest", "manager"]
# login = input("Enter the login: ").lower()
# for user in users:
#     if user == login:
#         print("Access is allowed")
#         break
# else:
#     print("User not found")

# users = {
#     "admin": "1234",
#     "tanya": "qwerty",
#     "guest": "0000"
# }

# login = input("Login: ")
# password = input("Password: ")

# if login in users:
#     if users[login] == password:
#         print("Login successful")
#     else:
#         print("Incorrect password")
# else:
#     print("User not found")


users = [
    { "id": "01",
    "username": "Alisa",
    "password": 123456,
    "role": "admin"} 
    ,
    {"id": "02",
    "username": "Lui",
    "password": 456789,
    "role": "user"} 
    ,
    {"id": "03",
    "username": "Ron",
    "password": 987654,
    "role": "user"}
    ,
    {"id": "04",
    "username": "Mark",
    "password": 456123,
    "role": "user"}
]
username = input("Username: ")
password = int(input("Password: "))
user = next((u for u in users if u["username"] == username), None)

if user is None: 
    print("User not found")
elif user["password"] != password:
    print("Incorrect password")
else:
    print("Access allowed")