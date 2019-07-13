# coding: utf-8


class Server:
    def __init__(self):
        self.connected_users = []
        self.umax = 10

    def add_user(self, user):
        if len(self.connected_users) < self.umax:
            self.connected_users.append(user)
            return True
        return False

    def remove_user(self, user):
        self.connected_users.remove(user)

    def available_server(self):
        if self.umax - len(self.connected_users) > 0:
            return True
        return False

    def run_tasks(self):
        for user in self.connected_users:
            user.run_task()

            if user.completed_task():
                self.remove_user(user)
