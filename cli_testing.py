from CliConstructor import CliConstructor


local_cli = CliConstructor()
local_cli.add('add', 'adding element')
local_cli.add('del', 'delete element')
local_cli.add('list', 'list elements')
local_cli.initial('my_cli>')
