from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        login = request.form.get('login')
        email = request.form.get('email')
        if not login:
            flash('Вы не ввели логин', 'danger')
        if not email:
            flash('Вы не ввели почту', 'warning')
        if login and email:
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('login', login)
            response.set_cookie('email', email)
            return response
    response = make_response(render_template('index.html', title='Введите данные'))
    return response


@app.route('/welcome/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        response = make_response(redirect(url_for('index')))
        response.set_cookie('login', '')
        response.set_cookie('email', '')
        return response
    login = request.cookies.get('login')
    return render_template('welcome.html', login=login, title='Добро пожаловать')


if __name__ == '__main__':
    app.run(debug=True)