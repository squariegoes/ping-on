from flask import *

app = Flask(__name__)
app.secret_key = 'my precious'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contact')
def gallery():
    return render_template('contact.html')

if __name__ == '__main__':
    app.debug = False
    app.run()