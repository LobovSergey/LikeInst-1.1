from blueprint.posts.utils import *


def test_one():
    assert type(get_post_by_pk(1)) == dict


def test_two():
    assert type(get_post_by_pk(100)) is None
