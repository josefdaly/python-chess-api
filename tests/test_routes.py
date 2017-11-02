import json

import pytest
from flask import url_for


class TestProcessGameRoute(object):

    def test_basic_case_valid_moves(self, client):
        data = ['e4']
        res = client.post(url_for('process_game'), data=json.dumps(data))
        assert res.status_code == 200
        assert json.loads(res.data) == data
