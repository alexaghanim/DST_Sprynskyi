import os
import sys

print("There's commands list: ")
commands = ['ping', 'echo', 'login', 'exit']
print(', '.join(map(str, commands)))
while True:
    command = input('Input your command: ')
    if command == 'exit':
        sys.exit(0)
    parameter = input("Input command parameters:")
    if command == 'ping':
        os.system('ping'+' ' + parameter)
    if command == 'echo':
        os.system('echo'+' ' + parameter)
    if command == 'dir':
        os.system('dir'+' ' + parameter)
    if command == 'exit':
        os.system('exit'+' ' + parameter)
    if command == 'login':
        input("Enter your username: ")
        input("Enter your password: ")

