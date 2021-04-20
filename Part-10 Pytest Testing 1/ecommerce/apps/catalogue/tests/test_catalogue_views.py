import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_root_url(client):
    url = reverse("catalogue:store_home")
    response = client.get(url)
    assert response.status_code == 200
