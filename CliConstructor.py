class CliConstructor(object):
    def __init__(self):
        self.top_level = {'help': 'print this menu', 'exit': 'quit programm'}
        self.func_array = {'help': self.cli_help}
        self.arg_array = {'help': False}

    def run_cli(self, prompt):
        import sys
        self.cli = ' '.lower()
        self.prompt = prompt

        while self.cli != 'exit':
            self.cli = str(input(self.prompt).lower())
            words = self.cli.split()

            try:
                if self.arg_array[self.cli]:
                    self.func_array[self.cli](self.arg_array[self.cli])
                else:
                    self.func_array[self.cli]()

            except:
                if self.cli == '' or self.cli == 'exit':
                    pass
                else:
                    print('Command not found')

        sys.exit('Graceful exit')

    def add_cli_item(self, name, description, parrent = False, func = False, args = False):
        self.name = name
        self.description = description
        self.parrent = parrent
        self.func = func
        self.args = args
        if type(self.args) is set:
            pass

        if not self.parrent:
            self.top_level[self.name] = self.description
            self.func_array[self.name] = self.func
            self.arg_array[self.name] = self.args

    def cli_return(self):
        pass

    def cli_help(self):
        for item in self.top_level:
            print(item, '\t\t', self.top_level[item])
