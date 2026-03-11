"""
Justin Wu
Lab 11, Classes, Objects, and Methods

"""
from flask import Flask, render_template

"""
create an object from the Flask module 
"""
app = Flask(__name__)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Justin Wu"
    fruits = ['apple', 'orange', 'grapes']
    fruit = 'pineapple'
    return render_template('index.html', username = name, listfruits = fruits, f = fruit)

# endpoints refer to the name of the view in an app
@app.route('/about')
def about():
    images = ['Horse.jpg', 'Crocodile.jpg', 'Tiger.jpg']
    return render_template('about.html', imagelist=images)


@app.route('/quotes')
def quotes():
    return ' <h1>Quotes</h1>'

# set the 'app to run if you execute the file directly (not when it is imported)
if __name__ == '__main__':
    app.run(debug=True)