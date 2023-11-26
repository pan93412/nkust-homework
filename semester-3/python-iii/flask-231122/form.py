from flask import render_template, redirect, url_for, Flask, request

app = Flask(__name__)


@app.route('/form')
def form_page():
    return render_template('form.html')


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        args = request.form.to_dict()
        print(f"post : {args}")
        return redirect(url_for('success', action='POST', **args))
    else:
        args = request.args.to_dict()
        print(f"get : {args}")
        return redirect(url_for('success', action='GET', **args))


@app.route('/success/<action>/<id>-<name>')
def success(action: str, id: str, name: str):
    return f'{action} : Welcome {id} {name} ~ !!!'


@app.route('/')
def index():
    return redirect(url_for('form_page'))


if __name__ == '__main__':
    app.run(debug=True)
