from django.test import TestCase

class HomePageTest(TestCase):

    def test_usues_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')