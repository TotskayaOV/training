from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('seminar0204_base.html')

@app.route('/form/')
def form_list():
    return render_template('seminar0204_form.html')

@app.route('/result/<int:num>')
def result(num):
    context = num
    return render_template('seminar0204_result.html', result=num)

@app.route('/auth/', methods=['GET', 'POST'])
def check_text():
    if request.method == 'POST':
        user_text = request.form.get('user_text')
        if user_text:
            print(len(user_text.split()))
            return redirect(url_for('result', num=len(user_text.split())))
    else:
        return redirect(url_for('base'))

if __name__ == ('__main__'):
    app.run(debug=True)
