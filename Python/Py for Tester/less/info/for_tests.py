import os

for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path=}\n{dir_name=}\n{file_name=}\n')
