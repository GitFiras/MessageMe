from flask import current_app as app
from flask import render_template
# from app import app
# from app.forms import LoginForm

from .MessageMeApp import MessageMeApi

app.register_blueprint(MessageMeApi, url_prefix='')

# homepage
@app.route('/')
@app.route('/home')
def messageme():

    # return #render_template('MessageMe.html')

    user = {'username': 'user'}
    return '''
<html>
    <head>
         {% if title %}
        <title>{{ title }} - MessageMe</title>
        {% else %}
        <title>Welcome to MessageMe</title>
        {% endif %}

    </head>
    <body>
        <h1>Hello, ''' + user['username'] + ''', Welcome to MessageMe!!</h1>
    </body>
</html>'''

# ADDITIONAL LOGIN MODULE
# @app.route('/login')
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Sign In', form=form)

