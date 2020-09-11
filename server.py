from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello world'

@app.route('/about')
def about():
	return 'The about page'

@app.route('/blog')
def blog():
	posts = [{'title': 'Technology in 2019', 'author': 'Tom'},
	{'title': 'Expansion of oil in Russia', 'author': 'Bob'}]
	return render_template('blog.html', author="Thomas Snellgrove", sunny=False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
	return 'This is the blog post number ' + blog_id

if __name__ == '__main__':
	app.run()


