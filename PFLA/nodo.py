from graphviz import Source
class nodo: 
    def __init__(self,id,nombre,terminales,noTerminales,estadoI,producciones): 
        self.nombre = nombre
        self.terminales = terminales 
        self.noTerminales = noTerminales
        self.estadoI = estadoI 
        self.producciones = producciones
        self.siguiente = None

class gramaticas: 
    def __init__(self): 
        self.primero = None
    
    def estaVacia(self): 
        if self.primero == None: 
            return True

    def printNombre(self): 
        tmp = self.primero
        if self.estaVacia(): 
            print("Vacia")
        else: 
            cont = 1
            while tmp is not None: 
                print("->",cont," ",tmp.nombre)
                tmp = tmp.siguiente
                cont += 1
   
    def nuevaGramatica(self,id,nombre,terminales,noTerminales,estadoI,producciones): 
       nuevo = nodo(id,nombre,terminales,noTerminales,estadoI,producciones)
       if self.estaVacia(): 
           self.primero = nuevo
       else: 
           tmp = self.primero
           while tmp is not None: 
               tmp = tmp.siguiente           
           tmp.siguiente = nuevo
        
    def getNodo(self,nombre): 
        tmp = self.primero
        while tmp is not None: 
            if tmp.nombre == nombre: 
                return tmp
            tmp = tmp.siguiente           

    def informacionGeneral(self,nombre): 
        tmp = self.getNodo(nombre)
        print("Nombre de la Gramatica: ",tmp.nombre)
        print("No Terminales: {",(",".join(tmp.noTerminales)),"}")
        print("  Terminales: {",(",".join(tmp.terminales)),"}")
        print(" Estado Inicial: ",(",".join(tmp.estadoI)))
        for elemen in tmp.producciones: 
            print(elemen[0])
            print(elemen[1])

    def pilaE(self,nombre): 
        tmp = self.getNodo(nombre)
        print(tmp)
        codigo = ''' digraph G {
                rankdir="LR";
                i->p[label="λ;λ;#"]
        ''' 
        pq = '  p->q[label="λ;λ;'+str(tmp.estadoI) +'"] '
        codigo += pq
        estadoq = '"'
        for elemen in tmp.producciones: 
            estadoq += 'q->q[label="λ;'+elemen[0]+';'+elemen[1] +'"]'
        estadoq += '"'

        codigo += estadoq        
        codigo += '''         
                q->f[label="λ;#;λ"]
                    
                }  '''  
        nombre = tmp.nombre + "P"
        imagen= Source(codigo,filename=nombre,format="png")
        imagen.render()


            
    
        