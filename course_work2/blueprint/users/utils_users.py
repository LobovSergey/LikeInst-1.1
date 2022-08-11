from utils_global import get_posts_all


def get_posts_by_user(user_name):
    users_post = [post for post in get_posts_all() if user_name == post['poster_name']]
    return users_post
