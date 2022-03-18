from flask import Flask, render_template, request
from compute import mde#, create_figure, compute
from validation import InputForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        Mde_c = mde(form.alpha.data, form.beta.data,
                         form.sigma.data, form.n.data,
                         form.Mean.data)
        # result = create_figure#(form.alpha.data, form.beta.data,
        #                 form.sigma.data, form.n.data,
        #                 form.Mean.data)
        #df = pd.read_csv(request.files.get('file'))
    else:
        #df = pd.DataFrame()
        Mde_c = None
        # result = None
    return render_template("index.html", current_title='Custom Title',  form=form, Mde_c=Mde_c)

if __name__ == '__main__':
    app.run(debug=True)
