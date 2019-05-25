from CliConstructor import CliConstructor

def func(arg):
    print(arg)

def func_to(arg):
    print(arg)

local_cli = CliConstructor()
local_cli.add('add', 'adding element', None, func, 'Jjfmr')
local_cli.add('del', 'delete element', None, func_to, 'ChECK')
local_cli.add('list', 'list elements', None, func, 'sgdg')
local_cli.initial('my_cli>')
