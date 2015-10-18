import os

from flask import url_for, abort

from ..modules.feedict import SortedDict
from post import Post

class Feed(object):
    def __init__(self, app, root_dir='', file_ext=None):
        self.root_dir = root_dir
        self.file_ext = file_ext if file_ext is not None else app.config['POSTS_FILE_EXTENSION']
        self._app = app
        self._cache = SortedDict(key = lambda p: p.date, reverse=True)
        self._initialize_cache()

    @property
    def posts(self):
        if self._app.debug:
            return self._cache.values()
        else:
            return [post for post in self._cache.values() if post.published]

    def get_post(self, path):
        """Returns post object of raises 404
        """
        try:
            return self._cache[path]
        except KeyError:
            abort(404)


    def _initialize_cache(self):
        """Walks the root directory and caches posts
        """
        for (root, dirpaths, filepaths) in os.walk(self.root_dir):
            for filepath in filepaths:
                filename, ext = os.path.splitext(filepath)
                if ext == self.file_ext:
                    path = os.path.join(root, filepath).replace(self. root_dir, '')
                    post = Post(path, root_dir = self.root_dir)
                    self._cache[post.urlpath] = post