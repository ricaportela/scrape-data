import pytest
import json
from app.aplica import app


@pytest.mark.usefixtures('client_class')
class TestApp:
    @pytest.fixture
    def app(self):
        return app

    def test_search_keyword(self):
        resp = self.client.get("/search/wordcounts?query=Microfocus")
        assert resp.json == {
                                   "wordcounts": [
                                 {
                                   "id": 1,
                                   "keyword": "Microfocus",
                                   "value": 45
                                 }
                               ]
                             }
        assert resp.status_code == 200
