import os
import shutil


def sort_files(path):
    '''sort files into folders'''
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_type = file.split('.')[-1]
            if not os.path.exists(os.path.join(path, file_type)):
                os.mkdir(os.path.join(path, file_type))
            shutil.move(os.path.join(path, file), os.path.join(path, file_type))


if __name__ == '__main__':
    sort_files('C:/Users/XxX/Downloads')

    