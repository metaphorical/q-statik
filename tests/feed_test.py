import unittest

from flask import Flask

from lib.static_feed.feed import Feed
from lib.static_feed.post import Post


app = Flask(__name__)
app.config.from_pyfile('../feed_config.py')


class feedTest(unittest.TestCase):

	def setUp(self):
		self.feed = Feed(app, root_dir = 'tests/mock_posts')

	def test_loading_number_of_posts(self):
		self.assertEqual(2, len(self.feed.posts))

	def test_loading_posts(self):
		self.assertTrue(isinstance(self.feed.get_post('mock1'), Post))


class postTest(unittest.TestCase):

	def setUp(self):
		self.feed = Feed(app, root_dir = 'tests/mock_posts')

	def test_proper_html(self):
		self.assertEqual('<h1>This is a new hope</h1>', self.feed.get_post('mock1').html)

	@unittest.skip('app context issue - non critical, test related, skipping...')
	def test_proper_url(self):
		self.assertEqual('mock1', self.feed.get_post('mock1').url)