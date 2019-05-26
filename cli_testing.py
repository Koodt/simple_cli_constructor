from CliConstructor import CliConstructor

def func(arg):
    print(arg)

def func_too(arg):
    print(arg)

local_cli = CliConstructor()
local_cli.add_cli_item('add', 'adding element', None, func, 'Jjfmr')
local_cli.add_cli_item('del', 'delete element', None, func_too, {'de', 'defe'})
local_cli.add_cli_item('list', 'list elements', None, func, 'sgdg')
local_cli.run_cli('my_cli>')
