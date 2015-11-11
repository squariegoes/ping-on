from flask import *

app = Flask(__name__)
app.secret_key = 'my precious'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sit_in_menu')
def sit_in_menu():
    return render_template('sit_in_menu.html')

@app.route('/takeaway_menu')
def takeaway_menu():
    return render_template('takeaway_menu.html')

@app.route('/contact')
def gallery():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    return home()

if __name__ == '__main__':
    app.debug = False
    app.run()