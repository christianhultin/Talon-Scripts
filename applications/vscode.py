from talon import ctrl
from talon.voice import Context, Key, press, Str
from user.utils import repeat_function, optional_numerals, numerals, text_to_number

context = Context('VSCode', bundle='com.microsoft.VSCodeInsiders')
contextDS = Context('DataStudios', bundle='com.azuredatastudio.oss')


def jump_to_line(m):
    line_number = text_to_number(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press('cmd-g')
    Str(str(line_number))(None)
    press('enter')


def jump_tabs(m):
    line_number = text_to_number(m._words[1:])

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
    line_number_from = int(str(text_to_number(m._words[2:divider])))
    line_number_until = int(str(text_to_number(m._words[divider+1:])))
    number_of_lines = line_number_until - line_number_from

    press('cmd-g')
    Str(str(line_number_from))(None)
    press('enter')
    for i in range(0, number_of_lines+1):
        press('shift-down')


def fold_level(m):
    line_number = text_to_number(m._words)
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


keymap = {
    # Navigating text
    'line' + numerals: jump_to_line,

    # Selecting text
    'select line' + optional_numerals + 'until' + optional_numerals: select_lines_function,
    'select': Key('cmd-d'),
    'select instances': Key('cmd-shift-l'),
    'refactor': Key('f2'),
    'cursor up': Key('alt-cmd-up'),
    'cursor down': Key('alt-cmd-down'),

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
    'delete file': Key('cmd-backspace'),
    'toggle pane': Key('cmd-b'),
    'steffy' + optional_numerals: repeat_function('cmd-alt-left', 0.1),
    'steppy' + optional_numerals: repeat_function('cmd-alt-right', 0.1),
    'undo crack': Key('cmd-shift-t'),
    'crack other': Key('alt-cmd-t'),

    # special input defined i keybindings.json file, this is from a stackoverflow tip which emulates wim
    'navigate left': navigate_left,
    'navigate right': navigate_right,
    'navigate up': Key('ctrl-cmd-shift-k'),
    'navigate down': Key('ctrl-cmd-shift-j'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),

    # spacing
    'slap' + optional_numerals: [repeat_function('enter')],
    'slappy': [Key('esc'), Key('end enter')],
    'slippy': [Key('esc'), Key('home enter up')],
    '(stacy | spacey)': [Key('esc'), Key('enter enter up')],

    # editing
    'bracken': [Key('cmd-shift-ctrl-right')],
    '(delete line | snap)' + optional_numerals: repeat_function('cmd-shift-k'),
    '(snipper | clear line)': Key('cmd-right home cmd-shift-right delete'),
    # 'snipple': Key('end cmd-shift-left delete'),

    'snapple' + optional_numerals: repeat_function('down cmd-shift-k up cmd-left'),
    'indent': Key('alt-shift-f'),
    'line up' + optional_numerals: repeat_function('alt-up'),
    'line down' + optional_numerals: repeat_function('alt-down'),

    # various
    'cast': Key('cmd-shift-7'),
    '(arrange | fix) imports': Key('alt-shift-o'),
    'block comment': Key('alt-shift-a'),
    'master': Key('cmd-p'),
    'search all': Key('cmd-shift-f'),
    '(version | source) control': Key('ctrl-shift-g'),
    '(drop-down | drop)': Key('ctrl-space'),
    'quickfix': Key('cmd-.'),
    '(go to | find) definition': Key('cmd+i'),
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),
    '(edit file | pin tab)': Key('a cmd-z'),
    'Split editor': [Key('ctrl-cmd-alt-shift-7'), navigate_right],
    '(merge | join) editor[s]': [Key('cmd-shift-p'), 'Join All Editor Group\n'],
    'reload window': [Key('cmd-shift-p'), 'Reload window\n'],
    'execute': Key('cmd-enter'),

    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold level' + optional_numerals: fold_level,
}

context.keymap(keymap)
contextDS.keymap(keymap)
