# thanks to Traversy Media for this tutorial - https://www.youtube.com/watch?v=zRwy8gtgJ1A&t=1510s
from flask import Flask, render_template
from data import Articles

app = Flask(__name__)


# <!--# Define the WSGI application object-->
# app = Flask(__name__, static_url_path='/static')


Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/articles')
# def articles():
#     return render_template('articles.html', articles = Articles)
#
# @app.route('/article/<string:id>/')
# def article(id):
#     return render_template('article.html', id=id )

@app.route('/resume')
def resume ():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')



if __name__ == '__main__':
    app.run(debug=True)