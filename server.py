from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/connect')
def login():
    return render_template('login.html', user_existing=True)

@app.route('/signup')
def signup():
    return render_template('login.html', user_existing=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
