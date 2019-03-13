from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

context = Context('VSCode', bundle='com.microsoft.VSCode')


def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press('cmd-g')
    Str(str(line_number))(None)
    press('enter')


def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    for i in range(0, line_number):
        press('cmd-alt-right')


def jump_to_next_word_instance(m):
    press('escape')
    press('cmd-f')
    Str(' '.join([str(s) for s in m.dgndictation[0]._words]))(None)
    press('return')


def select_lines_function(m):
    divider = 0
    for word in m._words:
        if str(word) == 'until':
            break
        divider += 1
    line_number_from = int(str(parse_words_as_integer(m._words[2:divider])))
    line_number_until = int(str(parse_words_as_integer(m._words[divider+1:])))
    number_of_lines = line_number_until - line_number_from

    press('cmd-g')
    Str(str(line_number_from))(None)
    press('enter')
    for i in range(0, number_of_lines+1):
        press('shift-down')


def fold_level(m):
    line_number = parse_words_as_integer(m._words)
    if line_number > 9:
        return
    press('cmd-k')
    press('cmd-' + str(line_number))

context.keymap({
    # Navigating text
    'line' + optional_numerals: jump_to_line,

    # Selecting text
    'select line' + optional_numerals + 'until' + optional_numerals: select_lines_function,

    # Finding text
    'find': Key('cmd-f'),
    'find all': Key('cmd-shift-f'),
    'find next <dgndictation>': jump_to_next_word_instance,

    # Clipboard
    'clone': Key('alt-shift-down'),
    'cut line': Key('end cmd-shift-left cmd-x backspace'),
    'copy line': Key('end cmd-shift-left cmd-c'),

    # Navigation
    'Go to line': Key('cmd-g'),
    'go bracket': [Key('cmd-alt-shift-b')] * 2,
    'explorer': Key('cmd-shift-e'),
    'extensions': Key('cmd-shift-x'),
    'open file': Key('cmd-down'),
    'toggle pane': Key('cmd-b'),

    # special input defined i keybindings.json file, this is from a stackoverflow tip which emulates wim 
    'navigate left': Key('ctrl-cmd-shift-h'),
    'navigate right': Key('ctrl-cmd-shift-l'),
    'navigate up': Key('ctrl-cmd-shift-k'),
    'navigate down': Key('ctrl-cmd-shift-j'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),

    # editing
    'bracken': [Key('cmd-shift-ctrl-right')],
    '(delete line | snap)' + optional_numerals: repeat_function('cmd-shift-k'),
    'snapple' + optional_numerals: repeat_function('down cmd-shift-k up cmd-left'),
    'select instances': Key('cmd-shift-l'),
    'indent': Key('alt-shift-f'),
    'line up' + optional_numerals: repeat_function('alt-up'),
    'line down' + optional_numerals: repeat_function('alt-down'),

    # various
    'comment': Key('cmd-shift-7'),
    'master': Key('cmd-p'),
    'search all': Key('cmd-shift-f'),
    '(version | source) control': Key('ctrl-shift-g'),
    '(drop-down | drop)': Key('ctrl-space'),
    '(go to | find) definition': Key('f12'),
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),
    '(edit file | pin tab)': Key('a cmd-z'),
    'Split editor': Key('ctrl-cmd-alt-shift-7'),
    '(merge | join) editor[s]': [Key('cmd-shift-p'), 'Join All Editor Group\n'],

    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold level' + optional_numerals: fold_level,
})
