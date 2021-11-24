import wtforms
from wtforms.validators import length, Optional


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=1, max=200)])
    content = wtforms.StringField(validators=[Optional()])
