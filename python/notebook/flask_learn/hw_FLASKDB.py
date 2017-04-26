from flask import Flask, render_template


app = Flask(__name__)

@app.route('/list')
def render(name=None):
    return render_template("dongari_index.html", name = name)


if __name__ == '__main__':
    app.run(host = '0.0.0.0')