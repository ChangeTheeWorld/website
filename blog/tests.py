from django.test import TestCase
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test import Client
from .models import BlogPost
import json
# Create your tests here.
teardown_test_environment()
setup_test_environment()


class BlogTestCase(TestCase):
    def test_api_status(self):
        client = Client()
        for post in BlogPost.objects.all():
            self.assertEqual(client.get(f'/blog/api/{post.id}').status_code, 200)

    def test_api_values(self):

        client = Client()
        for post in BlogPost.objects.all():
            # self.assertEqual(json.loads(client.get(f'/blog/api/{post.id}').content)["content"], )
            self.assertEqual(json.loads(client.get(f'/blog/api/{post.id}').content)['id'], post.id)
            self.assertEqual(json.loads(client.get(f'/blog/api/{post.id}').content)['title'], post.title)
            self.assertEqual(json.loads(client.get(f'/blog/api/{post.id}').content)['content'], post.content)

    def test_api(self):
        ...