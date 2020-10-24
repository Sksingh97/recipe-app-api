from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    # Setup function will run before running any function
    def setUp(self):
        # Creating a client to login
        self.client = Client()
        # created new admin user
        self.admin_user = get_user_model().objects.create_superuser(
            email="test@gmail.com",
            password="test@123"
        )
        # login using the created user
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="normal@gmail.com",
            password="test@123",
            name="normal user"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that user edit page works"""
        #  /admin/core/user/1
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
