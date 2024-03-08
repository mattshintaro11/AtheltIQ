from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is your scheduling application!'

if __name__ == '__main__':
    app.run(debug=True)
