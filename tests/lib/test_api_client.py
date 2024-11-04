import unittest
from unittest import mock

from fetcher.lib.api_client import post_data, EmptyBodyException, RequestException


class TestPostRequest(unittest.TestCase):

    @mock.patch("requests.post")
    def test_post_success_request(self, mock_response):
        _body = {"key": "value"}

        response = mock_response.return_value
        response.raise_for_status_value = None
        response.json.return_value = {"status": "success"}

        result = post_data(url="http://fake-url.com", data=_body)
        self.assertEqual(result, {"status": "success"})

    @mock.patch("requests.post")
    def test_post_body_is_empty(self, mock_response):
        _body = {}
        with self.assertRaises(EmptyBodyException):
            post_data(url="http://fake-url.com", data=_body)
        mock_response.assert_not_called()

    def test_post_url_is_empty(self):
        _body = {"key": "value"}
        with self.assertRaises(RequestException):  # InvalidHeader
            post_data(url="", data=_body)

    # check header type
    def test_post_invalid_header(self):
        _header = {"header": 123}
        _body = {"key": "value"}
        with self.assertRaises(RequestException):  # InvalidHeader
            post_data(url="http://fake-url.com", headers=_header, data=_body)

        _header = 123
        with self.assertRaises(AttributeError):  # InvalidHeader
            post_data(url="http://fake-url.com", headers=_header, data=_body)
