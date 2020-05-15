from talon.voice import Context, ctrl
from talon import ui
import time
import os

running = {}
launch = {}


def lookup_app(m=None, name=None):
    if isinstance(m, str):
        name = m
    elif name is None:
        name = str(m["switcher.running"][0])

    full = running.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            return app


def switch_app(m=None, name=None):
    app = lookup_app(m=m, name=name)
    app.focus()
    # print(dir(app))
    # TODO: replace sleep with a check to see when it is in foreground
    time.sleep(0.25)
    move_mouse_to_center_of_application()

def move_mouse_to_center_of_application():
    x, y = ui.active_window().screen.rect.center
    offset = 300 
    ctrl.mouse_move(x, y+offset)

def launch_app(m=None, name=None):
    if m:
        name = str(m["switcher.launch"][0])
    elif not name:
        raise ValueError("must provide name or m")

    path = launch.get(name)
    if path:
        ui.launch(path=path)

def focus_simulator(m):
    apps = ui.apps(name="Simulator")
    for app in apps:
        app.focus()

ctx = Context("switcher")
ctx.keymap(
    {
        "(focus | fox) {switcher.running}": switch_app,
        "launch {switcher.launch}": launch_app,
        # custom switchers here
        "madam": lambda x: switch_app(x, "Atom"),
        "system preferences": lambda x: switch_app(x, "System Preferences"),
        "focus simulator": focus_simulator,
    }
)

hardcoded_application_names = {
    "terminal": "iTerm2",
    "ink": "Inkdrop",
    "key pass": "KeePassXC",
}


def update_lists():
    global running
    global launch
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(" ")
        for word in words:
            if word and word not in new:
                new[word] = app.name
        new[app.name] = app.name
    running = new
    running.update(hardcoded_application_names)
    ctx.set_list("running", running.keys())

    new = {}
    for base in "/Applications", "/Applications/Utilities":
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit(".", 1)[0]
            new[name] = path
            words = name.split(" ")
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word] = path
    launch = new
    ctx.set_list("launch", launch.keys())


def ui_event(event, arg):
    if event in ("app_activate", "app_launch", "app_close", "win_open", "win_close"):
        # print(event, arg)
        if event in ("win_open", "win_closed"):
            if arg.app.name == "Amethyst":
                return
        update_lists()


ui.register("", ui_event)
update_lists()