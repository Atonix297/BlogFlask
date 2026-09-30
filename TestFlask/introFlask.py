from flask import Flask
app = Flask(__name__)



@app.route("/")
def hello():
    return "!Hola, Mundo!"


@app.route("/dam1")
def dam1():
    return "Estem a DAM1"


if __name__ == "__main__":
    app.run()