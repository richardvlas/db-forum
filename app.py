from flask import Flask, request, render_template, redirect, url_for

from forum_db import get_posts, add_post


app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    """Main page of the forum."""
    posts = get_posts()
    
    return render_template("home.html", posts=posts)


@app.route('/', methods=['POST'])
def post():
    """New post submission."""
    message = request.form['content']
    add_post(message)
    
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(host='localhost', port=5679, debug=True)