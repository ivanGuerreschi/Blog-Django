from django.test import TestCase
from blog.models import Post

class PostModelTest(TestCase):

    def test_string(self):
        post = Post(title = "Prova")
        self.assertEqual(str(post), post.title)    
