from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB
client = MongoClient('localhost', 27017)
db = client.personal_website
contacts = db.contacts

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        contacts.insert_one({'name': name, 'email': email, 'message': message})
        return redirect('/')
    return render_template('contact.html')

@app.errorhandler(Exception)
def internal_error(error):
    return render_template('error.html',error_code=500)

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html',error_code=404)


if __name__ == '__main__':
    app.run(debug=True)
