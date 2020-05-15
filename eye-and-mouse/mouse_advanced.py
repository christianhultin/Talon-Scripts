import time
from time import sleep
from talon import cron, ctrl, tap
from talon.voice import Context, Key, press
from user.utils import optional_numerals
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

# MOVING MOUSE
def move_mouse_relative(m):
    direction_type = m._words[1].word
    multiplier = 50
    pixels_to_travel = parse_words_as_integer(m._words[2:]) * multiplier
    if pixels_to_travel == None:
        return
    direction_vector = {
        'up': (0, -1),
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0)
    }[direction_type]
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse_move(x + direction_vector[0] * pixels_to_travel,
                    y + direction_vector[1] * pixels_to_travel)

def move_mouse_absolute(xPos, yPos):
    def move_mouse_to_position(m):
        ctrl.mouse_move(xPos, yPos)
    return move_mouse_to_position

# SCROLLING
scrollAmount = 0
scrollJob = None

def scroll_mouse(direction=1, distanceY=0, distanceX=0):
    def scroll(m):
        numberOfTimes = parse_words_as_integer(m._words)
        if numberOfTimes == None:
            numberOfTimes = 1

        for i in range(0, numberOfTimes):
            ctrl.mouse_scroll(direction * distanceY, direction * distanceX)
    return scroll

def mouse_scroll(amount):
    def scroll(m):
        global scrollAmount
        if (scrollAmount >= 0) == (amount >= 0):
            scrollAmount += amount
        else:
            scrollAmount = amount
        ctrl.mouse_scroll(y=amount)

    return scroll

##Autoscrolling
def scrollMe():
    global scrollAmount
    if scrollAmount:
        ctrl.mouse_scroll(by_lines=False, y=scrollAmount / 10)


def startScrolling(m):
    global scrollJob
    scrollJob = cron.interval("60ms", scrollMe)


def stopScrolling(m):
    global scrollAmount, scrollJob
    scrollAmount = 0
    cron.cancel(scrollJob)

##Smooth Scrolling
def mouse_smooth_scroll(amount):
    def scroll(m):
        total_time = 0.11
        interval = 0.007
        depth = int(total_time // interval)
        split = amount / depth
        numberOfTimes = parse_words_as_integer(m._words)
        if numberOfTimes == None:
            numberOfTimes = 1

        for i in range(0, numberOfTimes):
            for x in range(depth):
                ctrl.mouse_scroll(y=split)
                time.sleep(interval)

    return scroll


# OTHER
def mouse_install(m):
    move_mouse_absolute(1860, 92)(m)
    ctrl.mouse_click(pos=(None, None), button=0, times=1)
    sleep(0.3)
    press('down')
    sleep(0.3)
    press('down')
    sleep(0.3)
    press('down')


def toggle_mouse_visibility(m):
    if str(m._words[1]) == 'show':
        ctrl.cursor_visible(True)
        return
    ctrl.cursor_visible(False)


ctx = Context('mouse_advanced')

keymap = {
    # movement
    'mouse (left | up | right | down)' + optional_numerals: move_mouse_relative,

    # show / hide
    'mouse (hide | show)': toggle_mouse_visibility,

    # specific locations
    'mouse pop': move_mouse_absolute(1860, 60),
    'mouse outlook': move_mouse_absolute(1376, 881),
    'mouse (install | update)': mouse_install,

    # scrolling
    'skip' + optional_numerals: mouse_smooth_scroll(600),
    'skippy' + optional_numerals: mouse_smooth_scroll(300),
    'hip' + optional_numerals: mouse_smooth_scroll(-600),
    'hippie' + optional_numerals: mouse_smooth_scroll(-300),
    'skip right' + optional_numerals: scroll_mouse(1, distanceX=600),
    'skippy right' + optional_numerals: scroll_mouse(1, distanceX=300),
    'skip left' + optional_numerals: scroll_mouse(-1, distanceX=600),
    'skippy left' + optional_numerals: scroll_mouse(-1, distanceX=300),
    '(scroll | go) [to] (bottom | doomway)': Key('cmd-down'),
    '(scroll | go) [to] (top | jeepway)': Key('cmd-up'),

    # imported scrolling
    "wheel down": mouse_smooth_scroll(600),
    "wheel down continuous": [mouse_scroll(30), startScrolling],
    "wheel up": mouse_smooth_scroll(-600),
    "wheel up continuous": [mouse_scroll(-30), startScrolling],
    "wheel stop": stopScrolling,
}
ctx.keymap(keymap)
