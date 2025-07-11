from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from forms import UserForm
import config  # importa a configuração que carrega o .env

app = Flask(__name__)
app.config.from_object(config.Config)
db = SQLAlchemy(app)

from models import User

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = UserForm()
    if form.validate_on_submit():
        if not form.password.data:
            flash('Senha é obrigatória para criar usuário.')
            return render_template('create.html', form=form)
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        try:
            db.session.commit()
            flash('Usuário criado com sucesso!')
            return redirect(url_for('index'))
        except Exception:
            db.session.rollback()
            flash('Erro: email já cadastrado ou outro problema.')
            return render_template('create.html', form=form)
    return render_template('create.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    user = User.query.get_or_404(id)
    form = UserForm()

    if request.method == 'GET':
        form.name.data = user.name
        form.email.data = user.email
        # senha fica vazia

    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.email.data

        if form.password.data:
            if check_password_hash(user.password, form.password.data):
                flash('A senha informada é igual à senha atual. Por favor, escolha uma senha diferente.')
                return render_template('edit.html', form=form)
            user.password = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        try:
            db.session.commit()
            flash('Usuário atualizado com sucesso!')
            return redirect(url_for('index'))
        except Exception:
            db.session.rollback()
            flash('Erro ao atualizar usuário. Talvez o email já esteja em uso.')
            return render_template('edit.html', form=form)

    return render_template('edit.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    try:
        db.session.commit()
        flash('Usuário excluído com sucesso!')
    except Exception:
        db.session.rollback()
        flash('Erro ao excluir usuário.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
