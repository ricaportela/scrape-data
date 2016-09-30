import pytest

from app.aplica import app

@pytest.mark.usefixtures('client_class')
class TestApp:
    @pytest.fixture
    def app(self):
        return app

    def test_search(self):
        resp = self.client.get("/search/wordcounts/")
        assert response.data.decode('utf-8') == jsonify ({})
        assert response.status_code == 200
