from flask import Blueprint, render_template

from blueprint.users.utils_users import get_posts_by_user
from utils_global import abort_404

user_page = Blueprint('user_page', __name__)


@user_page.route('/users/<name>', methods=['GET'])
def user_feed(name):
    users_feed = get_posts_by_user(name)
    if len(users_feed) == 0:
        return abort_404()
    return render_template('user-feed.html', users_feed=users_feed)
