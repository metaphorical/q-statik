import sys

from flask import Flask, render_template
from flask.ext.frozen import Freezer

from lib.static_feed.static_feed import Feed

app = Flask(__name__)
blog = Feed(app, root_dir = 'posts')
freezer = Freezer(app )


@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)


@app.route('/')
def index():
    return render_template('index.html', posts=blog.posts)


@app.route('/blog/<path:path>/')
def post(path):
    post = blog.get_post( path )
    return render_template('post.html', post=post)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        """
            If we pass build argument, run freeze method to build static content.
        """
        freezer.freeze()
    else:
        """
            Here, I set it in dev-like environment (watching posts and source files and stuff)
            because, main purpose will be generating statics, not being live in prod.
        """
        post_files = [post.filepath for post in blog.posts]
        app.run(port=8000, debug=True, extra_files=post_files)
