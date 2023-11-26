import json

from flask import render_template, redirect, url_for, Flask, request, make_response

app = Flask(__name__)


def retrieve_message() -> dict[str, dict[str, str]]:
    with open('static/data/message.json') as f:
        data = json.load(f)
        return data


def write_message(data: dict[str, dict[str, str]]):
    with open('static/data/message.json', 'w') as f:
        json.dump(data, f, indent=4)


@app.route('/api/app-info')
def get_app_info():
    message = retrieve_message()
    return message["appInfo"]


@app.route('/api/app-info', methods=['POST'])
def set_app_info():
    data = retrieve_message()

    for key, value in request.form.items():
        print(f"Writing {key} : {value} to appInfo")
        data["appInfo"][key] = value

    write_message(data)
    return data["appInfo"]


@app.route('/')
def index():
    message = retrieve_message()
    return render_template("api.html", data=message["appInfo"])


if __name__ == '__main__':
    app.run(debug=True)
