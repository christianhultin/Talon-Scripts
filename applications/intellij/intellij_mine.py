from time import sleep
from talon import ctrl
from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

context = Context('Intellij', bundle='com.jetbrains.intellij.ce')


def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press('cmd-l')
    Str(str(line_number))(None)
    sleep(0.5)
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

    press('cmd-l')
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


distance_to_navigate = 500


def navigate_right(m):
    press('ctrl-cmd-shift-l')
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x + distance_to_navigate, y)


def navigate_left(m):
    press('ctrl-cmd-shift-h')
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x - distance_to_navigate, y)


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
    'clone': Key('cmd-d'),
    'cut line': Key('end cmd-shift-left cmd-x backspace'),
    'copy line': Key('end cmd-shift-left cmd-c'),

    # Navigation
    'Go to line': Key('cmd-l'),
    'go bracket': [Key('cmd-alt-shift-b')] * 2,
    'explorer': Key('cmd-1'),
    'extensions': Key('cmd-shift-x'),
    'open file': Key('cmd-down'),
    'open': Key('cmd-shift-alt-ctrl-o'),
    'toggle pane': Key('cmd-1'),
    'steffy' + optional_numerals: repeat_function('cmd-alt-ctrl-shift-left', 0.1),
    'steppy' + optional_numerals: repeat_function('cmd-alt-ctrl-shift-right', 0.1),

    # special input defined i keybindings.json file, this is from a stackoverflow tip which emulates wim
    'navigate left': navigate_left,
    'navigate right': navigate_right,
    'navigate up': Key('ctrl-cmd-shift-k'),
    'navigate down': Key('ctrl-cmd-shift-j'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),

    # editing
    'bracken': [Key('alt-up')],
    '(delete line | snap)' + optional_numerals: repeat_function('cmd-backspace'),
    '(snipper | clear line)': Key('cmd-right home cmd-shift-right delete'),
    # 'snipple': Key('end cmd-shift-left delete'),

    'snapple' + optional_numerals: repeat_function('down cmd-backspace up cmd-left'),
    '(select instances) | refactor': Key('shift-f6'),
    'indent': Key('alt-shift-f'),
    'line up' + optional_numerals: repeat_function('alt-shift-up'),
    'line down' + optional_numerals: repeat_function('alt-shift-down'),

    # spacing
    'slap' + optional_numerals: [Key('esc'), repeat_function('enter')],
    'slappy': [Key('esc'), Key('end enter')],
    'slippy': [Key('esc'), Key('home enter up')],
    '(stacy | spacey)': [Key('esc'), Key('enter enter up')],

    # various
    '(comment | cast)': Key('ctrl-shift-7'),
    'hide (terminal | dock)': Key('cmd-4 shift-escape'),
    'block comment': Key('alt-shift-a'),
    'master': Key('cmd-shift-p'),
    'search all': Key('cmd-shift-f'),
    '(version | source) control': Key('ctrl-shift-g'),
    '(drop-down | drop)': Key('alt-space'),
    '(go to | find) definition': Key('cmd-b',),
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),
    '(edit file | pin tab)': Key('a cmd-z'),
    'Split editor': [Key('ctrl-cmd-alt-shift-7'), navigate_right],
    '(merge | join) editor[s]': Key('ctrl-cmd-alt-shift-8'),

    # IntelliJ specific
    'run (backend | application)': Key('ctrl-r'),
    'stop (backend | application)': Key('cmd-f2'),
    'run function': Key('ctrl-shift-r'),
    'run checkstyle': Key('ctrl-shift-alt-cmd-c'),

    'settings': Key('cmd-,'),
    'next file': Key('cmd-shift-ctrl-alt-right'),
    '(last | previous) file': Key('cmd-shift-ctrl-alt-left'),


    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold level' + optional_numerals: fold_level,
})
