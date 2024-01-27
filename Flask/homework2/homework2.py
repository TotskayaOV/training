from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    if float(age) < 18:
        return redirect(url_for('index'))
    else:
        response = make_response(redirect(url_for('greet')))
        response.set_cookie('user_data', f'name={name}&email={email}')
        return response

@app.route('/greet')
def greet():
    user_cookie = request.cookies.get('user_data')
    if user_cookie:
        user_data = dict(item.split('=') for item in user_cookie.split('&'))
        return render_template('greet.html', name=user_data['name'])
    else:
        return redirect(url_for('index'))

@app.route('/squaring/', methods=['GET', 'POST'])
def squaring():
    if request.method == 'POST':
        user_text = request.form.get('user_text')
        try:
            user_num = float(user_text)
            print(user_num * user_num)
            return redirect(url_for('result', num=(user_num * user_num)))
        except:
            return redirect(url_for('logout'))

    else:
        return redirect(url_for('logout'))

@app.route('/result/<float:num>')
def result(num):
    context = num
    return render_template('result.html', result=num)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('user_data', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
