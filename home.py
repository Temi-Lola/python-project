from flask import Flask, render_template, request
app = Flask("My App")

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/food')
def food_page():
    return render_template("food.html")


@app.route('/people')
def people_page():
    return "We are Sorry! This page is down for maintenance"

@app.route('/events')
def events_page():
    return "We are Sorry! This page is down for maintenance"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
