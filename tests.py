"""Project-level tests.

Prefer app-level tests under each app's /tests.py.
This file keeps a small smoke test to validate the custom user model.
"""

from django.test import TestCase

from apps.users.models import User


class UserModelSmokeTests(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="user@example.com", first_name="John", last_name="Doe")
        user.set_password("Pa$$w0rd")
        user.save()

        self.assertTrue(user.check_password("Pa$$w0rd"))
        self.assertEqual(str(user), "John Doe")
