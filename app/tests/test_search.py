import pytest

from app.aplica import app

@pytest.mark.usefixtures('client_class')
class testApp:
    @pytest.fixture
    def app(self):
        return app

    def test_search(self):
        responde = self.client.get("/search/wordcounts")
        assert response.data.decode('utf-8') == "<h1> Testando... </h1>"
        assert response.status_code == 200
