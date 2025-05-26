# Advanced Flask App
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'you-secret-key-here'

class User:
    def __init__(self, username, email, join_date):
        self.username = username
        self.email = email
        self.join_date = join_date

class Post:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

#sample user data
sample_user = User("Darryl Hii", "ddd@gmail.com", datetime.now())
sample_post = [
                Post("Getting Started with Flask", 
                "Flask is a lightweight web framework for Python...", 
                datetime.now()),
                Post("Template Inheritance", 
                "How to use Jinja2 templates effectively...", 
                datetime.now())
            ]

#Routes
@app.route("/")
def home():
    """Home page with dynamic content."""
    return render_template(
        "home.html", 
        user=sample_user, 
        posts=sample_post,
        current_time = datetime.now())

@app.route("/about")
def about():
    """About page with static content."""
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form handling."""
    if request.method == 'POST':
        name = request.form.get['name']
        email = request.form.get['email']
        subject = request.form.get['subject']
        message = request.form.get('message')

        print(f"Contact form submitted: ")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/user/<username>')
def user_profile(username):
    """Dynamic route for User profile page."""

    user_data = {
        'username': username,
        'join_date': datetime.now(),
        'post_count': len(sample_post),
    }
    return render_template('user_profile.html', user=user_data)

@app.route('/post/<int:post_id>')
def view_post(post_id):
    """Dynamic route for integer converter."""
    if 0 <= post_id < len(sample_post):
        post = sample_post[post_id]
        return render_template('post.html', post=post, 
        post_id = post_id)
    else:
        flash('Post not found!')
        return redirect(url_for('home'))

@app.route('/api/posts')
def api_posts():
    """API endpoint for retrieving posts."""
    posts_data = []
    for i, post in enumerate(sample_post):
        post_data = {
            'id': i,
            'title': post.title,
            'content': post.content,
            'date': post.date.strftime('%Y-%m-%d %H:%M:%S')
        }
        posts_data.append(post_data)
    return {'posts': posts_data}

@app.route('/search')
def search():
    """Search functionality with query parameters."""
    query = request.args.get('q', '')
    results = []

    if query:
        for post in sample_posts:
            if query.lower() in post.title.lower() or query.lower() in post.content.lower():
                results.append(post)
    
    return render_template('search.html', query=query, results=results)


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Custom 500 error page. """
    return render_template('500.html'), 500

@app.template_filter('datetime')
def datetime_format(value, format='%Y-%m-%d %H:%M:%S'):
    """Custom filter to format datetime objects. """
    return value.strftime(format)

@app.context_processor
def inject_now():
    """Make current datetime avilable to all templates. """
    return {'now': datetime.now()}

if __name__ == '__main__':
    app.run(debug=True, port=5001)