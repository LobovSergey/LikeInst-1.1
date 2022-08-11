from flask import Flask, redirect, url_for

from blueprint.posts.posts import posts_page
from blueprint.search.search_file import search_page
from blueprint.users.user_file import user_page
from utils_global import logger, abort_404, abort_500

logger()

app = Flask(__name__)
app.register_blueprint(posts_page)
app.register_blueprint(search_page)
app.register_blueprint(user_page)

app.config['JSON_AS_ASCII'] = False


@app.route('/')
def redirected():
    return redirect(url_for('posts.main'), code=302)


@app.errorhandler(404)
def abort(error):
    return abort_404()


@app.errorhandler(500)
def abort(error):
    return abort_500()


if __name__ == "__main__":
    app.run(host='127.0.0.3', port=8000, debug=True)
