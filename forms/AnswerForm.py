import wtforms
from wtforms.validators import length


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])
