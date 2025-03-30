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


@app.route("/choice/<planet_name>")
def choice(planet_name):
    style = ["alert-success", "alert-dark", "alert-danger", "alert-warning"]
    opisanie = {"марс": [("Эта планета близка к Земле;", 2),
                         ("На ней много необходимых ресурсов;", 1),
                         ("На ней есть вода и атмосфера;", 2),
                         ("На есть небольшое магнитное поле;", 4),
                         ("Наконец, она просто красива!", 3)],
                "земля": [("Эта наша любимая планета;", 4),
                          ("На ней мы живем;", 2),
                          ("Она красива;", 3),
                          ("И неповторима;", 1),
                          ("И прекрасна!", 2)],
                "юпитер": [("Эта планета находится после марса;", 3),
                           ("Она очень интересна;", 4),
                           ("И неизвестна;", 1),
                           ("Понятия не имею, что сюда написать", 4),
                           ("Хорошая планета!", 2)],
                "сатурн": [("Сатурн находится после юпитера;", 2),
                           ("Это очень большая планета;", 3),
                           ("О ней я ничего не знаю;", 1),
                           ("На ней есть что то", 4),
                           ("Не очень хорошая планета", 3)],
                "уран": [("Эта планета находится после сатурна;", 2),
                         ("Она чуть больше, чем земля;", 3),
                         ("На есть небольшое магнитное поле", 1),
                         ("Уран это хим элемент", 2),
                         ("2,9 млрд км от земли", 4)],
                "нептун": [("Эта планета рядом с ураном;", 4),
                           ("На нём очень холодно;", 4),
                           ("На есть небольшое магнитное поле;", 1),
                           ("Эта планета дальше всех от солнца!", 2),
                           ("Диаметр превышает земной в 3,9 раза!", 3)],
                "венера": [("Эта планета рядом с землей;", 3),
                           ("Есть песня ты венера я юпитер ты москва я питер :);", 4),
                           ("На есть магнитное поле;", 1),
                           ("Она находится почти ближе всех к солнцу!", 3),
                           ("Радиус: 6 051,8 км", 2)],
                "меркурий": [("Эта планета рядом с венерой;", 2),
                             ("На ней жарко;", 4),
                             ("На есть небольшое магнитное поле;", 1),
                             ("Эта планета ближе всех к солнцу!;", 3),
                             ("Конец!", 1)]}
    if planet_name.lower() not in opisanie:
        return f"<h2>Возможно вы ввели название несуществующей планеты({planet_name})</h2>"
    res_opesanie = opisanie[planet_name.lower()]
    styles = list(map(lambda x: style[x[1] - 1], res_opesanie))
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <div class="alert {styles[0]}" role="alert">
                         <h5>{res_opesanie[0][0]}</h5>
                        </div>
                        <div class="alert {styles[1]}" role="alert">
                         <h5>{res_opesanie[1][0]}</h5>
                        </div>
                        <div class="alert {styles[2]}" role="alert">
                         <h5>{res_opesanie[2][0]}</h5>
                        </div>
                        <div class="alert {styles[3]}" role="alert">
                         <h5>{res_opesanie[3][0]}</h5>
                        </div>
                        <div class="alert {styles[4]}" role="alert">
                         <h5>{res_opesanie[4][0]}</h5>
                        </div>
                      </body>
                    </html>'''


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
