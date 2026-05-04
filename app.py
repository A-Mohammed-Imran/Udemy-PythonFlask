from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<name>')
def hello_name(name):
    return (f"Hello {name}!")

# redirect and url_for example

@app.route('/admin')
def hello_admin():
    return "Hello Admin!"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f"Hello {guest} as Guest"

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))

# HTTP Methods (GET, POST, etc.)

@app.route('/welcome/<name>')
def welcome(name):
    return f"Welcome {name}!"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user=request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('welcome', name=user))
    
@app.route('/render')
def render():
    str = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Render Page</title>
</head>
<body>
<p>This is a render html page.</p>
</body>
</html>"""
    return str
# we can also use the main html doc fromtemplates folder with the help of 'render_template' function

# Static files (CSS, JavaScript, Images)

@app.route('/static')
def static_files():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(debug=True)