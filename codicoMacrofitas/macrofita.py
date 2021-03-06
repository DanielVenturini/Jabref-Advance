class Macrofita:
    def __init__(self, nomeEspecie):
        self.__nomeEspecie = nomeEspecie
        self.__floraID = ''
        self.__statusFlora = ''
        self.__nomeFlora = ''
        self.__statusPlantlist = ''
        self.__nomePlantlist = ''
        self.__floraXplantlist = ''
        self.__obsFlora = ''
        self.__obsPlantlist = ''
        self.__sinonimosFlora = []

    def saidaStringExcel(self):
        return [self.nomeEspecie, self.statusFlora, self.nomeFlora, self.obsFlora, self.statusPlantlist, self.nomePlantlist, self.obsPlantlist, self.floraXplantlist]

    def comaparaNome(self,site):
        if(site == 'flora'):
            if(self.nomeEspecie.replace(' ', '').lower() != self.nomeFlora.replace(' ', '').lower()):
                self.obsFlora = 'Autor Incorreto'
        elif(site == 'plantlist'):
            if(self.nomeEspecie.replace(' ', '').lower() != self.nomePlantlist.replace(' ', '').lower()):
                self.__obsPlantlist = 'Autor Incorreto' #nao mecher aki
            
    def comparaFloraPlantlist(self):
        if(self.nomeFlora and self.nomePlantlist and self.nomeFlora != self.nomePlantlist):
            self.floraXplantlist = 'Diferente'

    @property
    def floraID(self):
        return self.__floraID
    
    @floraID.setter
    def floraID(self, id):
        self.__floraID = id
    
    @property
    def nomeEspecie(self):
        return self.__nomeEspecie

    @property
    def statusFlora(self):
        return self.__statusFlora

    @property
    def nomeFlora(self):
        return self.__nomeFlora
    
    @property
    def statusPlantlist(self):
        return self.__statusPlantlist

    @property
    def nomePlantlist(self):
        return self.__nomePlantlist

    @property
    def floraXplantlist(self):
        return self.__floraXplantlist
        
    @property
    def obsFlora(self):
        return self.__obsFlora

    @property
    def obsPlantlist(self):
        return self.__obsPlantlist
    

    @statusFlora.setter
    def statusFlora(self, status):
        self.__statusFlora = status

    @statusPlantlist.setter
    def statusPlantlist(self, status):
        self.__statusPlantlist = status

    @nomeFlora.setter
    def nomeFlora(self, nome):
        self.__nomeFlora = nome
        
    @nomePlantlist.setter
    def nomePlantlist(self, nome):
        self.__nomePlantlist = nome

    @obsFlora.setter
    def obsFlora(self, obs):
        self.__obsFlora = obs

    @obsPlantlist.setter
    def obsPlantlist(self, obs):
        if(self.nomeFlora.__len__() == 0):
            self.__obsPlantlist = obs
    
    @floraXplantlist.setter
    def floraXplantlist(self, data):
        self.__floraXplantlist = data

    @property
    def sinonimosFlora(self):
        return self.__sinonimosFlora

    @sinonimosFlora.setter
    def sinonimosFlora(self, sinonimo):
        self.__sinonimosFlora = sinonimo
