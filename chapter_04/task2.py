# Цикл while
# i = 100
# while i >= 10:
#     print(i)
#     i -= 10

#Практичне використання

# work = True
# while work:
#     user_input = input('Enter word STOP: ')
#     if user_input == 'STOP':
#         work = False
# print('While loop is done')

#вгадай число
i = 7
while True:
    user_input = int(input("Enter the number: "))
    if user_input == i:
        print("Correct! 🎉")
        break
    elif user_input < i:
        print("Too low!")
    else:
        print("Too high!")