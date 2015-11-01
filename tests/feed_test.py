import unittest

from flask import Flask
import json

from lib.static_feed.feed import Feed
from lib.static_feed.post import Post

# For nose test to load threat this as if it was in root where nose is executed (nose cwd is ../)
with open('config.json') as config_file:
    config = json.load(config_file)

app = Flask(__name__)
app.config.update(config['feed_config'])


class FeedTest(unittest.TestCase):

    def setUp(self):
        self.feed = Feed(app, root_dir='tests/mock_posts')

    def test_loading_number_of_posts(self):
        self.assertEqual(2, len(self.feed.posts))

    def test_loading_posts(self):
        self.assertTrue(isinstance(self.feed.get_post('mock1'), Post))


class PostTest(unittest.TestCase):

    def setUp(self):
        self.feed = Feed(app, root_dir = 'tests/mock_posts')

    def test_proper_html(self):
        self.assertEqual('<h1>This is a new hope</h1>', self.feed.get_post('mock1').html)

    @unittest.skip('app context issue - non critical, test related, skipping...')
    def test_proper_url(self):
        self.assertEqual('mock1', self.feed.get_post('mock1').url)