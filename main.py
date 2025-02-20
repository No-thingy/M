from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Миссия Колонизация Марса<h1>'


@app.route('/index')
def ad():
    return '<h2>И на Марсе будут яблони цвести!</h2>'

@app.route('/promotion')
def promotion():
    return ('<p>Человечество вырастает из детства.</p>'
            '<p>Человечеству мала одна планета.</p>'
            '<p>Мы сделаем обитаемыми безжизненные пока планеты.</p>'
            '<p>И начнем с Марса!</p>'
            '<p>Присоединяйся!</p>')

@app.route('/image_mars')
def mission():
    return render_template('image_mars.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)