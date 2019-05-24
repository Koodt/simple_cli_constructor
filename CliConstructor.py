class CliConstructor(object):
    def __init__(self):
        self.top_level = {'help': 'print this menu', 'exit': 'quit programm'}

    def initial(self, prompt):
        import sys

        self.cli = ''.lower()
        self.prompt = prompt

        while self.cli != 'exit':
            self.cli = input(self.prompt).lower()
            try:
                getattr(self, self.cli)()
            except:
                pass

        sys.exit('Graceful exit')

    def help(self):
        for item in self.top_level:
            print(item, '\t\t', self.top_level[item])
