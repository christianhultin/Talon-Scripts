from talon.voice import Context, Key
from ..imported.switcher import switch_app

ctx = Context('outlook', bundle='com.microsoft.Outlook')

ctx.keymap({
    'reply': Key('cmd-r'),
    'read': Key('cmd-t'),
    'reply all': Key('cmd-shift-r'),
    'send e-mail': Key('cmd-enter'),
    'clear flag': None,
    'next pain': Key('shift-ctrl-['),
    'pree.lv pain': Key('shift-ctrl-]'),
    'mark': Key('cmd-t'),
    'unread': Key('cmd-shift-t'),
    'dismiss outlook': [
        lambda m: switch_app(name='outlook'),
        Key('cmd-w'),
    ],

    # navigation
    'calendar': Key('cmd-2'),
    'mail': Key('cmd-1'),
})


'''
pack = Packages.register
  name: "custom outlook"
  applications: ["com.microsoft.Outlook"]
  description: "custom commands for outlook"

pack.commands
  "reply-to-email":
    spoken: "reply to e-mail"
    misspoken: 'reply email'
    description: "reply to email"
    enabled: true
    action: (input) ->
      @key 'r', 'command'
  "send-email":
    spoken: "send e-mail"
    description: "send email"
    enabled: true
    action: (input) ->
      @key 'enter', 'command'
  "clear-flag":
    spoken: "clear flag"
    description: "clear flag"
    enabled: true
    action: (input) ->
      @do 'os:openMenuBarPath', ['Message', 'Follow Up', 'Clear Flag']

pack.implement
  'object:previous': -> @key '[', 'control'
  'object:next': -> @key ']', 'control'
  'object:backward': -> @key '[', 'shift control'
  'object:forward': -> @key ']', 'shift control'
'''
