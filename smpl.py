from flask import Flask 
from flask_restful import Resource, Api

app = Flask("Videos_API")

api = Api(app)


videos = {
    'vid_1': {'title': "Harry Potter"},
    'vid_2': {'title': "The Lord of The Rings"},
    'vid_3': {'title': "The Godfather"}

}

class Video(Resource):
    def get (self):
        return videos



api.add_resource(Video, '/')

if __name__ == '__main__':
    app.run()