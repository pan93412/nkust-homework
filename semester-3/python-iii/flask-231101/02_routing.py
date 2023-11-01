from flask import Flask

app = Flask(__name__)


@app.route('/data/appInfo/<name>', methods=['GET'])
def get_name(name: str):
    return f'Hello, {name}'


@app.route('/data/appInfo/id/<int:number>', methods=['GET'])
def school_number(number: int):
    return f'Your school number is: {number}'


@app.route('/data/appInfo/age/<float:age>', methods=['GET'])
def get_age(age: float):
    return f'Your age is: {age}'


if __name__ == '__main__':
    app.run()
