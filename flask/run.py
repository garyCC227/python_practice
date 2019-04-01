from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    items = (i for i in range(10))
    dict = {
        'female':"mother",
        'male':'father'
    }
    return render_template('child.html')


if __name__ == '__main__':
    app.run(debug=True)
