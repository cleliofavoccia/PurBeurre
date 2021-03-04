"""Test views of website app"""

from django.test import TestCase
from django.shortcuts import reverse


class IndexViewTest(TestCase):
    """Class to test index view"""
    def test_if_view_uses_correct_template(self):
        """Test index view use website/index.html template"""
        response = self.client.get(reverse('website:index'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/index.html')


class LegalMentionsViewTest(TestCase):
    """Class to test legal mentions view"""
    def test_if_view_uses_correct_template(self):
        """Test legal mentions view use
        website/legal_mentions.html template"""
        response = self.client.get(reverse('website:legal_mentions'))
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/legal_mentions.html')
