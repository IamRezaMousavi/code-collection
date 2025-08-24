# @Author: @IamRezaMousavi
# @Date:   2023-02-14 19:05:18
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2023-02-14 19:20:00
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_user1 = User.objects.create(username='testuser1', password='abc123')
        test_user1.save()

        test_post = Post.objects.create(author=test_user1, title='test title', body='This is body')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')
