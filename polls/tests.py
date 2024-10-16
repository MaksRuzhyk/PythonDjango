from django.test import TestCase
from django.urls import reverse
from .models import Post, Author
from .forms import PostForm
from django.test.utils import setup_test_environment
from django.test import Client
from datetime import datetime

# Create your tests here.

class AddPostTest(TestCase):
    def setUp(self):
        self.url = reverse('add_post')
        self.user = Author.objects.create(first_name='John', last_name='Doe')

    def test_get_form(self):

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PostForm)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_valid_data(self):
        valid_data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'author': self.user.id
        }

        response = self.client.post(self.url, valid_data)
        if Post.objects.count() == 0:
            print(response.context['form'].errors)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')

    def test_invalid_data(self):

        invalid_data = {
            'title': '',
            'content': '321',
            'author': self.user.id
        }

        response = self.client.post(self.url, invalid_data)
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PostForm)
        self.assertTemplateUsed(response, 'add_post.html')

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Home Page")
        self.assertIn('latest_question_list', response.context)

    def test_post_datail(self):
        response = self.client.get('post_datail')
        self.assertEqual(response.status_code, 404)