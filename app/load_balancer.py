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


class User:
    def __init__(self):
        self.ttask = 5

    def run_task(self):
        self.ttask -= 1

    def completed_task(self):
        if self.ttask > 0:
            return False
        return True


class Logger:
    def __init__(self, message):
        self.file_output = open('app/data/output.txt', 'a')
        self.file_output.write(message)
        self.file_output.close()


class LoadBalancer:
    def __init__(self):
        self.file = open('app/data/input2.txt', 'r')
        self.users_per_clock_ticks = [int(line.replace('\n', '')) for line in self.file.readlines()]
        self.file.close()

        self.servers = []
        self.clock_tick = 0
        self.total_cost = 0

    def start(self):
        while True:
            pass
            # TODO: Faz o Log da Linha
        # TODO: Faz o Log do custo total

    def calculate_total_cost(self):
        pass


