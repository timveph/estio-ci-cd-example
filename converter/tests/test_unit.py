import unittest
import requests
import pytest
import requests_mock

from flask import url_for
from flask_testing import TestCase

from app import app

from application.routes import birthDate 


class TestInit(TestCase):
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

class TestConvert(unittest.TestCase):

    def test_values(self):

       self.assertEqual((0), 'value entered is less than one month', msg='Equal')   
        