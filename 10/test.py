'''
filename = 'learning_python.txt'

with open(filename) as f:
    contents = f.read()
    print(contents)

print("\n")

with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n")

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

with open(filename) as f:
    contents = f.read()

print(contents.replace('Python', 'C'))

'''

# message = input("Please enter a message: ")
filename = 'guest.txt'
# with open(filename, 'w') as f:
#     f.write(message)

while True:
    name = input("Please enter your name: ")
    if name == 'q':
        break
    else:
        message = input("Please enter a wish: ")
        with open(filename, 'a') as f:
            f.write(name + ": " + message + "\n")