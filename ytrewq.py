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

                <h3>1.Какое животное считается самым быстрым на суше?</h3>

                <label>
                    <input type="radio" name="question1" value="Лев">
                    Лев
                </label>

                <label>
                    <input type="radio" name="question1" value="Гепард">
                    Гепард
                </label>

                <label>
                    <input type="radio" name="question1" value="Страус">
                    Страус
                </label>


                <h3>2.Кто из этих животных не умеет прыгать?</h3>

                <label>
                    <input type="radio" name="question2" value="Лягушка">
                    Лягушка
                </label>

                <label>
                    <input type="radio" name="question2" value="Слон">
                    Слон
                </label>

                <label>
                    <input type="radio" name="question2" value="Кролик">
                    Кролик
                </label>


                <h3>3.У какого животного самое длинное сердце относительно размера тела?</h3>

                <label>
                    <input type="radio" name="question3" value="У жирафа">
                    У жирафа
                </label>

                <label>
                    <input type="radio" name="question3" value="У кита">
                    У кита
                </label>

                <label>
                    <input type="radio" name="question3" value="У крокодила">
                    У крокодила
                </label>


                <h3>4.Какое из этих животных впадает в зимнюю спячку?</h3>

                <label>
                    <input type="radio" name="question4" value="Медведь">
                    Медведь
                </label>

                <label>
                    <input type="radio" name="question4" value="Заяц">
                    Заяц
                </label>

                <label>
                    <input type="radio" name="question4" value="Лиса">
                    Лиса
                </label>

                <h3>5.У кого из перечисленных животных нет голосовых связок, и они не умеют издавать звуки</h3>

                <label>
                    <input type="radio" name="question5" value="Дельфин">
                    Дельфин
                </label>

                <label>
                    <input type="radio" name="question5" value="Жираф">
                    Жираф
                </label>

                <label>
                    <input type="radio" name="question5" value="Кошка">
                    Кошка
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

    if answer1 == "Гепард":
        score += 1

    if answer2 == "Слон":
        score += 1

    if answer3 == "У жирафа":
        score += 1

    if answer4 == "Медведь":
        score += 1
    
    if answer5 == "Жираф":
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
