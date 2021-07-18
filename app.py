from flask import Flask, render_template, request
import pandas as pd
from compute import mde, plot_png
from validation import InputForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        Mde_c = mde(form.alpha.data, form.beta.data,
                         form.sigma.data, form.n.data,
                         form.Mean.data)
        result = plot_png#(form.alpha.data, form.beta.data,
        #                 form.sigma.data, form.n.data,
        #                 form.Mean.data)
        #df = pd.read_csv(request.files.get('file'))
    else:
        #df = pd.DataFrame()
        Mde_c = None
        result = None
    return render_template("index.html", current_title='Custom Title',  form=form, Mde_c=Mde_c, result=result)

if __name__ == '__main__':
    app.run(debug=True)
