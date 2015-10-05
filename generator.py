from flask import Flask, render_template

from lib.static_feed.static_feed import Feed

app = Flask(__name__)
blog = Feed(app, root_dir = 'posts')


@app.template_filter('date')
def format_date(value, format='%B %d, %Y'):
    return value.strftime(format)


@app.route('/')
def index():
    return render_template('index.html', posts=blog.posts)


@app.route('/blog/<path:path>')
def post(path):
    post = blog.get_post( path )
    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
