from wtforms import Form, FloatField, validators

class InputForm(Form):
        alpha = FloatField(
            label='%', default=0.05,
            validators=[validators.InputRequired()])
        beta = FloatField(
            label='%', default=80,
            validators=[validators.InputRequired()])
        tail = FloatField(
            label='(one-tailed/two-tailed)', default='two-tailed',
            validators=[validators.InputRequired()])