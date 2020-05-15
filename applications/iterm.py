from talon.voice import Key, Context
from user.utils import parse_words_as_integer, repeat_function, optional_numerals


def text(m):
    try:
        tmp = [str(s).lower() for s in m.dgndictation[0]._words]
        words = [parse_word(word) for word in tmp]
        Str(' '.join(words))(None)
    except AttributeError:
        return


ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    # shortcut projects:
    'cd home': ['cd ~/'],
    'cd talon': ['cd ~/.talon/user'],
    'cd developer': ['cd ~/Developer'],
    'cd two point you': ['cd ~/Developer/TwoPointYou/'],
    'cd feedback': ['cd ~/Developer/Netlight/FrontEnd/feedback-client'],
    'cd sales client': ['cd ~/Developer/Netlight/FrontEnd/sales-client'],
    'cd sales backend': ['cd ~/Developer/Netlight/BackEnd/sales-api'],
    'cd (lough | laugh)': ['cd ~/Developer/Netlight/FrontEnd/laf-client'],

    # iterm functionality
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    '(new tab | nippy)': Key('cmd-t'),
    'next pane': Key('ctrl-tab'),
    'steffy' + optional_numerals: repeat_function('ctrl-shift-tab', 0.1),
    'steppy' + optional_numerals: repeat_function('ctrl-tab', 0.1),
    'make (durr | dear) [<dgndictation>]': ['mkdir ', text],

    # shell scripts
    'restart voice recognition': ['restartTalonDragon'],
    'restart talon': ['restartOnlyTalon'],

    # package managers
    'start': ['npm run start\n'],
    '(start | run) ios': ['npm run ios:dev\n'],
    '(start | run) android': ['npm run android:dev\n'],
    'start mocked': ['npm run start:mockedBackend\n'],
    '(start | run) backend': ['SPRING_PROFILES_ACTIVE=development ./gradlew bootRun\n'],
    'test': ['npm run test\n'],
    'node install': ['npm i\n'],
    'generate': ['npm run generate\n'],

    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': 'ls -a\n',
    'search': Key('ctrl-r'),

    # Git
    'add': ['git add '],
    'add all': ['git add .'],
    'commit': ["git commit -m ''", Key('left')],
    'simple commit': ["git add .  && git commit -m 'update'  && git push"],
    'clone': ['git clone '],
    'push up': ['git push'],
    'status': ['git status\n'],
    '(difference | did | dave)': 'git diff\n',
    'pull down': ['git pull\n'],
    '(pull origin) | (origin master)': ['git pull origin master\n'],
    '[remote] add upstream': ['git remote add upstream'],
    'fetch upstream': ['git fetch upstream'],
    'fetch': ['git fetch\n'],
    'remote': ['git remote -v'],
    'check out': ['git checkout '],
    'merge': ['git merge '],
    'stash': ['git stash\n'],
    'stash pop': ['git stash pop\n'],
    'log': ['git log\n'],
    'reset hard': ['git reset --hard'],
    'go (to) master': ['git checkout master\n'],
    'reload submodule': ['git submodule deinit -f . && git submodule update --init'],

    # Docker
    'docker componse': ['docker-compose -f docker-compose-env.yml up -d'],
}

ctx.keymap(keymap)
