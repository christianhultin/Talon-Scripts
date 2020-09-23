from talon.voice import Context, Rep, talon, generic
from user.utils import parse_words_as_integer


class MyRep(generic):
    def __call__(self, m):
        tmp = []
        if self.ctx.last_action:
            for action, rule in self.ctx.last_action:
                for i in range(self.data):
                    act = action(rule) or (action, rule)
                tmp.append(act)
        return tmp


ctx = Context('repeater')


def repeat(m):
    repeat_count = parse_words_as_integer(m._words[1:])

    if repeat_count != None and repeat_count >= 1:
        repeater = MyRep(repeat_count)
        repeater.ctx = talon
        return repeater(None)


ctx.keymap({
    'wink': MyRep(1),
    'soup': MyRep(2),
    'trace': MyRep(3),
    'quarr': MyRep(4),
    'fypes': MyRep(5),
    'repeat (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': repeat,
    # Ordinals
    'first': MyRep(1),
    'second': MyRep(1),
    'third': MyRep(2),
    'fourth': MyRep(3),
    'fifth': MyRep(4),
    'sixth': MyRep(5),
    'seventh': MyRep(6),
    'eighth': MyRep(7),
    'ninth': MyRep(8),
    'tenth': MyRep(9),
    'eleventh': MyRep(10),
    'twelfth': MyRep(1),
    'thirteenth': MyRep(12),
    'fourteenth': MyRep(13),
    'fifteenth': MyRep(14),
    # '1': MyRep(1),
    # '2': MyRep(1),
    # '3': MyRep(2),
    # '4': MyRep(3),
    # '5': MyRep(4),
    # '6': MyRep(5),
    # '7': MyRep(6),
    # '8': MyRep(7),
    # '9': MyRep(8),
    # '10': MyRep(9),
    # '11': MyRep(10),
    # '12': MyRep(1),
    # '13': MyRep(12),
    # '14': MyRep(13),
    # '15': MyRep(14),
})
