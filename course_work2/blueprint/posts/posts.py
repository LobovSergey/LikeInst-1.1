

from flask import Blueprint, render_template, jsonify

from blueprint.posts.utils import get_post_by_pk, get_comments_by_post_id
from utils_global import get_posts_all, abort_404, abort_500

posts_page = Blueprint('posts', __name__)


@posts_page.route('/posts', methods=['GET'])
def main():
    data_json = get_posts_all()
    if data_json is None:
        return abort_500()
    return render_template('index.html', data_json=data_json)


@posts_page.route('/posts/<int:uid>', methods=['GET'])
def post(uid):
    posted = get_post_by_pk(uid)
    comments = get_comments_by_post_id(uid)
    if posted is None:
        return abort_404()
    return render_template('post.html', posted=posted, comments=comments)


@posts_page.route('/api/posts')
def api_json_all():
    posts_api = get_posts_all()
    if posts_api is None:
        return abort_500()
    return jsonify(posts_api)


@posts_page.route('/api/posts/<int:uid>')
def api_json_post(uid):
    posts_api = get_post_by_pk(uid)
    if posts_api is None:
        return abort_404()
    return jsonify(posts_api)


