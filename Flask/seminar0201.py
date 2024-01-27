from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('seminar0201_first.html')

@app.route('/next_page/')
def next_page():
    return render_template('seminar0201_next.html')

if __name__ == '__main__':
    app.run(debug=True)
