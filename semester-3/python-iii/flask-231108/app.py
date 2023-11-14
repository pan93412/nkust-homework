import base64
import os.path
import time

from flask import Flask, render_template, redirect, request, Response, url_for

app = Flask(__name__)


@app.context_processor
def utility_processor():
    import hashlib

    def integrity_for(filename: str):
        static_filename = os.path.join(app.static_folder, filename)

        try:
            with open(static_filename, "rb") as f:
                digest = hashlib.sha512(f.read()).digest()
                digest_b64 = base64.b64encode(digest).decode()
                return f"sha512-{digest_b64}"
        except Exception as e:
            print(e)
            return ""

    return dict(integrity_for=integrity_for)


@app.route("/redirect_example")
def redirect_example():
    max_redirect_count = 5

    try:
        redirect_count = int(request.args.get('times', '0'))
    except ValueError:
        return Response(status=400)

    if redirect_count >= max_redirect_count:
        return redirect("https://tw.yahoo.com")

    time.sleep(0.3)
    return Response(
        f"{max_redirect_count - redirect_count}…",
        status=302,
        headers={
            'Location': url_for('redirect_example', times=redirect_count + 1)
        }
    )


@app.route("/redirect/1")
def redirect_simple_example_01():
    time.sleep(1)
    return redirect("/redirect/2")


@app.route("/redirect/2")
def redirect_simple_example_02():
    time.sleep(1)
    return redirect("/redirect/3")


@app.route("/redirect/3")
def redirect_simple_example_03():
    time.sleep(1)
    return redirect("/redirect/4")


@app.route("/redirect/4")
def redirect_simple_example_04():
    time.sleep(1)
    return redirect("https://google.com")


@app.route("/example")
def example():
    return render_template('static.html')


if __name__ == '__main__':
    app.run()
