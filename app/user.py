# coding: utf-8


class User:
    def __init__(self):
        self.ttask = 5

    def __str__(self):
        return 'User'

    def __repr__(self):
        return 'User'

    def run_task(self):
        self.ttask -= 1

    def completed_task(self):
        if self.ttask > 0:
            return False
        return True
