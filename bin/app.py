import web
from web.template import ALLOWED_AST_NODES

from dungeon_crawl.dungeon import dungeon
from dungeon_crawl.monsters.player import Player

ALLOWED_AST_NODES.append('Constant')

web.config.debug = False

urls = (
    '/game', 'GameEngine',
    '/', 'Index'
)

game_globals = {'room': None, 'player': None}

app = web.application(urls, globals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store)

render = web.template.render('templates/', base="layout", globals=game_globals)


class Index(object):
    def GET(self):
        session.room = dungeon.start_point
        return render.hello_form()

    def POST(self):
        form = web.input(name="Player")
        session.player = Player(form.name)
        return render.index(name=form.name, player=session.player)


class GameEngine(object):
    def GET(self):
        render
        return "Start Game"

    def POST(self):
        pass


if __name__ == "__main__":
    app.run()
