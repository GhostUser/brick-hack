from flask import Flask, request, render_template
#from vision import get_labels

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/room.html')
def room():
    return render_template('room.html')



if __name__ == '__main__':
    app.run(threaded=True, port=5000)