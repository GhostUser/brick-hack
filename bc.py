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
'''
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
        if 'file' not in request.files:
                return "NO FILE"
        file = request.files['file']
        filename = "image.jpg"
        file.save('/tmp/' + filename)
        labels = get_labels('/tmp/' + filename)
        classification=''
        classification = labels[0].description
                
        if classification=='':
            classification="no labels found"

        return render_template('display_labels.html', labels=labels, classification=classification)
    elif request.method=='GET':
        return render_template('upload.html')
    
'''


if __name__ == '__main__':
    app.run()