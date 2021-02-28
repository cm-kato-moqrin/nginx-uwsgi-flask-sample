from flask import Flask
import logging
app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route("/")
def hello():
    app.logger.info('Hello called!')
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run()
