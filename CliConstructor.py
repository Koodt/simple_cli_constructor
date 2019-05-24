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
#                getattr(self, self.cli)()
                self.top_level[self.cli]
            except:
                pass

        sys.exit('Graceful exit')

    def add(self, name, description, parrent, func, arg):
        self.name = name
        self.description = description
        self.parrent = parrent
        self.func = func
        self.arg = arg

        if not self.parrent:
            self.top_level[self.name] = self.description
            self.top_level[self.cli] = self.func

    def help(self):
        for item in self.top_level:
            print(item, '\t\t', self.top_level[item])
