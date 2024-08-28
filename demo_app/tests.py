from django.test import TestCase
from django.urls import reverse

from demo_app.models import TestModel


class TestContext(TestCase):
    def setUp(self):
        TestModel.objects.create(text="test1")
        TestModel.objects.create(text="test2")

    def test_partial_context(self):
        response = self.client.get(reverse("partial-view"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["test"]), 2)

    def test_regular_context(self):
        response = self.client.get(reverse("regular-view"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["test"]), 2)