from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

class WatchlistTesting(TestCase):
    def test_mywatchlist_html_is_exist(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_xml_is_exist(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    
    def test_mywatchlist_json_is_exist(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)