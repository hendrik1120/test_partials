import pytest
from django.urls import reverse

from demo_app.models import TestModel


@pytest.mark.django_db
def test_partial_context(client):
    TestModel.objects.create(text="test1")
    TestModel.objects.create(text="test2")

    response = client.get(reverse("partial-view"))
    assert response.status_code == 200
    assert len(response.context["test"]) == 2


@pytest.mark.django_db
def test_regular_context(client):
    TestModel.objects.create(text="test1")
    TestModel.objects.create(text="test2")

    response = client.get(reverse("regular-view"))
    assert response.status_code == 200
    assert len(response.context["test"]) == 2
