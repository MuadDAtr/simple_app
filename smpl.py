from flask import Flask 
from flask_restful import Resource, Api

app = Flask("Videos_API")

api = Api(app)

class Video(Resource):
    def get (self):
        return "Test"



api.add_resource(Video, '/')

if __name__ == '__main__':
    app.run()