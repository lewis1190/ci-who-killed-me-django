from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import NewsPost


class TestNewsBlogViews(TestCase):
    def setUp(self):
        """Set up test client and create sample news posts"""
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Use fixed base time for consistent datetime comparisons
        base_time = timezone.now()

        # Create published posts (created_on will be auto-set, then we
        # override)
        self.post1 = NewsPost.objects.create(
            title="First News",
            author=self.user,
            content="Content 1",
            status=1
        )
        self.post1.created_on = base_time - timezone.timedelta(days=3)
        self.post1.save()

        self.post2 = NewsPost.objects.create(
            title="Second News",
            author=self.user,
            content="Content 2",
            status=1
        )
        self.post2.created_on = base_time - timezone.timedelta(days=2)
        self.post2.save()

        self.post3 = NewsPost.objects.create(
            title="Third News",
            author=self.user,
            content="Content 3",
            status=1
        )
        self.post3.created_on = base_time - timezone.timedelta(days=1)
        self.post3.save()

        # Create unpublished post (status=0)
        self.unpublished_post = NewsPost.objects.create(
            title="Unpublished News",
            author=self.user,
            content="Content",
            status=0
        )
        self.unpublished_post.created_on = base_time
        self.unpublished_post.save()

    def test_news_list_view_status_code(self):
        """Test that news list view returns 200 status code"""
        response = self.client.get(reverse('news_list'))
        self.assertEqual(response.status_code, 200)

    def test_news_list_view_template(self):
        """Test that news list view uses correct template"""
        response = self.client.get(reverse('news_list'))
        self.assertTemplateUsed(response, 'newsblog/news_list.html')

    def test_news_list_shows_published_posts_only(self):
        """Test that only published posts are displayed"""
        response = self.client.get(reverse('news_list'))
        self.assertEqual(len(response.context['posts']), 3)
        self.assertNotIn(self.unpublished_post, response.context['posts'])

    def test_news_list_ordered_newest_first(self):
        """Test that posts are ordered by newest first"""
        response = self.client.get(reverse('news_list'))
        posts = list(response.context['posts'])
        self.assertEqual(posts[0].pk, self.post3.pk)
        self.assertEqual(posts[1].pk, self.post2.pk)
        self.assertEqual(posts[2].pk, self.post1.pk)

    def test_news_list_pagination(self):
        """Test that pagination works correctly"""
        response = self.client.get(reverse('news_list'))
        self.assertIn('page_obj', response.context)
        self.assertFalse(
            response.context['page_obj'].has_other_pages())

    def test_news_detail_view_status_code(self):
        """Test that news detail view returns 200 status code"""
        response = self.client.get(
            reverse('news_detail', args=[self.post1.pk]))
        self.assertEqual(response.status_code, 200)

    def test_news_detail_view_template(self):
        """Test that news detail view uses correct template"""
        response = self.client.get(
            reverse('news_detail', args=[self.post1.pk]))
        self.assertTemplateUsed(response, 'newsblog/news_detail.html')

    def test_news_detail_correct_post(self):
        """Test that detail view displays correct post"""
        response = self.client.get(
            reverse('news_detail', args=[self.post2.pk]))
        self.assertEqual(response.context['post'], self.post2)

    def test_news_detail_unpublished_post_returns_404(self):
        """Test that unpublished posts return 404"""
        response = self.client.get(
            reverse('news_detail', args=[self.unpublished_post.pk]))
        self.assertEqual(response.status_code, 404)

    def test_news_detail_recent_posts(self):
        """Test that recent posts exclude current post"""
        response = self.client.get(
            reverse('news_detail', args=[self.post2.pk]))
        recent_posts = response.context['recent_posts']
        self.assertEqual(len(recent_posts), 2)
        self.assertNotIn(self.post2, recent_posts)

    def test_news_detail_previous_post(self):
        """Test that previous post is correctly identified"""
        response = self.client.get(
            reverse('news_detail', args=[self.post2.pk]))
        self.assertEqual(response.context['previous_post'], self.post1)

    def test_news_detail_next_post(self):
        """Test that next post is correctly identified"""
        response = self.client.get(
            reverse('news_detail', args=[self.post2.pk]))
        self.assertEqual(response.context['next_post'], self.post3)

    def test_news_detail_first_post_no_previous(self):
        """Test that first post has no previous post"""
        response = self.client.get(
            reverse('news_detail', args=[self.post1.pk]))
        self.assertIsNone(response.context['previous_post'])

    def test_news_detail_last_post_no_next(self):
        """Test that last post has no next post"""
        response = self.client.get(
            reverse('news_detail', args=[self.post3.pk]))
        self.assertIsNone(response.context['next_post'])

    def test_news_detail_nonexistent_post_returns_404(self):
        """Test that requesting non-existent post returns 404"""
        response = self.client.get(reverse('news_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)
