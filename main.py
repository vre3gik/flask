from flask import Flask, url_for, request

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


@app.route("/astronaut_selection", methods=["POST", "GET"])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styleform.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h3>на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="education" name="education">
                                          <option>Начальное</option>
                                          <option>Основное (общее)</option>
                                          <option>Среднее (полное) общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <label for="classSelect"></label>
                                    <label for="classSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules1" name="in_is">
                                        <label class="form-check-label" for="acceptRules1">Инженер-исследователь</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules2" name="pil">
                                        <label class="form-check-label" for="acceptRules2">Пилот</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules3" name="sto">
                                        <label class="form-check-label" for="acceptRules3">Строитель</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules4" name="exb">
                                        <label class="form-check-label" for="acceptRules4">Экзобиолог</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="in_tr">
                                        <label class="form-check-label" for="acceptRules5">Врач</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules5" name="in_tr">
                                        <label class="form-check-label" for="acceptRules5">Инженер по терраформированию</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules7" name="klim">
                                        <label class="form-check-label" for="acceptRules7">Климатолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules9" name="prf_rad_arm">
                                        <label class="form-check-label" for="acceptRules9">Специалист по радиационной защите</label>
                                     </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules10" name="astrg">
                                        <label class="form-check-label" for="acceptRules10">Астрогеолог</label>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules11" name="shtur">
                                        <label class="form-check-label" for="acceptRules11">Гляциолог</label>
                                    </div>
                                    <label for="classSelect"></label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="answer" rows="3" name="answer"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == "POST":
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
