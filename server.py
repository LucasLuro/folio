# It's possible to use http.server library built-in Python or one of 2 Frameworks: Flask or Django. Flask is smaller and more simple, 
# Django is a whole nother beast, to refresh the info on the website you have to shut it down and turn it on again on your terminal.
# To make this refresh automatic you can turn on Development environment on Flask which comes with a Debug Mode.
# Static Files, are files that will never going to change, for example JS and CSS files.
# The power of flask is that it allows us to build things dinamically with Jinja (which is built-in Flask).
# Flask also has the tool named Variable Rules (read documentation).

import csv
from lib2to3.pgen2.token import NEWLINE
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/<string:page_name>')
def all_pages(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            mailing_sheet(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong, please try again!'

@app.route('/')
def my_home():
    return render_template('index.html')

def build_mailing(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email}, {subject}, {message}')

def mailing_sheet(data):
    with open ('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


# @app.route('/index.html')
# def also_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def portfolio():
#     return render_template('works.html')

# @app.route('/work.html')
# def also_portfolio():
#     return render_template('work.html')

# @app.route('/contact.html')
# def talk_dirty_to_me():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')