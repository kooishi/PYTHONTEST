prompt = "\nTell me something, and I will repeat to back to you:"
prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)
# 
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# The code in parrot.py is a combination of the code in rollercoaster.py and counting.py.

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)