from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm

class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(title='testing', content='testing content')
        self.about.save()

    def test_render_about_page_with_collab_form(self):

        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"testing", response.content)
        self.assertIn(b"testing content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

        
    def test_successful_collab_submission(self):

        post_data = {
            'name' : 'test',
            'email' : 'test@test.com',
            'message' : 'test content'
        }
        response = self.client.post(reverse('about'), post_data)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content
        )