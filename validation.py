from wtforms import Form, FloatField, SelectField, validators

class InputForm(Form):
        alpha = FloatField(
            label='the selected level of significance', default=0.05,
            validators=[validators.InputRequired()])
        beta = FloatField(
            label='%', default=20,
            validators=[validators.InputRequired()])
        sigma = FloatField(
            label='the standard deviation', default=1,
            validators=[validators.InputRequired()])
        n = FloatField(
            label='', default=100,
            validators=[validators.InputRequired()])
        Mean = FloatField(
            label='', default=10,
            validators=[validators.InputRequired()])
        Side = SelectField(
            u'one-sided or two-sided test', choices=[('one', 'one-sided'), ('two', 'two-sided')]
            )
