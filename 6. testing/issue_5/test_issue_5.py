import unittest
from unittest.mock import Mock, patch
from issue_5 import what_is_year_now
import json


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_what_year_1(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '2022-11-15'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2022)

    @patch('urllib.request.urlopen')
    def test_what_year_2(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '2021-11-15'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2021)

    @patch('urllib.request.urlopen')
    def test_what_year_3(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '11.15.2019'}).encode('utf-8')
        result = what_is_year_now()
        self.assertEqual(result, 2019)

    @patch('urllib.request.urlopen')
    def test_what_year_4(self, mock_urlopen):
        mock_resp = mock_urlopen.return_value.__enter__.return_value
        mock_resp.read.return_value = json.dumps(
            {'currentDateTime': '11/15/2019'}).encode('utf-8')
        self.assertRaises(ValueError, what_is_year_now)
