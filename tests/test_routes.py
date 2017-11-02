import pytest
from flask import url_for

class TestProcessGameRoute(object):

    def test_basic_case(self, client):
        res = client.post(url_for('process_game'))
        assert res.status_code == 200
        assert res.data == 'Response'
