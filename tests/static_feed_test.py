# Fix for internal packages call
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import unittest

from flask import Flask

from lib.static_feed.static_feed import Feed


app = Flask(__name__)
app.config.from_pyfile('../feed_config.py')


class feedTest(unittest.TestCase):

	def test_create_feed(self):
		feed = Feed(app, root_dir = 'tests/mock_posts')

	def test_loading_number_of_posts(self):
		feed = Feed(app, root_dir = 'tests/mock_posts')
		self.assertEqual(1, len(feed.posts))

	def test_loading_post(self):
		feed = Feed(app, root_dir = 'tests/mock_posts')
		self.assertEqual('<h1>This is a new hope</h1>', feed.get_post('mock1').html)





if __name__ == '__main__':
    unittest.main()