from flask import Flask 
from flask_restful import Resource, Api

app = Flask("Videos_API")

api = Api(app)


videos = {
    'vid_1': {'title': "Harry Potter"},
    'vid_2': {'title': "The Lord of The Rings"},
    'vid_3': {'title': "The Godfather"},
    'vid_4': {'title': "The Lion King"}

}

class Video(Resource):
    def get (self, video_id):
        return videos[video_id]



api.add_resource(Video, '/videos/<video_id>')

if __name__ == '__main__':
    app.run()