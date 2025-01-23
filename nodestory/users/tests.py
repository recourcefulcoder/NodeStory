from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from parameterized import parameterized

TEST_USERNAME = "new_user"
SIGNUP_REDIRECT_PAGE = reverse("homepage:index")


class UserTests(TestCase):
    fixtures = ["test_fixture.json"]

    @parameterized.expand(
        [
            ("admin", "admin"),
            ("farnaKK", "Hemaphoho54"),
            ("farMak", "Giggily15!"),
        ]
    )
    def test_login_correct(self, username, password):
        c = Client()
        c.login(username=username, password=password)
        self.assertIn("_auth_user_id", c.session)

    def test_non_auth_user_redirected(self):
        c = Client()
        self.assertRedirects(
            c.get(reverse("users:review")),
            f"{reverse('login')}?next={reverse('users:review')}",
        )

    def test_signup_creates_user(self):
        c = Client()
        c.post(
            reverse("users:signup"),
            {
                "username": TEST_USERNAME,
                "password1": "new_password",
                "password2": "new_password",
            },
        )
        self.assertTrue(
            get_user_model().objects.filter(username=TEST_USERNAME).exists()
        )

    def test_signup_redirects(self):
        c = Client()
        response = c.post(
            reverse("users:signup"),
            {
                "username": TEST_USERNAME,
                "password1": "new_password",
                "password2": "new_password",
            },
        )
        self.assertRedirects(response, SIGNUP_REDIRECT_PAGE)
