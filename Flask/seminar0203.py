from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def base():
    return render_template('seminar0203_first.html')

@app.route('/login/')
def form_login():
    return render_template('seminar0203_login.html')

@app.route('/auth/', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_pass = request.form.get('pass')
        if user_name == 'Olga' and user_pass == '12345':
            return 'Добро пожаловать'
        else:
            return 'Таких не знаем'
    else:
        return redirect(url_for('base'))

if __name__ == ('__main__'):
    app.run(debug=True)
