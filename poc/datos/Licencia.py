
class Licencia(object):

    def __init__ (self, entrada):
        self.entrada = entrada
        self.nroLicencia = self.cortarLicencia()
        #self.clases = clases
        self.apellido = self.cortarApellido()
        self.nombre = self.cortarNombre()
        self.domicilio = self.cortarDomicilio()
        self.nacimiento = self.cortarNacimiento()
        #self.vencimiento =  sel 
    def getEntrada(self):
        return self.entrada
    def setEntrada(self, entrada):
        self.entrada = entrada
    def getNroLicencia(self):
        return self.nroLicencia
    def setNroLicencia(self,nroLicencia):
        set.nroLicencia = nroLicencia
    def getClases(self):
        return self.clases
    def setClases(self, clases):
        self.clases= clases

    def getApellido(self):
        return self.apellido

    def setApellido(self,apellido):
        self.apellido = apellido

    def  getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre= nombre

    def getDomicilio(self):
        return self.domicilio

    def setDomicilio(self, domicilio):
        self.domicilio = domicilio
        
    def getNacimiento(self):
        return self.nacimiento

    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento


    def getVencimiento(self):
        return self.vencimiento

    def setVencimiento(self, vencimiento):
        self.vencimiento =  vencimiento

    def cortarLicencia(self):
        pos = self.entrada.lower().find("1.apellido")
        lic = self.entrada[pos-9:pos-1]
        return(lic)

    def cortarApellido(self):
        pos = self.entrada.lower().find("last name")+11
        final=  self.entrada.lower().find("2.nombre")-2
        ap= self.entrada[pos : final]
        return (ap)
    
    def cortarNombre(self):
        pos = self.entrada.lower().find("first name")+12
        final = self.entrada.lower().find("8. domicilio")-2
        nom =  self.entrada[pos : final]
        return (nom)

    def cortarDomicilio(self):
        pos = self.entrada.lower().find("address")+9
        final = self.entrada.lower().find("3. fecha de nac")-34 ## revisar
        dom = self.entrada[pos : final]
        return (dom)

    def cortarNacimiento(self):
        pos = self.entrada.lower().find("date of birth")+16
        nac = self.entrada[pos:pos +12]
        return (nac)



    def __str__(self):
        return "Licencia : {}, Apellido: {}, Nombre: {}, Domicilio: {}, Fecha Nacimiento:{}".format(self.nroLicencia, self.apellido, self.nombre,self.domicilio, self.nacimiento)