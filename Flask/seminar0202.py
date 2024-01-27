from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def base():
    return render_template('seminar0202_base.html')

@app.get('/upload/')
def upload_img():
    return render_template('seminar0202_upload.html')

@app.post('/upload/')
def upload_post():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
    return 'Файл отправлен'

if __name__ == ('__main__'):
    app.run(debug=True)
