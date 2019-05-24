class Ticket(object):

	def __init__(self,entrada):
	 	self.entrada = entrada
	 	self.cuit = self.getCuit()
	 	self.fecha = self.getFecha()
	 	self.total = self.getTotal()

	def getEntrada(self):
	 	return  self.entrada

	def setEntrada(self, entrada):
		self.entrada = entrada

	def setCuit(self,cuit ):
		self.cuit=cuit

	def setFecha(self, fecha):
		self.fecha = fecha

	def setTotal(self, total):
		self.total =total

	def getFecha(self):
		fechaPos= self.entrada.lower().find("fecha")+6
		fecha = self.entrada[fechaPos:fechaPos+8]
		return (fecha)

	def getCuit(self):
		cuitPos= self.entrada.lower().find("cuit")+11
		cuit = self.entrada[cuitPos:cuitPos+13]
		return (cuit)

	def getTotal(self):
		totalPos= self.entrada.lower().find("total")+6
		total=totalPos
		cont = 0
		flag=True
		while (flag==True):
			txt=self.entrada[totalPos+cont:totalPos+(cont+1)]
			if (txt=="1" or txt=="2" or txt=="3" or txt=="4" or txt=="5" or txt=="6" or txt=="7" or txt=="8" or txt=="9" or txt==","):
				totalPos=totalPos+1
				cont=cont+1
			else:
				flag=False
		return (self.entrada[total:totalPos+cont])

	def completar(self):
		self.setCuit(self.getCuit(self.entrada))
		self.setFecha(self.getFecha(self.entrada))
		self.setTotal(self.getTotal(self.entrada))

	def __str__(self):
		return "Cuit : {}, fecha: {}, total: {}".format(self.cuit, self.fecha, self.total)