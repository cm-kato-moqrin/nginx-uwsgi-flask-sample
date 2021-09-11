from flask import Flask
from flask_restful import Resource, Api
import logging
import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
api = Api(app)
xray_recorder.configure(service='demo flask-app')
XRayMiddleware(app, xray_recorder)


class Hello(Resource):
    def get(self):
        name = os.environ["NAME"]
        app.logger.info('Hello called!')
        return {'hello': name}


api.add_resource(Hello, '/')

if __name__ == "__main__":
    app.run()
