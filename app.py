from flask import Flask, render_template, request, jsonify
from io import StringIO
from validation import InputForm
import pandas as pd
from compute import compute

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        #result = compute(form.alpha.data, form.beta.data)
        df = pd.read_csv(StringIO(request.file['file']))
        #df = pd.read_csv(request.files.get('file'))
        #df = df.shape
        #tables = [df.to_html(classes='data', index=False)]
        #itles = df.columns.values
        return render_template("index.html", current_title='Custom Title',
                           MDE=df, form=form, result=result,
                           #tables=tables,
                           #titles=titles
                               )
    else:
        df = pd.DataFrame({'unique id': [1, 2, 3, 4, 5, 6],
                           'metric value': [10, 11, 12, 10, 13, 14],
                           'test group': ['a', 'b', 'a', 'a', 'b', 'b']})
        #MDE = df.shape
        #tables = [df.to_html(classes='data', index=False)]
        #titles = df.columns.values
        return render_template("index.html", current_title='Custom Title',
                           form=form, MDE=df)

if __name__ == '__main__':
    app.run(debug=True)
