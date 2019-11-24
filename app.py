import os
from threading import Thread

from flask import Flask, request, render_template, abort, Response
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

SENDER = 'notify.go.eco.grpup@gmail.com'
SENDER_PASS = '$Joo3m21$J'
RECIPIENTS = ['moskvichovoleg@gmail.com']

app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_DEBUG=False,
    MAIL_USERNAME=f'{SENDER}',
    MAIL_PASSWORD=f'{SENDER_PASS}',
    MAIL_DEFAULT_SENDER=f'{SENDER}',
    MAIL_MAX_EMAILS=None,
    MAIL_ASCII_ATTACHMENTS=False,
))

mail = Mail(app)


@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/order/', methods=['GET'])
def order():
    if request.method == 'GET':
        item = request.args.get('item')
        return render_template('order.html', item=item)


@app.route('/contacts/', methods=['GET'])
def contacts():
    if request.method == 'GET':
        return render_template('contacts.html')


@app.route('/success/', methods=['GET'])
def success():
    if request.method == 'GET':
        return render_template('success.html')


def send_email(msg):
    with app.app_context():
        mail.send(msg)


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


@app.route('/service-1/', methods=['GET'])
def service_1():
    if request.method == 'GET':
        return render_template('service-1.html')
    abort(405)


if __name__ == '__main__':
    app.run(debug=False)
