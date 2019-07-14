# coding: utf-8

from app.logger import Logger
from app.server import Server
from app.user import User


class LoadBalancer:
    def __init__(self):
        self.file = open('app/data/input1.txt', 'r')
        self.users_per_clock_ticks = [int(line.replace('\n', '')) for line in self.file.readlines()]
        self.file.close()

        self.servers = []
        self.clock_tick = 0
        self.total_cost = 0

    def start(self):
        """
        Função responsavel por rodar o Load Balance
        """
        ttask = 5
        while self.clock_tick < (len(self.users_per_clock_ticks) + ttask):

            if self.clock_tick < len(self.users_per_clock_ticks) and self.users_per_clock_ticks[self.clock_tick] > 0:
                self.user_manager(self.users_per_clock_ticks[self.clock_tick])

            for server in self.servers:
                server.run_tasks()

            self.balance_servers()

            for server in self.servers:
                if server.users_online() == 0:
                    self.servers.remove(server)

            self.sum_cost()
            self.log_line()
            self.clock_tick += 1

        Logger(f'Total Cost: ${format(self.total_cost, ".2f")}' + '\n' * 2)

    def user_manager(self, user_count):
        """
        Coloca os usuários em servidores existentes, se os servidores existentes não derem conta e sobrar usuários,
        cria-se mais servidores

        Parameters
        ----------
        user_count: Numero de usuários

        """

        remaining_users = self.add_user_to_existent_server(user_count)

        if remaining_users > 0:
            self.add_user_to_new_server(remaining_users)

    def add_user_to_existent_server(self, user_count):
        """
        Para cada servidor, enquanto ele estiver disponivel e existir usuarios, o usuario é adicionado

        Parameters
        ----------
        user_count: Numero de usuarios

        Returns
        -------
        Numero de usuarios remanescentes

        """
        for server in self.servers:
            while server.available_server() is True and user_count > 0:
                server.add_user(User())
                user_count -= 1
        return user_count

    def add_user_to_new_server(self, user_count):
        """
        Cria-se um novo servidor, enquanto ele estiver disponível e existir usuários, um novo usuario é adicionado

        Parameters
        ----------
        user_count: Numero de usuarios

        Returns
        -------
        Numero de usuários remanescentes

        """
        server = Server()
        while server.available_server() is True and user_count > 0:
            server.add_user(User())
            user_count -= 1

        self.servers.append(server)
        return user_count

    def balance_servers(self):
        """
        Função que realiza a distribuição de usuarios entre os servidores
        """
        for base_server in self.servers:
            if base_server.available_server() and base_server.users_online():
                for target_server in self.servers:
                    if target_server.users_online() and base_server != target_server:
                        if base_server.users_online() <= target_server.users_online():
                            for user in target_server.connected_users:
                                if base_server.add_user(user):
                                    target_server.remove_user(user)

    def sum_cost(self):
        """
        Função que soma o total gasto com servidores

        Returns
        -------
        Custo total em dólar
        """
        for server in self.servers:
            if server.users_online():
                self.total_cost += 1
        return self.total_cost

    def log_line(self):
        """
        Função que loga a linha no arquivo output.txt
        """
        line = ''
        for server in self.servers:
            line += str(server.users_online()) + ','
        line = line[:-1] + '\n'
        Logger(line)
