# 3-4

# List = ['wang', 'qian', 'li', 'zhao']
# print(List)

# 3-5
# print(List[1].title() + " is cannot come to dinner.")
# List[1] = 'sun'
# print(List)

# 3-6
# print("I found a bigger table.")

# List.insert(0, 'zhou')
# List.insert(2, 'wu')
# List.append('zheng')
# print(List)

# 3-7
# print("I can only invite two people to dinner.")
# print("Sorry, " + List.pop() + ", I can't invite you to dinner.")
# print("Sorry, " + List.pop() + ", I can't invite you to dinner.")
# print("Sorry, " + List.pop() + ", I can't invite you to dinner.")
# print("Sorry, " + List.pop() + ", I can't invite you to dinner.")
# print("Sorry, " + List.pop() + ", I can't invite you to dinner.")
# print(List)
# print("You are still invited to dinner, " + List[0] + ".")
# print("You are still invited to dinner, " + List[1] + ".")


# 3-8
# travel = ['beijing', 'shanghai', 'guangzhou', 'shenzhen', 'chengdu']
# print(travel)
# print(sorted(travel))
# print(travel)
# print(sorted(travel, reverse=True))
# print(travel)
# travel.reverse()
# print(travel)
# travel.reverse()
# print(travel)
# travel.sort()
# print(travel)
# travel.sort(reverse=True)
# print(travel)

# 3-9
# print(len(travel))

# 4-1
# pizzas = ['pepperoni', 'cheese', 'sausage', 'mushroom', 'onion', 'green pepper']
# for pizza in pizzas:
#     print(pizza.title() + " pizza is delicious!")
# print("Ireally love piza!")

# 4-2

# animals = ['dog', 'cat', 'rabbit']
# for animal in animals:
#     print("A " + animal + " would make a great pet.")
# print("Any of these animals would make a great pet!")

# 4-3
# for value in range(1, 21):
#     print(value, end=", ")

# 4-4
# num = list(range(1, 1000001))
# for value in num:
#     print(value, end=" ")
# print("\n")

# 4-5
# num = list(range(1, 1000001))
# print(min(num))
# print(max(num))
# print(sum(num))

# 4-6
# even_numbers = list(range(1, 21, 2))
# for value in even_numbers:
#     print(value, end=" ")
# print("\n")

# 4-7
# threes = list(range(3, 31, 3))
# for value in threes:
#     print(value, end=" ")

# 4-8
# cubes = []
# for value in range(1, 11):
#     cubes.append(value ** 3)
# for cube in cubes:
#     print(cube, end=" ")

# 4-9
# cubes = list(value ** 3 for value in range(1, 11))
# for cube in cubes:
#     print(cube, end=" ")

