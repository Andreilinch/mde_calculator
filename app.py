from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('index.html',  current_title = 'Custom Title',shape=df.shape)
    else:
        return render_template('index.html', current_title = 'Custom Title')

# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     if request.method == 'POST':
#         df = pd.read_csv(request.files.get('file'))
#         return render_template('result.html',  shape=df.shape)
#     return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
#print(__name__)