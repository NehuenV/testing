from datos.Ocr import Ocr
from datos.Ticket import Ticket
from datos.CedulaVerde import CedulaVerde
from datos.Licencia import Licencia
from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask import jsonify

app = Flask(__name__)
@app.route('/cedula')

def ticket():
	ocrC=Ocr("Cedula.jpg")
	texto=ocrC.imagenATexto()
	cedulav=CedulaVerde(texto)
	return jsonify({'Dominio': cedulav.cortarDominio(), 'Marca': cedulav.getMarca(), 'Modelo': cedulav.getModelo(), 'Tipo': cedulav.getTipo(), 'Uso': cedulav.getUso(), 'Chasis': cedulav.getChasis(), 'Motor':cedulav.getMotor()} )

@app.route('/licencia')
def licencia():
	ocr = Ocr("Licencia.jpg")
	texto = ocr.imagenATexto()
	licencia = Licencia(texto)
	back= {'Licencia':licencia.getNroLicencia(), 'Apellido':licencia.getApellido(), 'Nombre': licencia.getNombre(), 'Domicilio': licencia.getDomicilio(), 'Fecha Nacimiento':licencia.getNacimiento()}
	return jsonify(back)

@app.route('/ticket')
def tkt():
	ocrT=Ocr("ticket.jpeg")
	txt=ocrT.imagenATexto()
	ticket=Ticket(txt)
	back= {'cuit': ticket.getCuit(), 'fecha': ticket.getFecha(),'total':ticket.getTotal()}
	return jsonify(back)


if __name__=='__main__':
	app.run(debug=True)
