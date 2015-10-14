import sys
import SimpleHTTPServer
import SocketServer
import os

from flask import Flask, render_template
from flask.ext.frozen import Freezer

from lib.static_feed.static_feed import Feed

app = Flask(__name__)
app.config.from_pyfile('feed_config.py')

blog = Feed(app, root_dir = 'posts')
freezer = Freezer(app)

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
            run with 'build' to build static
        """
        #If we pass build argument, run freeze method to build static content.
        if app.config['DEBUG'] and not app.config['BUILD_DRAFTS']:
            app.config['DEBUG'] = False
        freezer.freeze()

    elif len(sys.argv) > 1 and sys.argv[1] == 'serve-static':
        """
            run with 'serve-static' to run simple server on port 8081 to serve generated static content
        """
        #serve static content built by 'build' task
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        os.chdir("build/")
        httpd = SocketServer.TCPServer(("", 8082), Handler)

        print "serving at port 8081"
        httpd.serve_forever()
    else:
        """
            no params runs server on port 4000 serving the content
        """
        # Here, I set it in dev-like environment (watching posts and source files and stuff)
        # because, main purpose will be generating statics, not being live in prod.
        post_files = [post.filepath for post in blog.posts]
        app.run(port=4000, extra_files=post_files)
