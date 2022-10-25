FILE_NAME = 'transmission.txt'

def open_file():
    file = open(FILE_NAME, 'r')
    return file.readline()


