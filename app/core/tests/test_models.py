from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "john.doe@test.com"
        password = "Test123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_create_user_with_normalized_email(self):

        email = "john.doe@TEST.COM"

        user = get_user_model().objects.create_user(
            email=email,
            password="Test1234"
        )

        self.assertEqual(user.email, email.lower())

    def test_create_user_with_invalid_email(self):

        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email=None, password="abcd1234")

    def test_create_new_superuser(self):

        user = get_user_model().objects.create_superuser('superuser@test.com', 'test1234')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

