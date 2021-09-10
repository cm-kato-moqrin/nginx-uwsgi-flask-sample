from flask import Flask
import logging
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
app = Flask(__name__)
app.logger.setLevel(logging.INFO)
xray_recorder.configure(service='demo flask-app')
XRayMiddleware(app, xray_recorder)


@app.route("/")
def hello():
    app.logger.info('Hello called!')
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run()
