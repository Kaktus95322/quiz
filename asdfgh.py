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
                font-family: Arial;
                background: #eeeeee;
            }

            .quiz {
                width: 500px;
                margin: 50px auto;
                padding: 30px;
                background: white;
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

                <h3>1. Столица Франции?</h3>

                <label>
                    <input type="radio" name="question1" value="London">
                    Лондон
                </label>

                <label>
                    <input type="radio" name="question1" value="Paris">
                    Париж
                </label>

                <label>
                    <input type="radio" name="question1" value="Rome">
                    Рим
                </label>


                <h3>2. Сколько будет 4 + 4?</h3>

                <label>
                    <input type="radio" name="question2" value="6">
                    6
                </label>

                <label>
                    <input type="radio" name="question2" value="8">
                    8
                </label>

                <label>
                    <input type="radio" name="question2" value="10">
                    10
                </label>


                <h3>3. Какой язык используется в этом приложении?</h3>

                <label>
                    <input type="radio" name="question3" value="Java">
                    Java
                </label>

                <label>
                    <input type="radio" name="question3" value="Python">
                    Python
                </label>

                <label>
                    <input type="radio" name="question3" value="C++">
                    C++
                </label>


                <h3>4. Сколько пальцев на одной руке?</h3>

                <label>
                    <input type="radio" name="question4" value="9">
                    9
                </label>

                <label>
                    <input type="radio" name="question4" value="17">
                    17
                </label>

                <label>
                    <input type="radio" name="question4" value="4 + 2 - 1">
                    4 + 2 - 1
                </label>

                <h3>5.Что такое H2O? </h3>

                <label>
                    <input type="radio" name="question5" value="вода">
                    вода
                </label>

                <label>
                    <input type="radio" name="question5" value="уран">
                    Уран
                </label>

                <label>
                    <input type="radio" name="question5" value="кислород">
                    кислород
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

    if answer1 == "Paris":
        score += 1

    if answer2 == "8":
        score += 1

    if answer3 == "Python":
        score += 1

    if answer4 == "4 + 2 - 1":
        score += 1
    
    if answer5 == "вода":
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
