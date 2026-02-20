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
# i = 7
# while True:
#     user_input = int(input("Enter the number: "))
#     if user_input == i:
#         print("Correct! 🎉")
#         break
#     elif user_input < i:
#         print("Too low!")
#     else:
#         print("Too high!")


#Лічильник до n
# n = int(input("Enter the number: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1


#Сума чисел
# total = 0
# while True:
#     n = int(input("Enter the number (0 to stop):"))
#     if n == 0:
#         break
#     total += n
#     print("Total sum", total)


# months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',' September', 'October', 'November', 'December']
# i = 0
# while i < len(months):
#     if months[i] =='December':
#         break
#     print(months[i])
#     i +=1
