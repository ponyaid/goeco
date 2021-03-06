import jinja2
import socket
import os
from threading import Thread

from flask import Flask, request, render_template, abort, Response
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

SENDER = 'notify.go.eco.grpup@gmail.com'
SENDER_PASS = '$Joo3m21$J'
RECIPIENTS = ['go-eco.group@i.ua', 'moskvichovoleg@gmail.com']

app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_DEBUG=False,
    MAIL_USERNAME='%s' % SENDER,
    MAIL_PASSWORD='%s' % SENDER_PASS,
    MAIL_DEFAULT_SENDER='%s' % SENDER,
    MAIL_MAX_EMAILS=None,
    MAIL_ASCII_ATTACHMENTS=False,
))

mail = Mail(app)


def send_email(msg):
    with app.app_context():
        mail.send(msg)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    abort(405)


@app.route('/order/', methods=['GET'])
def order():
    if request.method == 'GET':
        item = request.args.get('item')
        return render_template('order.html', item=item)
    abort(405)


@app.route('/contacts/', methods=['GET'])
def contacts():
    if request.method == 'GET':
        return render_template('contacts.html')
    abort(405)


@app.route('/about/', methods=['GET'])
def about():
    if request.method == 'GET':
        return render_template('about.html')
    abort(405)


@app.route('/what/', methods=['GET'])
def what():
    if request.method == 'GET':
        return render_template('what.html')
    abort(405)


@app.route('/service/<int:num>', methods=['GET'])
def service(num):
    if request.method == 'GET':
        template = 'service-%d.html' % num
        return render_template(template)
    abort(405)


@app.route('/success/', methods=['GET'])
def success():
    if request.method == 'GET':
        return render_template('success.html')
    abort(405)


@app.route('/order_form/', methods=['POST'])
def order_form():
    if request.method == 'POST' and request.json:
        name = request.json.get('name')
        company = request.json.get('company')
        tel = request.json.get('tel')
        email = request.json.get('email')
        item = request.json.get('item')

        msg = Message('Новая заявка с сайта GO-ECO!',
                      sender=SENDER,
                      recipients=RECIPIENTS)

        body = 'Новая заявка с сайта GO-ECO! <br>' \
               'Имя: %s<br>' \
               'Компания: %s<br>' \
               'Телефон: %s<br>' \
               'Email: %s<br>' \
               'Что утилизировать: %s<br>' % (name, company, tel, email, item)

        msg.body = '%s' % body
        msg.html = "<b>%s</b>" % body

        Thread(target=send_email, args=(msg,)).start()

        return Response(status=200)
    else:
        abort(405)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def template_not_found(error):
    if issubclass(jinja2.exceptions.TemplateNotFound, socket.error):
        return render_template('404.html'), 500
    abort(500)


if __name__ == '__main__':
    app.run(debug=False)
