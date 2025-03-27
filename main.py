from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def first():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    fraza = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return "</br>".join(fraza)


@app.route("/image_mars")
def image_mars():
    return f'''<!doctype html>
                    <html lang="en">
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                        <div class="alert alert-success" role="alert">
                            <p>Вот она какая, красная планета.</p>
                        </div>
                      </body>
                    </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
