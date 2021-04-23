from graphviz import Source
class GramaticaE: 
    def __init__(self,id,nombre,noTerminales,terminales,So,producciones,error): 
        self.id = id
        self.nombre = nombre
        self.noTerminales = noTerminales
        self.terminales = terminales 
        self.So = So 
        self.producciones = producciones
        self.error = error
    def getID(self): 
        return self.id
    
    def getNombre(self): 
        return self.nombre
        
    def get_noTerminales(self): 
        return self.noTerminales
    
    def get_Teminales(self): 
        return self.terminales
    
    def get_Producciones(self): 
        return self.producciones
        
    def getError(self): 
        return self.error

      