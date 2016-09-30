import pytest
import json
from app.aplica import app


@pytest.mark.usefixtures('client_class')
class TestApp:
    @pytest.fixture
    def app(self):
        return app

    def test_search(self):
        resp = self.client.get("/search/wordcounts")
        assert resp.json == {
                              "wordcounts": [
                                {
                                  "id": 1,
                                  "keyword": "Microfocus",
                                  "value": 45
                                },
                                {
                                  "id": 2,
                                  "keyword": "Programador",
                                  "value": 33
                                },
                                {
                                  "id": 34,
                                  "keyword": "Cobol",
                                  "value": 3
                                }
                              ]
                            }

        assert resp.status_code == 200

    def test_search_id(self):
        resp = self.client.get("/search/wordcounts/0")
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
