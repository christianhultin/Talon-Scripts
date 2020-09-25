from user.utils import parse_words_as_integer, repeat_function, optional_numerals
from talon.voice import Key, Context


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
    'go home': ['cd ~/'],
    'go talon': ['cd ~/.talon/user'],
    'go developer': ['cd ~/Developer'],
    'go two point you': ['cd ~/Developer/TwoPointYou/'],
    'go feedback': ['cd ~/Developer/Netlight/FrontEnd/feedback-client'],
    'go sales client': ['cd ~/Developer/Netlight/FrontEnd/sales-client'],
    'go sales backend': ['cd ~/Developer/Netlight/BackEnd/sales-api'],
    'go (lough | laugh)': ['cd ~/Developer/Netlight/FrontEnd/laf-client'],
    'go galaxy': ['cd ~/Developer/milkywire/galaxy'],
    'go voyager': ['cd ~/Developer/milkywire/voyager'],
    'go (policy | bossy)': ['cd ~/Developer/milkywire/bosse'],
    'go milky': ['cd ~/Developer/milkywire'],
    'go up': ['cd ..'],

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
    'start (application | this | frontend)': ['npm run start\n'],
    'start galaxy': ['npm run dev -- -s -m'],
    '(start | run) ios': ['npm run ios:dev'],
    '(start | run) android': ['npm run android:dev'],
    'start (mocked | mock)': ['npm run start:mockedBackend'],
    '(start | run) backend': ['SPRING_PROFILES_ACTIVE=development ./gradlew bootRun\n'],
    'test (application | this | frontend)': ['npm run test'],
    'test settings': ['npm run setup:dev'],
    'node install': ['npm i\n'],
    'generate': ['npm run generate\n'],

    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': 'ls -a\n',
    'search': Key('ctrl-r'),
    'slap': Key('enter'),

    # Git
    'add': ['git add '],
    'add all': ['git add .'],
    'commit': ["git commit -m ''", Key('left')],
    'amend': ["git commit --amend"],
    'simple commit': ["git add .  && git commit -m 'update'  && git push"],
    'clone': ['git clone ', Key('cmd-v')],
    'push up': ['git push'],
    'status': ['git status\n'],
    '(difference | did | dave)': 'git diff\n',
    'pull down': ['git pull\n'],
    '(pull origin) | (origin master)': ['git pull origin master'],
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
    'remove untracked files': 'git clean -f',

    # Docker
    'doc': 'docker',
    'doc status': 'docker ps -a',
    'doc images': 'docker images',
    'doc volumes': 'docker volume ls',
    'doc volume prune': 'docker volume prune',
    'doc system prune': 'docker system prune -a',
    'doc compose': ['docker-compose up -d'],
    'doc compose down': ['docker-compose down'],

    # Knex:
    '( neck | nick ) migrate': 'knex migrate:latest',
    '( neck | nick ) rollback': 'knex migrate:rollback',
    '( neck | nick ) rollback all': 'knex migrate:rollback --all',
    '( neck | nick ) migrate (create | make)': 'knex migrate:make ',
}

ctx.keymap(keymap)
