from datetime import datetime

from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = ")PTT\E9&QmU$wX&}ex^Cz<pv{q]#ozMx0R,+P-~QI*b'9Q{k6O[eFOX.S}]wM#LT|2`T$0)56cwefd{zkFUlZvoj}efF#mH*#Il:tK/e]!qh{W37t,xGScQY#iJR1b{p"


@app.route("/session/<key>", methods=["POST"])
def write_session(key: str):
    value = request.form.get("value")

    session[key] = value
    session["last_updated_at"] = datetime.now().isoformat()

    return redirect(url_for("read_session", key=key))


@app.route("/session/<key>")
def read_session(key: str):
    print(session.values())
    value = session.get(key)

    if not value:
        return "Key not found", 404

    return {
        "value": value,
        "last_updated_at": session.get("last_updated_at"),
    }


if __name__ == "__main__":
    app.run(debug=True)
