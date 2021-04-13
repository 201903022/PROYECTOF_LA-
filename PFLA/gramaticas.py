from graphviz import Source
class Gramatica: 
    def __init__(self,nombre,noTerminales,terminales,So,producciones): 
        self.nombre = nombre
        self.noTerminales = noTerminales
        self.terminales = terminales 
        self.So = So 
        self.producciones = producciones
    
    def getNombre(self): 
        return self.nombre
    
    def get_noTerminales(self): 
        return self.noTerminales

    def informacionGeneral(self,nombre): 
        print("Nombre de la Gramatica: ",self.nombre)
        print("No Terminales: {",(",".join(self.noTerminales)),"}")
        print("  Terminales: {",(",".join(self.terminales)),"}")
        print(" Estado Inicial: ",(",".join(self.So)))
        for elemen in self.producciones: 
            print(elemen[0])
            print(elemen[1])

    def pilaE(self,nombre): 
        imagen = True
        if imagen: 
            codigo = ''' digraph G {
                        rankdir="LR";
                        i->p[label="λ;λ;#"]
            ''' 
            pq = '      p->q[label="λ;λ;'+str(self.So) +'"] \n '
            codigo += pq
            labelq = ' " '
            for elemen in self.producciones:  
                labelq += '   λ;' + elemen[0]+';'+elemen[1].replace(" ","") + ' \n'

            labelq += ' " '
            codigo += '''q->q[label= '''+labelq+ ''']  '''
            codigo += '''   
                        node[shape="doublecircle"]      
                        q->f[label="λ;#;λ"]
                        
                    }  '''  
            nombre = self.nombre + "P"
            imagen= Source(codigo,filename=nombre,format="png")
            imagen.render()
        
        import webbrowser
        nombreW = self.nombre +"html.html"
        f = open(nombreW,mode="w", encoding="utf-8")
        mensaje = """<!DOCTYPE html>
        <html lang="en">
            <head>
            <link href="estilo1.css" rel="stylesheet" >
            <link href="estiloT.css" rel="stylesheet" >
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
            <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
            <title>Aplicacion de Prueba</title>
            </head>
            <body>
            <div class="sidenav">
            <div class="login-main-text">
                <h2>GRMATICAS LIBRE DE CONTEXTO<br> </h2>
                <p > """+self.nombre + """</p>
            </div>
        </div>
        <div class="main">
            <div class="col-md-6 col-sm-12">
                <div class="login-form">
                <h1>Mostrando</h1>
                <form>
            """
        alfabeto ="{"+ (",".join(self.terminales)) + (",".join(self.noTerminales))+"# }"
        mensaje +=""" 
                <div class="form-group">
                    <label> NOMBRE:  </label>
                    <input id = "username"type="text" class="form-control" value =  """ + str(self.nombre)+  """ onkeydown="return false" >  
                </div>   
                <div class="form-group">
                    <label> Terminales:  </label>
                    <input id = "username"type="text" class="form-control" value =  {""" + str((",".join(self.terminales)))+  """} onkeydown="return false" >                                          
                </div>       
                <div class="form-group">
                    <label> Alfabeto de pila de pila:  </label>
                    <input id = "username"type="text" class="form-control" value = """ + str(alfabeto)+  """ onkeydown="return false" >                                          
                </div>     
                <div class="form-group">
                    <label> Estados:  </label>
                    <input id = "username"type="text" class="form-control" value ="{i,p,q,f} " onkeydown="return false" >                                          
                </div>     
                <div class="form-group">
                    <label> Estado de Aceptación:  </label>
                    <input id = "username"type="text" class="form-control" value ="{f} " onkeydown="return false" >                                          
                </div>     
                <br>                                                                               
                <br  """  
  
        mensaje += """  
            </form>
            </div>
            <a href="tablaEntrada2.html">Tabla de Tokens</a>
            </div>
            </div>
            </body>
            </html>  
            """ 
        f.write(mensaje)
        f.close()    
        webbrowser.open_new_tab(nombreW)                            


    
        