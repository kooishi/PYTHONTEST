# 8-1
def display_message():
    print("我学了函数")
# display_message()

# 8-2
def favorite_book(title):
    print("One of my favorite books is " + title.title())

# title = input("请输入你最喜欢的书名：")
# favorite_book(title)

# 8-3
def make_shirt(size = "L", message = "I love Python"):
    print("T-shirt size is " + size + ", message is " + message)

# make_shirt()

# 8-5
def describe_city(city_name, country='China'):
    print(city_name + " is in " + country)

cname = input("请输入城市名：")

ccountry = input("请输入国家名：")
describe_city(cname, ccountry)

