import unittest
import requests
import pytest
# import requests_mock
from flask_testing import TestCase
from app import app


class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED=False,
            DEBUG=True
            )
        return app

    def setUp(self):
        print("-----------")

    def tearDown(self):
        print("--------")

class TestMain(unittest.TestCase):

    pass
    # def test_response(self):
    #     response = self.client.get(url_for('index'))
        # self.assertEqual(response.status_code, 200, msg='Expecting status code of 200')