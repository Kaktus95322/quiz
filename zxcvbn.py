from flask import Flask, request
import sqlite3

app = Flask(__name__)


def create_database():
    connection = sqlite3.connect("quiz.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta charset="UTF-8">
        <title>Викторина</title>

        <style>
            body {
                font-family: segoe print;
                background: #e5e5e5;
            }

            .quiz {
                width: 500px;
                margin: 50px auto;
                padding: 30px;
                background: #fafafa;
                border-radius: 10px;
            }

            h1 {
                color: #333333;
            }

            label {
                display: block;
                margin: 10px 0;
            }

            input[type="text"] {
                width: 100%;
                padding: 10px;
                box-sizing: border-box;
            }

            button {
                margin-top: 20px;
                padding: 10px 20px;
                background: #4285f4;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            button:hover {
                background: #2867c7;
            }
        </style>
    </head>

    <body>

        <div class="quiz">

            <h1>Викторина</h1>

            <form action="/check" method="POST">

                <p>Твоё имя:</p>
                <input type="text" name="name" required>

                <h3>1.Что выведет этот код?
                "print(type(3.14))"</h3>

                <label>
                    <input type="radio" name="question1" value="<class 'int'>">
                    class 'int'
                </label>

                <label>
                    <input type="radio" name="question1" value="<class 'float'>">
                    class 'float'
                </label>

                <label>
                    <input type="radio" name="question1" value="<class 'decimal'>">
                    class 'decimal'
                </label>


                <h3>2.Какой оператор в Python используется для возведения в степень?</h3>

                <label>
                    <input type="radio" name="question2" value="**">
                    **
                </label>

                <label>
                    <input type="radio" name="question2" value="/">
                    /
                </label>

                <label>
                    <input type="radio" name="question2" value="###">
                    ###
                </label>


                <h3>3.Что произойдёт при выполнении этого кода?
                "my_list = [1, 2, 3]
                my_list[3] = 4"</h3>

                <label>
                    <input type="radio" name="question3" value="Список станет [1, 2, 3, 4]">
                    Список станет [1, 2, 3, 4]
                </label>

                <label>
                    <input type="radio" name="question3" value="Ничего не произойдёт, код просто игнорируется">
                    Ничего не произойдёт, код просто игнорируется
                </label>

                <label>
                    <input type="radio" name="question3" value="Вылетит ошибка">
                    Вылетит ошибка
                </label>


                <h3>4.Какая конструкция используется для обработки исключений в Python?</h3>

                <label>
                    <input type="radio" name="question4" value="handle...error">
                    handle...error
                </label>

                <label>
                    <input type="radio" name="question4" value="if...else">
                    if...else
                </label>

                <label>
                    <input type="radio" name="question4" value="try...except">
                    try...except
                </label>

                <h3>5.Что вернёт выражение 5 // 2 в Python?</h3>

                <label>
                    <input type="radio" name="question5" value="2.5">
                    2.5
                </label>

                <label>
                    <input type="radio" name="question5" value="2">
                    2
                </label>

                <label>
                    <input type="radio" name="question5" value="3">
                    3
                </label>

                <button type="submit">
                    Проверить
                </button>

            </form>

        </div>

    </body>
    </html>
    """


@app.route("/check", methods=["POST"])
def check():

    name = request.form["name"]

    answer1 = request.form.get("question1")
    answer2 = request.form.get("question2")
    answer3 = request.form.get("question3")
    answer4 = request.form.get("question4")
    answer5 = request.form.get("question5")

    score = 0

    if answer1 == "<class 'float'>":
        score += 1

    if answer2 == "**":
        score += 1

    if answer3 == "Вылетит ошибка":
        score += 1

    if answer4 == "try...except":
        score += 1
    
    if answer5 == "2":
        score += 1

    connection = sqlite3.connect("quiz.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO results (name, score) VALUES (?, ?)",
        (name, score)
    )

    connection.commit()
    connection.close()

    return f"""
    <!DOCTYPE html>
    <html lang="ru">

    <head>
        <meta charset="UTF-8">
        <title>Результат</title>

        <style>
            body {{
                font-family: Arial;
                background: #eeeeee;
                text-align: center;
            }}

            .result {{
                width: 400px;
                margin: 100px auto;
                padding: 30px;
                background: white;
                border-radius: 10px;
            }}

            a {{
                color: #4285f4;
            }}
        </style>

    </head>

    <body>

        <div class="result">

            <h1>Результат</h1>

            <h2>{name}</h2>

            <p>Ты набрал:</p>

            <h1>{score} из 5</h1>

            <a href="/">Пройти ещё раз</a>

        </div>

    </body>
    </html>
    """


create_database()

app.run(debug=True)
