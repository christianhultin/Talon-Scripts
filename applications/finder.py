from talon.voice import Key, Context, Str, press

def go_to_path(path):
	def path_function(m):
		press('cmd-shift-g')
		Str(path)(None)
		press('return')
	return path_function

ctx = Context('Finder', bundle='com.apple.finder')
ctx.keymap({
	# actions
    'duplicate': Key('cmd-d'),
	'collapse': Key('cmd-left'),
	'expand': Key('cmd-right'),
	'open': Key('cmd-down'),
	'(delete file) | (trash it)': Key('cmd-backspace'),
	'new folder': Key('cmd-shift-n'),
	'show package contents': Key('cmd-alt-o'),

	# navigation
	'[go] computer': Key('cmd-shift-c'),
	'[go] desktop': Key('cmd-shift-d'),
	'[go] all files': Key('cmd-shift-f'),
	'go to': Key('cmd-shift-g'),
	'[go] home': Key('cmd-shift-h'),
	'[go] icloud': Key('cmd-shift-i'),
	'[go] documents': Key('cmd-shift-o'),
	'[go] air drop': Key('cmd-shift-r'),
	'[go] utilities': Key('cmd-shift-u'),
	'[go] downloads': Key('cmd-shift-l'),
	'[go] applications': Key('cmd-shift-a'),
	'[go] developer': go_to_path('~/Developer'),
	'[go] talon': go_to_path('~/.talon/user'),
	'[go] pictures': go_to_path('~/Pictures'),
 })
