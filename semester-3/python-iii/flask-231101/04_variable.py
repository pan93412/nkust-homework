from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'C111156103 潘奕濬'


@app.route('/test')
def test():
    return '<html><body><h1>智商二甲 潘奕濬 C111156103</h1><p>Hello, World!</p></body></html>'


@app.route('/data')
def home():
    variables = {
        "text": "Yi-Jyun Pan",
        "info": {
            "性別": "Male",
            "年齡": 19,
            "學號": "C111156103",
            "專長": "Coding",
        },
        "countries": {
            "亞洲": ["台灣", "日本", "韓國"],
            "歐洲": ["英國", "法國", "德國"],
            "美洲": ["美國", "加拿大", "墨西哥"],
            "非洲": ["埃及", "剛果", "南非"],
            "大洋洲": ["澳洲", "紐西蘭", "斐濟"],
        }
    }

    return render_template('variable.html', **variables)


if __name__ == '__main__':
    app.run()
