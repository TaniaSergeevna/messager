from flask import Flask, request
import time

app = Flask(__name__)
messages = [
    {'username': 'Jack', 'text': '', 'time': time.time()},
    {'username': 'Mary', 'text': '', 'time': time.time()}
]

users = {
    # username: password
    'Mary': '999',
    'Jack': '123'
}


# @app.route("/")
# def hello():
#     return "Hello,World!"
#
#
# @app.route("/status")
# def status():
#     tim = datetime.datetime.now()
#     return {
#         'status': True,
#         "time": "{0}:{1}:{2}".format(tim.hour, tim.minute, tim.second)
#     }


@app.route("/history")
def history():
    after = float(request.args['after'])

    filter_messages = []
    for message in messages:
        if after < message['time']:
            filter_messages.append(message)

    return {"messages": filter_messages}


@app.route("/send", methods=["POST"])
def send():
    data = request.json
    username = data['username']
    password = data['password']
    text = data['text']

    if username in users:
        real_password = users[username]
        if real_password != password:
            return {'ok': True}
    else:
        users[username] = password

    messages.append({'username': username,
                     'text': text,
                     'time': time.time()
                     })

    return {'ok': True}


app.run()
