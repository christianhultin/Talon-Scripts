from talon.voice import Context, Key, Str
from ..utils import alternatives, parse_word

ctx = Context('words')


last_word = None
def shrink_word(m):
    word = str(m._words[1])
    if not word in shrink_map:
        last_word = word
        raise Exception('%s not in shrink map' % word)
    Str(shrink_map[word])(None)


shrink_map = {
    'administrator': 'admin',
    'alternate': 'alt',
    'apartment': 'apt',
    'applications': 'apps',
    'arguments': 'args',
    'attributes': 'attrs',
    'authentication': 'auth',
    'button': 'btn',
    'command': 'cmd',
    'compute': 'cmp',
    'context': 'ctx',
    'concatenate': 'concat',
    'configure': 'config',
    'control': 'ctrl',
    'format': 'fmt',
    'image': 'img',
    'jason': 'json',
    'message': 'msg',
    'package': 'pkg',
    'parameter': 'param',
    'source': 'src',
    'standard': 'std',
    'temporary': 'tmp',
    'text': 'txt',
    'user': 'usr',
    'user id': 'uid',
    'utilities': 'utils',
    'user': 'usr',
    'error': 'err',
    'boolean': 'bool',
    'return': 'ret',
    'package': 'pkg',
    'python': 'py',
    'random': 'rand',
    'frequency': 'freq',
    'operations': 'ops',
    'initialize': 'init',
    'iterator': 'iter',
    'vector': 'vec',
    'convolution': 'conv',
    'deconvolution': 'deconv',
    'derivative': 'deriv',
    'distribution': 'dist',
    'contribute': 'contrib',
    'delete': 'del',
    'different': 'diff',
    'square root': 'sqrt',
    'sequence': 'seq',
    'predict': 'pred',
    'ending': 'end',
    'yaml': 'yml',
    'condition': 'cond',
    'validation': 'val',
    'optimization': 'opt',
    'generator': 'gen',
    'memory': 'mem',
    'environments': 'envs',
    'environment': 'env',
    'application': 'app',

    "inc.": "inc",
    "_c": "char",
    "administrator": "admin",
    "administrators": "admins",
    "allocate": "alloc",
    "alternate": "alt",
    "apartment": "apt",
    "application": "app",
    "applications": "apps",
    "architecture": "arch",
    "argument": "arg",
    "arguments": "args",
    "attribute": "attr",
    "attributes": "attrs",
    "authentic": "auth",
    "authenticate": "auth",
    "author": "auth",
    "binary": "bin",
    "button": "btn",
    "calculate": "calc",
    "call": "col",
    "car": "char",
    "care": "char",
    "certificate": "cert",
    "character": "char",
    "column": "col",
    "command": "cmd",
    "concatenate": "concat",
    "configuration": "config",
    "configure": "config",
    "constant": "const",
    "define": "def",
    "descending": "desc",
    "develop": "dev",
    "developer": "dev",
    "development": "dev",
    "directory": "dir",
    "divider": "div",
    "document": "doc",
    "environment": "env",
    "execute": "exec",
    "extend": "ext",
    "extension": "ext",
    "favorite": "fav",
    "function": "func",
    "image": "img",
    "imager": "int",
    "incorporate": "inc",
    "increment": "inc",
    "initialize": "init",
    "integer": "int",
    "iterate": "iter",
    "jason": "json",
    "language": "lang",
    "large": "lg",
    "latitude": "lat",
    "length": "len",
    "library": "lib",
    "locate": "loc",
    "location": "loc",
    "longitude": "lng",
    "medium": "md",
    "minimum": "min",
    "miscellaneous": "misc",
    "navigate": "nav",
    "navigation": "nav",
    "number": "num",
    "object": "obj",
    "parameter": "param",
    "parameters": "params",
    "position": "pos",
    "previous": "prev",
    "production": "prod",
    "pseudo": "sudo",
    "reference": "ref",
    "references": "refs",
    "repeat": "rep",
    "request": "req",
    "result": "res",
    "revision": "rev",
    "source": "src",
    "standard": "std",
    "standing": "stdin",
    "standout": "stdout",
    "string": "str",
    "system": "sys",
    "temporary": "tmp",
    "text": "txt",
    "thanks": "thx",
    "utilities": "utils",
    "utility": "util",
    "value": "val",
    "variable": "var",
    
    # months,
    "january": "jan",
    "february": "feb",
    "march": "mar",
    "april": "apr",
    "june": "jun",
    "july": "jul",
    "august": "aug",
    "september": "sept",
    "october": "oct",
    "november": "nov",
    "december": "dec",
    'dictionary': 'dict',
}

ctx.keymap({
    'shrink' + alternatives(shrink_map.keys()): shrink_word,
})
