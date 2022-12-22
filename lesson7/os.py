import os

print(f"username: {os.name}")
print(f"username in terminal: {os.getlogin()}")
print('list of files and folders in the current directory:')
dirs = os.listdir(path='.')
for file in dirs:
    print(file)