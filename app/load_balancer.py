# coding: utf-8

# from app.user import User
# from app.server import Server
# from app.logger import Logger


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
