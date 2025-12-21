import requests
from pytest import fixture

from baseclasses.response import Response
from constants.url import BASE_URL


@fixture()
def get_all_posts_fixture():
    return get_all_posts


def get_all_posts():
    response = requests.get(url=f"{BASE_URL}/posts")
    return Response(response)


@fixture()
def get_first_post_comments_fixture():
    return get_first_post_comments


def get_first_post_comments():
    response = requests.get(url=f"{BASE_URL}/posts/1/comments")
    return Response(response)


@fixture()
def get_first_album_photos_fixture():
    return get_first_album_photos


def get_first_album_photos():
    response = requests.get(url=f"{BASE_URL}/albums/1/photos")
    return Response(response)


@fixture()
def get_first_user_albums_fixture():
    return get_first_user_albums


def get_first_user_albums():
    response = requests.get(url=f"{BASE_URL}/users/1/albums")
    return Response(response)


@fixture()
def get_first_user_todos_fixture():
    return get_first_user_todos


def get_first_user_todos():
    response = requests.get(url=f"{BASE_URL}/users/1/todos")
    return Response(response)


@fixture()
def get_first_user_posts_fixture():
    return get_first_user_posts


def get_first_user_posts():
    response = requests.get(url=f"{BASE_URL}/users/1/posts")
    return Response(response)
