import json
import pprint

def get_posts():
    with open("data/data.json", encoding='utf-8') as f:
        posts = json.load(f)
    return posts


def get_comments():
    with open("data/comments.json", encoding='utf-8') as f:
        comments = json.load(f)
    return comments


def get_posts_with_comments_count():
    posts = get_posts()
    comments = get_comments()

    for index, post in enumerate(posts):

        comments_count = 0
        for comment in comments:
            if comment["post_id"] == post["pk"]:
                comments_count += 1

        posts[index]['comments_count'] = comments_count

    return posts


def get_post_by_pk(post_pk):
    posts = get_posts()
    for post in posts:
        if post["pk"] == post_pk:
            post['content'] = replace_hashtags_with_links(post['content'])
            return post
    return None


def get_post_comments_by_pk(post_pk):
    with open("data/comments.json", encoding='utf-8') as f:
        comments = json.load(f)
        post_comments = []
    for comment in comments:
        if comment["post_id"] == post_pk:
            post_comments.append(comment)
    return post_comments


def replace_hashtags_with_links(content):
    words = content.split(" ")
    for index, word in enumerate(words):
        if word.startswith("#"):
            tag = word[1:]
            words[index] = f"<a href='tags/{tag}'>{word}</a>"
    return " ".join(words)

def search_word_in_content(user_search_word):
    posts = get_posts()
    search_posts = []
    for post in posts:
        if user_search_word in (post['content']):
            search_posts.append(post['content'])
    return search_posts


def get_username(username):
    user_posts = []
    posts = get_posts_with_comments_count()
    for post in posts:
        if post['poster_name'] == username:
            user_posts.append(post)
    return user_posts

# print(search_word_in_content('кот'))