from django.test import TestCase
from .models import Posts
from django.urls import reverse

# Create your tests here.
class PostsTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.posts = Posts.objects.create(text='This is a test')

    def test_model_content(self):

        self.assertEqual(self.posts.text, 'This is a test')

    def test_page_location_exists(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'This is a test')