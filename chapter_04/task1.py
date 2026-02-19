# Цикл for
# for i in range(-5, 16, 3):
#     print("El:", i)

# print("\n\n")

# word = 'Some text'
# for i in word:
#     print(i)


# таблиця множення
# user_input = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(f"{user_input} * {i} = {user_input * i}")


#Сума чисел
# n = int(input("Enter the number: "))
# total = 0
# for i in range(1, n + 1):
#     total += i
# print("Sum = ", total)


#Парні числа до n
# n = int(input("Enter the number: "))
# count = 0
# for i in range( 1, n+1):
#     if i % 2 == 0:
#         count += 1
#         print(i)
# print("Total even numbers:", count)


# Ділення на 3
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1, n+1):
#     if i % 3 == 0:
#         count += 1
#         print(i)
# print('Total numbers divisible by 3: ', count)

#Парні числа, кратні 5
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1, n+1):
#     if i % 2 == 0 and i % 5 == 0:
#         count += 1
#         print(i)
# print('Total numbers divisible by 2 and 5: ', count)


#Кратні 4, але не кратні 8
# n = int(input("Enter the number: "))
# count = 0
# for i in range(1, n+1):
#     if i % 4 == 0 and i % 8 != 0:
#         count += 1
#         print(i)
# print('Total numbers divisible by 4 but not by 8: ', count)


#Прості числа до n
# n = int(input("Enter the number: "))
# count = 0
# for i in range(2, n+1):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0 :
#             is_prime = False
#             break
#     if is_prime:
#         print(i)
#         count +=1
# print(f'Total prime numbers: {count}')