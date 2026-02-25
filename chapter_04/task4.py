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

users = {
    "admin": "1234",
    "tanya": "qwerty",
    "guest": "0000"
}

login = input("Login: ")
password = input("Password: ")

if login in users:
    if users[login] == password:
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("User not found")