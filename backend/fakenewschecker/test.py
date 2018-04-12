import unittest, json
from index import app
import os

class FakeNewsCheckerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_result(self):
        response = self.app.get('/checknews/?article=http://flask.pocoo.org/docs/0.12/reqcontext/')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], "FAKE")

if __name__ == "__main__":
    unittest.main()