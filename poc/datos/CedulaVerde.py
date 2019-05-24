class CedulaVerde():
	def __init__(self,texto):
		self.texto = texto
		self.dominio= self.cortarDominio()
		self.marca = self.cortarMarca()
		self.modelo =self.cortarModelo()
		self.tipo = self.cortarTipo ()
		self.uso = self.cortarUso()
		self.chasis = self.cortarChasis()
		self.motor = self.cortarMotor()

	def getTexto(self):
		return self.texto

	def setTexto(self, texto):
		self.texto=texto

	def getDominio(self):
		return self.dominio

	def setDominio(self, dominio):
		self.dominio = dominio

	def getMarca(self):
		return self.marca
	def setMarca(self, marca):
		self.marca= marca

	def getModelo(self):
		return self.modelo

	def setModelo(self, modelo):
		self.modelo = modelo

	def getTipo(self):
		return self.tipo

	def setTipo(self, tipo):
		self.tipo= tipo

	def getUso(self):
		return self.uso

	def setUso(self, uso):
		self.uso = uso 

	def getChasis(self):
		return self.chasis

	def setChasis (self, chasis):
		self.chasis= chasis

	def getMotor(self):
		self.motor

	def setMotor(self, motor):
		self.motor= motor

	def cortarDominio(self):
		ini= self.texto.lower().find("dominio")+8
		fin = self.texto.lower().find("marca")-1
		dom = self.texto[ini:fin]
		return (dom)

	def cortarMarca(self):
		ini= self.texto.lower().find("marca")+6
		fin = self.texto.lower().find("modelo")-2
		mar= self.texto[ini:fin]
		return (mar)

	def cortarModelo(self):
		ini=self.texto.lower().find("modelo")+7
		fin = self.texto.lower().find("tipo")-1
		return(self.texto[ini:fin])

	def cortarTipo(self):
		ini=self.texto.lower().find("tipo")+5
		fin = self.texto.lower().find("uso")-1
		return(self.texto[ini:fin])

	def cortarUso(self):
		ini=self.texto.lower().find("uso")+4
		fin = self.texto.lower().find("chasis")-1
		return(self.texto[ini:fin])
	
	def cortarChasis(self):
		ini=self.texto.lower().find("chasis")+7
		fin = self.texto.lower().find("motor")-1
		return(self.texto[ini:fin])

	def cortarMotor(self):
		ini=self.texto.lower().find("motor")+7
		fin = self.texto.lower().find("ntrole")-4
		return(self.texto[ini:fin])



	def __str__(self):
		return "Dominio: {}, Marca: {}, Modelo: {}, Tipo: {}, Uso: {}, Chasis: {}, Motor: {}".format(self.dominio,self.marca,self.modelo, self.tipo,self.uso, self.chasis,self.motor)
