# Списки з даними
# list = [5, 7, 2, 6, 8, 'Hello', True]
# numbers[0] = 555
# print(numbers[5])

# nums = [5, 3, 7, 5, 9]

# print(nums[-1][-2])
# numbers.append(58) # додає елемент
# numbers.insert(1, False) # додає елемент відносно вказаного індекса
# numbers.extend(nums) # додає список
# nums.sort() # сортує список
# nums.reverse() # сортує на спадання
# numbers.pop() # видаляє останій елемент
# numbers.remove(8) # видаляє конкретний елемент
# nums.clear() #видаляє список
# print(nums.count(8)) # шукає елемент
# print(len(nums)) # довжина списка
# print(numbers)

# Списки та цикли

# nums = [1, 6, 5, 9, 8, 3, 2]
# for el in nums:
#     res = el ** 2
#     print(res)


# user_count_hobby = int(input("Enter hobby number: "))

# i = 0
# hobby = []
# while i < user_count_hobby:
#     text = "Enter hobby" + str(i + 1) + ":"
#     hobby.append(input(text))
#     i += 1

# print(hobby)

# transactions = [120, 350, 90, 560, 40, 800, 150]
# total = 0
# n = 0
# small = []

# for i in transactions:
#     total += i
#     if i > 200:
#         n += 1
#     if i <= 150:
#         small.append(i)

# print(n)
# print(small)
# print(total)
# print(len(transactions))


# temps = [18, 22, 25, 19, 30, 15, 27]

# print(max(temps))
# print(min(temps))
# temps.sort()
# print(temps)
# print(any(t > 28 for t in temps))
# print(all(t > 10 for t in temps))
# print(any(t == 19 for t in temps))

week_temps = [
    [18, 22, 25],
    [19, 30, 15],
    [27, 21, 23]
]

count = 0
for day in week_temps:
    for temp in day:
        count += 1

print(count)

max_temp = week_temps[0][0] #береться перший елементи списку, та шукається більший елемент
for day in week_temps:
    for temp in day:
        if temp > max_temp:
            max_temp = temp

print(max_temp)