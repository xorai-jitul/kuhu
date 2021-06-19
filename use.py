from flask import Flask,request
from flask_restx import Resource, Api
import json
import io
app = Flask(__name__)
api = Api(app, version='1.0', title='Xorai speech API',
    description='Speech App',)

ns = api.namespace('xorai_speech', description='Operations')
@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
@ns.route('/matching/<json:name>',methods=['GET','POST'])
@api.response(404, 'Invalid Input!')
class matching(Resource):

    def get(self, name):
        """Returns match output"""
        object=json.dumps(name)
        #result={'percent match':100}
        return object

if __name__ == '__main__':
    app.run(debug=True)