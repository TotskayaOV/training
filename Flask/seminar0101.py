from flask import Flask, render_template


app = Flask(__name__)

html1 = """
        <h1>Моя первая HTML-страница!</h1>
        <p>Привет мир!</p>
        """


@app.route("/")
def hello():
    return "Hello World"


@app.route("/about/")
def about():
    return "This is we"


@app.route("/contact/")
def contact():
    return "There is we"

@app.route("/summurize/<int:a>/<int:b>/")
def summurize(a, b):
    return f"{a}+{b}={a+b}"


@app.route("/len_str/<string:user_str>/")
def len_str(user_str):
    return f"{len(user_str)}"

@app.route("/html1/")
def first_html():
    return html1

@app.route("/html/")
def stud_html():
    students = ({'firstname': 'Ivanov', 'lastname': 'Petr', 'age': '18', 'score': '4,5'},
                {'firstname': 'Sidorov', 'lastname': 'Igor', 'age': '19', 'score': '3,5'},
                {'firstname': 'Petrov', 'lastname': 'Stas', 'age': '18', 'score': '5'})
    return render_template('students.html', stud_list=students)

@app.route("/news/<int:num>")
def news(num):

    base = [{'title': 'Title1', 'body': 'text', 'date_pub': '2023'},
            {'title': 'Title2', 'body': 'text2', 'date_pub': '2022'},
            {'title': 'Title3', 'body': 'text3', 'date_pub': '2021'}]
    context = base[num-1]
    return render_template('news.html', news=context)

if __name__ == "__main__":
    app.run(debug=True)
