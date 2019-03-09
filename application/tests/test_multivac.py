import unittest

from flask import current_app


class TestMultiVac(unittest.TestCase):

    def setUp(self):
        self.app = current_app.test_client()
        self.app.testing = True

    def test_get_multivac(self):
        response = self.app.get('/multivac')
        self.assertEqual(response.status_code, 200)

    def test_post_multivac(self):
        response = self.app.post('/multivac/data', data=dict(data='test'))
        self.assertEqual(response.status_code, 200)

    def test_get_multivac_data(self):
        response = self.app.get('/multivac')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data, "INSUFFICIENT DATA FOR MEANINGFUL ANSWER.")


if __name__ == '__main__':
    unittest.main()
