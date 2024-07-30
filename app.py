from flask import Flask, render_template

app = Flask(__name__)

# Predefined list of blog posts
posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'created_at': '2024-01-01'
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'created_at': '2024-02-01'
    },
    {
        'id': 3,
        'title': 'Third Post',
        'content': 'This is the content of the third post.',
        'created_at': '2024-03-01'
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>/')
def post_detail(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    return render_template('post_detail.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
