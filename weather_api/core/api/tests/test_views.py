import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestTemperatureListView:
    @pytest.fixture
    def anti_spam_token(self):
        return "test-anti-spam-token"

    @pytest.fixture
    def override_settings(self, settings, anti_spam_token):
        settings.ANTI_SPAM_TOKEN = anti_spam_token

    @pytest.fixture
    def url(self):
        return reverse("core:temperature-list")

    def test_response_is_ok(self, api_client, url, override_settings, anti_spam_token):
        response = api_client.get(url, headers={"X-Token": anti_spam_token})
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_without_token_header(self, api_client, url, override_settings):
        response = api_client.get(url)
        assert response.status_code == status.HTTP_403_FORBIDDEN
