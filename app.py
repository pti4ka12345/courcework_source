from flask import Flask, request, render_template, send_from_directory, abort
from function import *


app = Flask(__name__)


@app.route('/')
def page_index():
    posts = get_posts_with_comments_count()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_pk>')
def page_post(post_pk):
    post = get_post_by_pk(post_pk)
    comments = get_post_comments_by_pk(post_pk)
    comments_count = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_count=comments_count)



@app.route('/users/<username>')
def page_user(username):
   posts = get_username(username)
   return render_template('user-feed.html', posts=posts, username=username)


@app.route('/search/<search_word>')
def page_search(search_word):
    user_search_word = request.args.get("s")
    posts = search_word_in_content(user_search_word)
    return render_template('search.html', posts=posts)





app.run()