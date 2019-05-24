class CliConstructor(object):
    def __init__(self, prompt):
        import sys

        self.cli = ''.lower()
        self.prompt = prompt

        while self.cli != 'exit':
            self.cli = input(self.prompt).lower()
            try:
                getattr(self, self.cli)()
            except:
                if self.cli != 'exit':
                    print('Command not found')

        sys.exit('Graceful exit')
