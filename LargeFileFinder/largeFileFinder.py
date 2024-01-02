import os


def large_file_finder():
    path = input('Please enter a path')
    for root, dirs, files in os.walk(path):
        for file in files:
            my_path = os.path.join(root, file)
            if not os.path.exists(my_path):
                raise Exception(f'{my_path} does not exist or can\'t be located.')
            if os.path.getsize(my_path) > (100*1024*1024):  # files larger than 100mb
                print(f'''
                        File name: {file}
                        File size: {os.path.getsize(my_path)//1024//1024}MB
                        File path: {my_path}
                    ''')


try:
    large_file_finder()
except Exception as err:
    print(str(err))
