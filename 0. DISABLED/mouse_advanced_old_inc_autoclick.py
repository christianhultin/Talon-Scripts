# import time
# from time import sleep
# from talon import cron, ctrl, tap
# from talon.voice import Context, Key
# from user.utils import optional_numerals
# from user.utils import parse_words_as_integer, repeat_function, optional_numerals

# class AutoClick:
#     def __init__(self):
#         self.enable()
#         self.disable() # if present, by default it is disabled
#         self.job = None
#         self.last_move = None

#     def on_move(self, typ, e):
#         self.last_move = time.time()
#         if not self.job:
#             self.job = cron.interval('250ms', self.on_interval)

#     def on_interval(self):
#         seconds = 0.250 # Seconds before click when mouse have stopped
#         if time.time() - self.last_move > seconds:
#             ctrl.mouse_click()
#             cron.cancel(self.job)
#             self.job = None

#     def is_activated(self):
#         return self.is_active

#     def enable(self):
#         tap.register(tap.MMOVE, self.on_move)
#         self.is_active = True

#     def disable(self):
#         tap.unregister(tap.MMOVE, self.on_move)
#         self.is_active = False

#     def toggle(self):
#         if self.is_active:
#             self.disable()
#         else:
#             self.enable()

# auto_clicker = AutoClick()

# def toggle_auto_click(m):
#     global auto_clicker
#     auto_clicker.toggle()

# def move_mouse_relative(m):
#     direction_type = m._words[1].word
#     multiplier = 30
#     line_number = parse_words_as_integer(m._words[2:]) * multiplier
#     if line_number == None:
#         return
#     direction_vector = {
#         'up': (0, -1),
#         'right': (1, 0),
#         'down': (0, 1),
#         'left': (-1, 0)
#     }[direction_type]
#     current_position = ctrl.mouse_pos()
#     move_mouse_programmatically_without_auto_click(
#         current_position[0] + direction_vector[0] * line_number,
#         current_position[1] + direction_vector[1] * line_number
#     )

# def move_mouse_absolute(xPos, yPos):
#     def move_mouse_to_position(m):
#         move_mouse_programmatically_without_auto_click(xPos, yPos)
#     return move_mouse_to_position

# def move_mouse_programmatically_without_auto_click(xPos, yPos):
#     if auto_clicker.is_activated():
#         auto_clicker.disable()
#         ctrl.mouse_move(xPos, yPos)
#         sleep(0.5)
#         auto_clicker.enable()
#     else:
#         ctrl.mouse_move(xPos, yPos)

# mouse_scroll_mode = {
#     'LEFT': (220, 420),
#     'MIDDLE': (730, 420),
#     'RIGHT': (1240, 420)
# }

# current_mouse_scroll_mode = mouse_scroll_mode['MIDDLE']

# def scroll_mouse(direction, distance):
#     def scroll(m):
#         global current_mouse_scroll_mode
#         (x, y) = current_mouse_scroll_mode
#         if ctrl.mouse_pos() != (x, y):
#             if auto_clicker.is_activated():
#                 auto_clicker.disable()
#                 ctrl.mouse_move(x, y)
#                 ctrl.mouse_scroll(direction * distance, 0)
#                 sleep(0.5)
#                 auto_clicker.enable()
#             else:
#                 ctrl.mouse_move(x, y)
#                 ctrl.mouse_scroll(direction * distance, 0)
#         else:
#             ctrl.mouse_scroll(direction * distance, 0)
#     return scroll

# def change_mouse_scroll_mode(m):
#     global current_mouse_scroll_mode
#     global mouse_scroll_mode
#     mode = m._words[3].word.upper()
#     current_mouse_scroll_mode = mouse_scroll_mode[mode]
#     (x, y) = current_mouse_scroll_mode
#     move_mouse_programmatically_without_auto_click(x, y)

# def toggle_mouse_visibility(m):
#     if str(m._words[1]) == 'show':
#         ctrl.cursor_visible(True)
#         return
#     ctrl.cursor_visible(False)

# def scrollMe():
#     global scrollAmount
#     if scrollAmount:
#         ctrl.mouse_scroll(by_lines=False, y=scrollAmount / 10)

# # scrolling
# def startScrolling(m):
#     global scrollJob
#     scrollJob = cron.interval("60ms", scrollMe)

# def stopScrolling(m):
#     global scrollAmount, scrollJob
#     scrollAmount = 0
#     cron.cancel(scrollJob)

# def mouse_scroll(amount):
#     def scroll(m):
#         global scrollAmount
#         # print("amount is", amount)
#         if (scrollAmount >= 0) == (amount >= 0):
#             scrollAmount += amount
#         else:
#             scrollAmount = amount
#         ctrl.mouse_scroll(y=amount)

#     return scroll

# scrollAmount = 0
# scrollJob = None

# ctx = Context('mouse_advanced')

# keymap = {
#     # auto click
#     'clickify': toggle_auto_click,

#     # movement
#     'mouse (left | up | right | down)' + optional_numerals: move_mouse_relative,
    
#     # show / hide
#     'mouse (hide | show)': toggle_mouse_visibility,
    
#     # scrolling
#     'mouse mode (left | middle | right)': change_mouse_scroll_mode,
#     # 'mouse mode pop (laptop | wide)': change_mouse_pop_mode,
#     'skip': scroll_mouse(1, 600),
#     'skippy': scroll_mouse(1, 300),
#     'hip': scroll_mouse(-1, 600),
#     'hippie': scroll_mouse(-1, 300),
#     # '[scroll] (bottom | doomway)': lambda m: ctrl.mouse_scroll(10000, 0),
#     '[scroll] (bottom | doomway)': Key('cmd-down'),
#     # '[(scroll | go)] [to] (top | jeepway)': lambda m: ctrl.mouse_scroll(-10000, 0),
#     '[(scroll | go)] [to] (top | jeepway)': Key('cmd-up'),


#     # specific locations
#     'mouse pop': move_mouse_absolute(1860, 60),
#     'mouse outlook': move_mouse_absolute(1376, 881),

#     # scrolling
#     "wheel down": mouse_scroll(30),
#     "wheel down continuous": [mouse_scroll(30), startScrolling],
#     "wheel up": mouse_scroll(-30),
#     "wheel up continuous": [mouse_scroll(-30), startScrolling],
#     "wheel stop": stopScrolling,
# }
# ctx.keymap(keymap)