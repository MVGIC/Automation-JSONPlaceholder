import allure
import pytest

from schemas.album import AlbumBody
from schemas.comment import CommentBody
from schemas.photo import PhotoBody
from schemas.post import PostBody
from schemas.todo import TodoBody


class TestNestedRoutes:

    @allure.id("8")
    @allure.title("Проверка получения комментариев к первому посту")
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_first_post_comments(self, get_first_post_comments_fixture):
        """
        Проверка получения комментариев к первому посту.
        """
        with allure.step("Получаем комментарии"):
            assert get_first_post_comments_fixture().assert_status_code(200).validate(CommentBody)


    @allure.id("9")
    @allure.title("Проверка получения фотографий первого альбома")
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_first_album_photos(self, get_first_album_photos_fixture):
        """
        Проверка получения фотографий первого альбома.
        """
        with allure.step("Получаем фотографии"):
            assert get_first_album_photos_fixture().assert_status_code(200).validate(PhotoBody)


    @allure.id("10")
    @allure.title("Проверка получения альбомов первого пользователя")
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_first_user_albums(self, get_first_user_albums_fixture):
        """
        Проверка получения альбомов первого пользователя.
        """
        with allure.step("Получаем альбомы"):
            assert get_first_user_albums_fixture().assert_status_code(200).validate(AlbumBody)


    @allure.id("11")
    @allure.title("Проверка получения списка дел первого пользователя")
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_first_user_todos(self, get_first_user_todos_fixture):
        """
        Проверка получения списка дел первого пользователя.
        """
        with allure.step("Получаем список дел"):
            assert get_first_user_todos_fixture().assert_status_code(200).validate(TodoBody)


    @allure.id("12")
    @allure.title("Проверка получения постов первого пользователя")
    @pytest.mark.regression
    @pytest.mark.api
    def test_get_first_user_posts(self, get_first_user_posts_fixture):
        """
        Проверка получения постов первого пользователя.
        """
        with allure.step("Получаем посты"):
            assert get_first_user_posts_fixture().assert_status_code(200).validate(PostBody)
