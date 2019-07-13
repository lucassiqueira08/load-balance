# coding: utf-8
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

        while self.clock_tick < (len(self.users_per_clock_ticks) + 5):

            # Gerencia os usuarios
            if self.clock_tick < len(self.users_per_clock_ticks) and self.users_per_clock_ticks[self.clock_tick] > 0:
                self.user_manager(self.users_per_clock_ticks[self.clock_tick])

            # Roda as tasks para todos os servidores
            for server in self.servers:
                server.run_tasks()

            # Retira os usuarios que já executaram as tasks
            # Todo: Retirar os usuarios que já executarm as taskas

            # Remaneja os usuarios para liberar espaço
            # Todo: Remanejar usuarios para liberar espaço

            # Remover os servidores que não estão sendo utilizados
            # Todo: Remover os servidores que não estão sendo utilizados

            # Faz o Log no arquivo
            # TODO: Faz o Log da Linha

            # Passa o tempo
            self.clock_tick += 1

        # Calcula o custo total
        total_cost = self.calculate_total_cost()

        # Faz o log final com o valor do custo total
        # TODO: Faz o Log do custo total

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
            remaining_users = self.add_user_to_new_server(user_count)
            if remaining_users > 0:
                self.user_manager(remaining_users)

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
        server_num = len(self.servers)
        server = Server(server_num)
        while server.available_server() is True and user_count > 0:
            server.add_user(User())
            user_count -= 1

        self.servers.append(server)
        return user_count

    def calculate_total_cost(self):
        # TODO: Faz o calculo do valor total levando em conta que o preço do clock é $1.00
        return True
