import allure

from schemas.album import AlbumBody
from schemas.comment import CommentBody
from schemas.photo import PhotoBody
from schemas.post import PostBody
from schemas.todo import TodoBody


class TestNestedRoutes:

    def test_get_first_post_comments(self, get_first_post_comments_fixture):
        with allure.step(""):
            assert get_first_post_comments_fixture().assert_status_code(200).validate(CommentBody)

    def test_get_first_album_photos(self, get_first_album_photos_fixture):
        with allure.step(""):
            assert get_first_album_photos_fixture().assert_status_code(200).validate(PhotoBody)

    def test_get_first_user_albums(self, get_first_user_albums_fixture):
        with allure.step(""):
            assert get_first_user_albums_fixture().assert_status_code(200).validate(AlbumBody)

    def test_get_first_user_todos(self, get_first_user_todos_fixture):
        with allure.step(""):
            assert get_first_user_todos_fixture().assert_status_code(200).validate(TodoBody)

    def test_get_first_user_posts(self, get_first_user_posts_fixture):
        with allure.step(""):
            assert get_first_user_posts_fixture().assert_status_code(200).validate(PostBody)
