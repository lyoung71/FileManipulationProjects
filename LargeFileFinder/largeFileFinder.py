import os

def large_file_finder():
    path = input('Please enter a path')
    for root, dirs, files in os.walk(path):
        for file in files:
            my_path = os.path.join(root, file)
            if not os.path.exists(my_path):
                continue
            if os.path.getsize(my_path) > (100*1024*1024):  # files larger than 100mb
                print(f'''
                        File name: {file}
                        File size: {os.path.getsize(my_path)//1024//1024}MB
                        File path: {my_path}
                    ''')

large_file_finder()
