from flask import Flask, redirect, url_for, request, render_template, make_response, session
app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return (f"Hello {name}!")

# # redirect and url_for example

# @app.route('/admin')
# def hello_admin():
#     return "Hello Admin!"

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return f"Hello {guest} as Guest"

# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))

# # HTTP Methods (GET, POST, etc.)

# @app.route('/welcome/<name>')
# def welcome(name):
#     return f"Welcome {name}!"

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user=request.form['nm']
#         return redirect(url_for('welcome', name=user))
#     else:
#         user=request.args.get('nm')
#         return redirect(url_for('welcome', name=user))
    
# @app.route('/render')
# def render():
#     str = """<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Render Page</title>
# </head>
# <body>
# <p>This is a render html page.</p>
# </body>
# </html>"""
#     return str
# # we can also use the main html doc fromtemplates folder with the help of 'render_template' function

# # Static files (CSS, JavaScript, Images)

# @app.route('/static')
# def static_files():
#     return render_template('static.html')

# Framwoerks (Request.from Object)

# @app.route('/student')
# def student():
#     return render_template('student.html')

# @app.route('/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template('result.html', result=result)
#     return "Method not allowed"

# framework (Cookies)
# @app.route('/cookie')
# def index():
#     return render_template('cookie.html')

# @app.route('/getcookie', methods=['POST', 'GET'])
# def getcookie():
#     if request.method == 'POST':
#         user = request.form['nm']
#         resp = make_response(render_template('getcookie.html', name=user))
#         resp.set_cookie('userID', user)
#         return resp
#     else:
#         user = request.cookies.get('userID')
#         return render_template('getcookie.html', name=user or "Guest")

# Framwork (Sessions)
app.secret_key = 'admin123'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Login as ' + username + '<br>' + "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + "click here to log in</b></a>"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)