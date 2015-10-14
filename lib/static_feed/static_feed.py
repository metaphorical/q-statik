import os
import markdown
import yaml

from flask import url_for, abort

from werkzeug import cached_property

from ..modules.feedict import SortedDict

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





class Post(object):
    def __init__(self, path, root_dir=''):
        self.urlpath = os.path.splitext(path.strip('/'))[0]
        self.filepath = os.path.join(root_dir, path.strip('/'))
        self.published = False
        self._initialize_metadata()

    @cached_property
    def html(self):
        with open(self.filepath, 'r') as fin:
            content = fin.read().split('\n\n', 1)[1].strip()
            return markdown.markdown(content)

    @property
    def url(self):
        return url_for('post', path=self.urlpath)

    def _initialize_metadata(self):
        content = ''
        with open(self.filepath, 'r') as fin:
            for line in fin:
                if not line.strip():
                    break
                content += line
        # Put meta data into self dictionary...
        # Think about putting it into meta dictionary
        self.__dict__.update(yaml.load(content))
