from flask import Blueprint, render_template, request, redirect, flash, url_for, g

from decorators import login_required
from extensions import db
from models.QuestionModel import QuestionModel
from models.AnswerModel import AnswerModel
from forms.QuestionForm import QuestionForm
from forms.AnswerForm import AnswerForm

bp = Blueprint('question', __name__, url_prefix='/')


@bp.route('/question/waiting')
@login_required
def waiting():
    return 'todo'


@bp.route('/question/publish', methods=['POST'])
@login_required
def publish():
    form = QuestionForm(request.form)
    if form.validate():
        title = form.title.data
        content = form.content.data
        question = QuestionModel(title=title, content=content, author=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect('/')
    else:
        flash('标题或内容格式错误！')
        return redirect(url_for('question.index'))


@bp.route('/question/<int:question_id>')
def detail(question_id):
    question = QuestionModel.query.get(question_id)
    return render_template('detail.html', question=question)


@bp.route('/delete_question/<int:question_id>')
def delete(question_id):
    question = QuestionModel.query.get(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect('/')


@bp.route('/update_question/<int:question_id>', methods=['POST', 'GET'])
def update(question_id):
    question = QuestionModel.query.get(question_id)
    if request.method == 'GET':
        return render_template('detail.html', question=question, type='edit')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question.title = title
            question.content = content
            db.session.commit()
        else:
            flash('标题或内容格式错误！')
        return redirect('/')


@bp.route('/answer/<int:question_id>', methods=['POST'])
def answer(question_id):
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        answer_model = AnswerModel(content=content, author=g.user, question_id=question_id)
        db.session.add(answer_model)
        db.session.commit()
        return redirect('/')
    else:
        flash("表单验证失败！")
    return redirect('/')


@bp.route('/delete_answer/<int:answer_id>')
def delete_answer(answer_id):
    target = AnswerModel.query.get(answer_id)
    db.session.delete(target)
    db.session.commit()
    return redirect('/')


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(db.text('-create_time')).all()
    return render_template('index.html', questions=questions)
