# coding: utf-8


class Logger:
    def __init__(self, message):
        self.file_output = open('app/data/output.txt', 'a')
        self.file_output.write(message)
        self.file_output.close()
