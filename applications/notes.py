from talon.voice import Key, Context, Str, press
from talon import ctrl, tap

ctx = Context('Notes', bundle='com.apple.Notes')

def click_mouse(xPos,yPos):
    def click_mouse_function(m):
        ctrl.mouse_move(xPos, yPos)
        ctrl.mouse_click()
    return click_mouse_function

ctx.keymap({
    'navigate': [Key('cmd-1')] * 2,
    'navigate big': click_mouse(98, 98),
 })
