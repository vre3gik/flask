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


@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                    <html lang="en">
                        <meta charset="utf-8">
                        <title>Колонизация</title>
                      <body>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                      <div class="alert alert-dark" role="alert">
                         Человечество вырастает из детства.
                      </div>
                      <div class="alert alert-success" role="alert">
                         Человечеству мала одна планета.
                      </div>
                      <div class="alert alert-dark" role="alert">
                         Мы сделаем обитаемыми безжизненные пока планеты.
                      </div>
                      <div class="alert alert-warning" role="alert">
                         И начнем с Марса!
                      </div>
                      <div class="alert alert-danger" role="alert">
                         Присоединяйся!
                      </div>
                      </body>
                    </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
