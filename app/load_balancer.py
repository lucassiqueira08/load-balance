# coding: utf-8
from app.server import Server
from app.user import User


class LoadBalancer:
    def __init__(self):
        # TODO: Não esquecer de mudar o arquivo para input1
        self.file = open('app/data/input2.txt', 'r')
        self.users_per_clock_ticks = [int(line.replace('\n', '')) for line in self.file.readlines()]
        self.file.close()

        self.servers = []
        self.clock_tick = 0
        self.total_cost = 0

    def start(self):

        # TODO: Não esquecer de trocar de 4 para 5
        while self.clock_tick < (len(self.users_per_clock_ticks) + 4):
            # Gerencia os usuarios
            if self.clock_tick < len(self.users_per_clock_ticks) and self.users_per_clock_ticks[self.clock_tick] > 0:
                self.user_manager(self.users_per_clock_ticks[self.clock_tick])

            # Roda as tasks para todos os servidores e retira usuarios que já executaram as tasks
            for server in self.servers:
                server.run_tasks()

            # Remover os servidores que não estão sendo utilizados
            for server in self.servers:
                if server.users_online() == 0:
                    self.servers.remove(server)

            # Remaneja os usuarios para liberar espaço
            self.balance_servers()

            # Faz o Log no arquivo
            # TODO: Faz o Log da Linha

            # Calcula o custo
            self.sum_cost()
            print('*' * 10 + '\n')

            # Passa o tempo
            self.clock_tick += 1

        # Calcula o custo total
        print('-' * 20)
        print(f'Total Cost: ${self.total_cost}')
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
        pass

    def sum_cost(self):
        print(f'Clock {self.clock_tick}')
        for server in self.servers:
            if server.users_online():
                self.total_cost += 1
            print(f'{server} - {server.users_online()}')
        return self.total_cost
