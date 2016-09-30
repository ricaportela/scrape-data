import pytest
import json
from app.aplica import app


@pytest.mark.usefixtures('client_class')
class TestApp:
    @pytest.fixture
    def app(self):
        return app

    def test_search(self):
        resp = self.client.get("/search/wordcounts/")
        assert resp  == json.loads(resp.data.decode())
        import ipdb; ipdb.set_trace()

        assert resp.status_code == 200
