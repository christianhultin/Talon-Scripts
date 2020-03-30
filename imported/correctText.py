from talon.voice import Context, Key, Str, press
from talon import clip, tap
from talon import cron
import time

# this is. a test.paragraph..it HasMore thanOne various.errors,in its capitalisation.. and...spacing? this script will attempt!to

context = Context('test')

def correctText():
    with clip.capture() as s:
        press('cmd-c')
    inputText = s.get()
    correctText = formatText(inputText)
    clip.set(correctText)
    press('cmd-v')

def formatText(inputText):
    correctText = ''
    uppern = True  # whether to capitalise the next character
    spacen = False  # whether to allow the next character to be a space
    spacenf = False  # Whether to force a space before the next character if one doesn't exist
    charPrevious = ''

    for index, charCurrent in enumerate(inputText):
        charNew = ''
        upper = uppern
        space = spacen

        if len(correctText) == 0:
            uppern = False
            if charCurrent == ' ':
                continue
            correctText = charCurrent.upper()
            continue

        if (charCurrent not in ' .') and spacenf and charPrevious in '.,!?':
            charNew += ' '
        spacenf = False

        if charCurrent.isupper() and charPrevious != ' ' and len(charNew) < 1:
            charNew += ' '

        if charCurrent in '.!?':
            while correctText[-1] == ' ':
                correctText = correctText[:-1]
            spacenf = True
            spacen = True
            uppern = True
            charNew += charCurrent

        elif charCurrent == ',':
            while correctText[-1] == ' ':
                correctText = correctText[:-1]
            spacen = True
            spacenf = True
            charNew += charCurrent

        elif charCurrent == ' ':
            if spacen:
                charNew += charCurrent
                spacen = False
            else:
                charNew = ''
        elif upper:
            charNew += charCurrent.upper()
            uppern = False
            spacen = True
        else:
            charNew += charCurrent.lower()
            spacen = True

        correctText += charNew
        charPrevious = charNew
    
    return correctText

def correctSelectedText(m):
    correctText()

def correctAllText(m):
    press('cmd-a')
    correctText()

keymap = {
    'correct text': correctSelectedText,
    'correct all text': correctAllText,
}

context.keymap(keymap)
