from utils_global import get_posts_all


def search_for_posts(query):
    posts = get_posts_all()
    list_searched = [post for post in posts if query in post['content']]
    print(list_searched)
    return list_searched

