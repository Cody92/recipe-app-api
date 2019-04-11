from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """Test creating a new user with an email is successfull"""
        email = 'utkarsh.saxena1@gmal.com'
        password = 'testpass'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user normalized"""
        email = 'utkarsh.saxena1@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'testpass')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpass')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'utkarsh.saxena1@gmail.com',
            'test123'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)