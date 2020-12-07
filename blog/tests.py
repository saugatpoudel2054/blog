from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


from .models import Article

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.article = Article.objects.create(
            title='A good title',
            text='Nice body content',
            author=self.user,
        )
        
    def test_string_representation(self):
        article = Article(title='A sample title')
        self.assertEqual(str(article), article.title)

    def test_article_content(self):
        self.assertEqual(f'{self.article.title}', 'A good title')
        self.assertEqual(f'{self.article.author}', 'testuser')
        self.assertEqual(f'{self.article.text}', 'Nice body content')

    def test_article_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_article_detail_view(self):
        response = self.client.get('/article/1/')
        no_response = self.client.get('/article/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
        'title': 'New title',
        'text': 'New text',
        'author': self.user,
        })

        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
        'title': 'Updated title',
        'text': 'Updated text',
        })
        self.assertEqual(response.status_code,302)

    def test_post_delete_view(self):
        response = self.client.get(
        reverse('post_delete', args='1'))
        self.assertEqual(response.status_code,200)




