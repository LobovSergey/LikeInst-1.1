from flask import Blueprint, request, render_template

from blueprint.search.utils_search import search_for_posts

search_page = Blueprint('search_page', __name__)


@search_page.route('/search', methods=['GET'])
def search():
    message = ''
    word = request.args.get('s')
    searched_posts = search_for_posts(word)
    if len(searched_posts) == 0:
        message = 'Таких постов нет'
    return render_template('search.html', word=word, searched_posts=searched_posts, message=message)
