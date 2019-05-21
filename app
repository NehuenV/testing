from flask import Flask
from flask_restful import Resource, Api
import json
import requests
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
		

    def get(self):
    	var="entrada"
    	urlOrigen= "http://xxxx/1.jpg"
    	urlProcesada= "http://xxxx/2.jpg"
    	textOcr= "todo el contenido de la imagen en modo texto"
    	textCuit= "11-111111111-1"
    	textFecha= "11/11/2019"
    	textTotal= "583"
    	back= {'url': var, 'urlProcesada': urlProcesada,'textOcr':textOcr, 'textCuit':textCuit, 'textFecha':textFecha,'textTotal':textTotal}
    	return back

api.add_resource(HelloWorld, '/test')

#

if __name__ == '__main__':
    app.run(debug=True)
  #  main()
