import json
from typing import Any

from utils_global import get_posts_all


def get_posts_by_user(user_name):
    try:
        post_list = []
        for post in get_posts_all():
            if post['poster_name'] == user_name.lower():
                post_list.append(post)
        return post_list

    except ValueError:
        return 'Empty value'


def get_comments_by_post_id(post_id):
    try:
        list_comments = []
        with open('static/data/comments.json', 'r', encoding='utf-8') as file:
            for comment in json.load(file):
                if comment['post_id'] == post_id:
                    list_comments.append(comment)
            return list_comments

    except ValueError:
        return


def get_post_by_pk(pk) -> Any | None:
    for post in get_posts_all():
        if post['pk'] == pk:
            return post

