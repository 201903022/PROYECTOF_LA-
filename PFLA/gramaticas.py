from graphviz import Source
from graphviz import Graph
from graphviz import Digraph
class Gramatica: 
    def __init__(self,id,nombre,noTerminales,terminales,So,producciones): 
        self.id = id
        self.nombre = nombre
        self.noTerminales = noTerminales
        self.terminales = terminales 
        self.So = So 
        self.producciones = producciones
        self.transicionPila = None
    
    def getNombre(self): 
        return self.nombre
    
    def getID(self): 
        return self.id
    
    def get_noTerminales(self): 
        return self.noTerminales

    def informacionGeneral(self): 
        print("Nombre de la Gramatica: ",self.nombre)
        print("No Terminales: {",(",".join(self.noTerminales)),"}")
        print("Terminales: {",(",".join(self.terminales)),"}")
        print("Estado Inicial: ",(",".join(self.So)))
        comparar = ""
        duply = self.producciones.copy()
        contador = 0
        inicio = True
        formato = ""
        tabulacion = ""
        while len(duply)>0:
            if inicio: 
                formato += duply[contador][0] +" -> " + duply[contador][1]
                comparar = duply[contador][0]
                duply.pop(contador)
                inicio = False
                for x in range(0,len(comparar)): 
                    tabulacion +=" "
                tabulacion = "  | " 
                if len(duply) == 0: 
                    print(formato)
            else: 
                if contador == len(duply): 
                    print(formato)
                    contador = 0
                    inicio = True  
                    formato = ""              
                elif duply[contador][0] == comparar: 
                    formato += "\n " + tabulacion + duply[contador][1]
                    duply.pop(contador)  
                    if len(duply) == 0: 
                        print(formato)

                else:                     
                    contador +=1
                    if contador ==  len(duply): 
                        print(formato)
                        contador = 0
                        inicio = True
                        formato = ""              

    def pilaE(self): 
        imagen = True
        dot = Digraph('html',format='svg')
        
        nombreI = self.nombre + "P"
        imagen = False
        if imagen: 
            codigo = ''' digraph G {
                        rankdir="LR";.

                        i->p[label="λ;λ;#"]
            ''' 
            pq = '      p->q[label="λ;λ;'+str(self.So) +'"] \n '
            codigo += pq
            labelq = ' " '
            for elemen in self.producciones:  
                labelq += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + ' \n'
            
            labelq += ' \n '

            for elemen in self.terminales: 
                labelq += "- "+elemen + ","+elemen+","+"λ \n"

            labelq += ' " '
            codigo += '''q->q[label= '''+labelq+ ''']  '''
            codigo += '''   
                        node[shape="doublecircle"]      
                        q->f[label="λ;#;λ"]
                        
                    }  '''  
            imagen= Source(codigo,filename=nombreI,format="png")
            imagen.render()
        svg = True 
        if svg: 
            dot.graph_attr['rankdir'] = 'LR'
            dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightblue' )
            dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightblue' )
            dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightblue' )
            dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightblue' )
            dot.edge('i','p',label= '< λ;λ;#>',fontcolor='green')
            dot.edge('p','q',label= '< λ;λ;' +self.So+' >',fontcolor='green')
            produccionesP = ""
            for elemen in self.producciones:  
                produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
            tipo3 = " "
            for elemen in self.terminales: 
                tipo3 += elemen + ","+elemen+","+"λ <BR/>"    
            dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >',fontcolor='green')
            dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >',fontcolor='green')
            dot.edge('q','f',label= '<λ;λ;#>',fontcolor='green')

        web = True
        if web: 
            import webbrowser
            nombreW = self.nombre +"html.html"
            f = open(nombreW,mode="w", encoding="utf-8")
            mensaje = """<!DOCTYPE html>
                <html lang="en">
                <head>
                <link href="estilo1.css" rel="stylesheet" >
                <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
                <title>Aplicacion de Prueba</title>
                </head>
                <body>
                <div class="sidenav">
                <div class="login-main-text">
                    <h2>NOMBRE: """+self.nombre + """<br> </h2>
                    <p >GRMATICAS LIBRE DE CONTEXTO</p>
                </div>
                </div>
                <div class="main">
                <div class="col-md-6 col-sm-12">
                    <div class="login-form">
                    <h1>Mostrando</h1>
                    <form>
                """
            alfabeto ="{"+ (",".join(self.terminales)) + ","+(",".join(self.noTerminales))+",#} "
            mensaje +=""" 
                    <div class="form-group">
                        <label> NOMBRE:  </label>
                        <input id = "username"type="text" class="form-control" value =  """ + str(self.nombre)+  """ onkeydown="return false" >  
                    </div>   
                    <div class="form-group">
                        <label> Terminales:  </label> 
                        <input id = "username"type="text" class="form-control" value =  {""" + str((",".join(self.terminales)) + "}")+  """  onkeydown="return false" >                                          
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
                    <br>  """  
            name_imagen = str(nombreI)+ ".png"
            mensaje += """  
                <h1>Representacion Grafica SVG</h1>
               """  + dot.pipe().decode('utf-8') + """
                </form>
                </div>
                </div>
                </div>
                </body>
                </html>  
                """ 
            f.write(mensaje)
            f.close()    
            webbrowser.open_new_tab(nombreW)                            

    def generaTablas(self,entrad): 
        import webbrowser
        nombreW = self.nombre +"Prueba.html"
        f = open(nombreW,mode="w", encoding="utf-8")
        seAcepta = True
        global ERROR 
        estaodoActual = ""
        estoadoNext = ""
        tabla = []#[[iteracion,pila,entrada,[Transiciones]]]
        entrada = str(entrad) + "#"
        tamaño_entrada = len(entrada)
        pila = []
        iteracion = 0
        cont = 0 
        estado = "i"
        import webbrowser
        self.listas()
        mensaje = """<!DOCTYPE html>
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <link href="estilosTablas.css" rel="stylesheet" >
                <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
                <title>Aplicacion de Prueba</title>
                </head>
                <body>
                <div class="sidenav">
                <div class="login-main-text">
                    <h1>"""+self.nombre + """<br> </h1>
                    <h1> Cadena: """+entrada+ """</h1>
                </div>
            </div>
            <div class="main">
                <div class="col-md-6 col-sm-12">
                    <div class="login-form">
                    <h1>Tabla </h1>
                    <form>
                """        
                
        while (cont < tamaño_entrada): 
            char = entrada[cont]
            if estado == "i": 
                pila.append("#")
                estadoA = estado
                estado = "p"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ pila[0] + ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(" ")
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())
                temp.clear()
                apila = "#"
                iteracion += 1 

            elif estado == "p":
                inPila = ""
                for elemen in pila: 
                    inPila += elemen
                temp = []
                temp.extend(str(self.So))
                temp.extend(pila)
                pila = temp.copy() 
                estadoA = estado                       
                estado = "q"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ self.So+ ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(str(inPila))
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())                
                temp.clear()
                iteracion += 1 
            elif estado == "q":
                pilaTop = pila[0]
                if pilaTop in self.noTerminales and char in self.terminales:                     
                    reglas = self.transicionPila[pilaTop]
                    if len(reglas)==1: 
                        inPila = ""
                        for elemen in pila.copy(): 
                            inPila += elemen                           
                        pila.pop(0)
                        temp = []
                        temp.extend(reglas[0])
                        temp.extend(pila)
                        pila = temp.copy()  
                        transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(reglas[0]))+ ")" 
                        temp1 = []    
                        temp1.append(str(iteracion))
                        temp1.append(str(inPila))
                        temp1.append(str(char))
                        temp1.append(transicion)
                        tabla.append(temp1.copy())  
                    else: 
                        find = False
                        for regla in reglas: 
                            if regla[0] == char: 
                                inPila = ""
                                for elemen in pila.copy(): 
                                    inPila += elemen                                   
                                pila.pop(0)
                                temp = []
                                temp.extend(regla)
                                temp.extend(pila)
                                pila = temp.copy()
                                transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(regla))+ ")" 
                                temp1 = []    
                                temp1.append(str(iteracion))
                                temp1.append(str(inPila))
                                temp1.append(str(char))
                                temp1.append(transicion)
                                tabla.append(temp1.copy())  
                                temp1.clear()                              
                                find = True

                        if not find: 
                            for regla in reglas:
                                if regla[0] in self.noTerminales: 
                                    inPila = ""
                                    for elemen in pila.copy(): 
                                        inPila += elemen                                 
                                    pila.pop(0)
                                    temp = []
                                    temp.extend(regla)
                                    temp.extend(pila)
                                    pila = temp.copy()
                                    transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(regla))+ ")" 
                                    temp1 = []    
                                    temp1.append(str(iteracion))
                                    temp1.append(str(inPila))
                                    temp1.append(str(char))
                                    temp1.append(transicion)
                                    tabla.append(temp1.copy())  
                                    temp1.clear()                              
                                    find = True

                        if not find: 
                            print("Error sintactico")
                            seAcepta = False
                            ERROR = "Error sintactico en la escritura de gramatica"
                            break

                elif pilaTop in self.terminales: 
                    if pilaTop == char: 
                        inPila = ""
                        for elemen in pila.copy(): 
                            inPila += elemen                          
                        pila.pop(0)
                        transicion = "("+estado+"," +char+","+ pilaTop+";"+estado+",λ)" 
                        temp1 = []    
                        temp1.append(str(iteracion))
                        temp1.append(str(inPila))
                        temp1.append(str(char))
                        temp1.append(transicion)
                        tabla.append(temp1.copy())  
                        temp1.clear()         
                        cont += 1
                    else: 
                        print("Pila top: ",pilaTop)
                        print("char: ",char)
                        print("Error no encontrado")
                        seAcepta = False 
                        ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                        # ERROR += concatenarError
                        print("Error, ",ERROR)
                        print("Tabla")
                        for table in tabla: 
                            print(" | ".join(table))
                        break 

                elif pilaTop =="#" and char =="#":
                    inPila = ""
                    for elemen in pila.copy(): 
                        inPila += elemen                     
                    pila.pop(0) 
                    estaodoActual = estado 
                    estado = "f"
                    estoadoNext = estado
                    transicion = "("+estaodoActual+",λ,"+ pilaTop+";"+estoadoNext+",λ)" 
                    temp1 = []    
                    temp1.append(str(iteracion))
                    temp1.append(str(inPila))
                    temp1.append(str("λ"))
                    temp1.append(transicion)
                    tabla.append(temp1.copy())  
                    temp1.clear()                       
                else: 
                    print("Error en, ",char," pos: ",cont," no encontrado")
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" no encontrado"
                    seAcepta = False
                    for table in tabla: 
                        print(" | ".join(table))                    
                    break                                                
                iteracion += 1 
            elif estado == "f": 
                cont +=1
                if cont == tamaño_entrada: 
                    temp1 = []    
                    temp1.append(str(iteracion))
                    temp1.append(str("λ"))
                    temp1.append(str("λ"))
                    temp1.append(str("f"))
                    tabla.append(temp1.copy())  
                    temp1.clear()                          
                else: 
                    print("Error pila queda: ",pila)
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" PILA"
                    seAcepta = False
                break
        
        #crear tabla
        mensaje +=   """ 
            <table id="customers">
                        <tr>
                            <th>Iteracion</th>
                            <th>Pila <br><-- </th>
                            <th>Entrada</th>
                            <th>Transiciones</th>
                        </tr>                
         """

        for table in tabla: 
            print(" | ".join(table))
        
            mensaje +=   """ 
                <tr>
                   <td>"""+table[0]+""" </td>
                   <td>"""+table[1]+""" </td>
                   <td>"""+table[2]+""" </td>
                   <td>"""+table[3]+""" </td>
                </tr>
            """
            
        mensaje +=   """ 
            </table>
         """
        if seAcepta: 
            print("Se acepta: ")
            mensaje +=""" <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                    LA CADENA ES ACEPTADA.</p>"""
        else: 
            print("No se acepta ")
            mensaje +=""" <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                    LA CADENA NO ES ACEPTADA POR: <br>"""+ERROR+""" .</p>"""

        mensaje += """                      
                </form>
                </div>
                </div>
                </div>
                </body>
                </html>  
            """ 
        f.write(mensaje)
        f.close()    
        webbrowser.open_new_tab(nombreW)    
    
    def getLast(self,lista): 
        lastT = len(lista) -1
        last = lista[lastT]
        return last

    def generRecorridoImagenes(self,entrad): 
        entrada = str(entrad)+"#"
        tamaño_entrada = len(entrada)
        pila = []
        tabla = []
        iteracion = 0
        cont = 0 
        estado = "i"
        seAcepta = True
        import webbrowser
        nombreW = self.nombre +"Recorrido.html"
        f = open(nombreW,mode="w", encoding="utf-8")
        self.listas()   
        mensaje = """<!DOCTYPE html>
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <link href="estiloR.css" rel="stylesheet" >
                <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
                <title>Aplicacion de Prueba</title>
                </head>
                <body>
                <div class="sidenav">
                <div class="login-main-text">
                    <h1>Nomre AP: """+self.nombre + """<br> </h1>
                    <h1> Cadena: """+entrada+ """</h1>
                </div>
            </div>
            <div class="main">
                <div class="col-md-6 col-sm-12">
                    <div class="login-form">
                    <h1>Imagenes:  </h1>
                    <form>
                """                 
        while (cont < tamaño_entrada): 
            char = entrada[cont]
            if estado == "i": 
                svg = True
                dot = Digraph('html',format='svg')
                if svg: 
                    dot.graph_attr['rankdir'] = 'LR'
                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='yellow' )
                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                    dot.edge('i','p',label= '< λ;λ;#>',fontcolor='red')
                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                    produccionesP = ""
                    for elemen in self.producciones:  
                        produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                    tipo3 = " "
                    for elemen in self.terminales: 
                        tipo3 += ""+elemen + ","+elemen+","+"λ <BR/>"    
                    dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                    dot.edge('q','f',label= '<λ;λ;#>')                             
                
                pila.append("#")
                estadoA = estado
                estado = "p"
                mensaje += """"<hr width="200%" size=5000 color="black">
                 <h1 align="center"> Iteración """+str(iteracion)+""": </h1>  
                                 
                 """ + dot.pipe().decode('utf-8') +"""
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Pila:      </td>
                        <td class="aaa">      vacia </td>
                        </tr>
                        </tfoot>
                        </table>     
                        <br>  
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Entrada:    </td>
                        <td class="aaa">      """+ char + """  </td>
                        </tr>
                        </tfoot>
                        </table>                                         
                   """
                iteracion += 1 

            elif estado == "p":
                inPila = ""
                for elemen in pila: 
                    inPila += elemen
                temp = []
                temp.extend(str(self.So))
                temp.extend(pila)
                pila = temp.copy() 
                estadoA = estado                       
                estado = "q"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ self.So+ ")"
                svg = True
                dot = Digraph('html',format='svg')
                if svg: 
                    dot.graph_attr['rankdir'] = 'LR'
                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='yellow')
                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                    dot.edge('i','p',label= '< λ;λ;#>',style='filled', fillcolor='yellow')
                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >',fontcolor='red')   
                    produccionesP = ""
                    for elemen in self.producciones:  
                        produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                    tipo3 = ""
                    for elemen in self.terminales: 
                        tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                    dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                    dot.edge('q','f',label= '<λ;λ;#>')  
                mensaje += """<hr width="200%" size=5000 color="black">
                 <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                
                 """ + dot.pipe().decode('utf-8')  +"""
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Pila:      </td>
                        <td class="aaa">      """+ inPila + """ </td>
                        </tr>
                        </tfoot>
                        </table>     
                        <br>  
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Entrada:    </td>
                        <td class="aaa">      """+ char + """  </td>
                        </tr>
                        </tfoot>
                        </table>                                         
                   """
                iteracion += 1 
            elif estado == "q":
                pilaTop = pila[0]
                if pilaTop in self.noTerminales and char in self.terminales:                     
                    reglas = self.transicionPila[pilaTop]
                    if len(reglas)==1: 
                        inPila = ""
                        for elemen in pila.copy(): 
                            inPila += elemen                           
                        pila.pop(0)
                        temp = []
                        temp.extend(reglas[0])
                        temp.extend(pila)
                        pila = temp.copy()  
                        transicion ="λ,"+ pilaTop+";"+ str("".join(reglas[0]))
                        dot = Digraph('html',format='svg')
                        svg = True
                        if svg: 
                            dot.graph_attr['rankdir'] = 'LR'
                            dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                            dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                            dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                            dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                            dot.edge('i','p',label= '< λ;λ;#>')
                            dot.edge('p','q',label= '< λ;λ;' +self.So+' >')  
                            tipo3 ="" 
                            for elemen in self.terminales: 
                                tipo3 += ""+elemen + ","+elemen+","+"λ <BR/>"    
                            dot.edge('q:n','q:n',label= '< ' + transicion+ ' >',fontcolor='red')
                            dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                            dot.edge('q','f',label= '<λ;λ;#>')    
                        mensaje += """"<hr width="200%" size=5000 color="black">
                                       <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                                
                                """ + dot.pipe().decode('utf-8')       +"""
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Pila:      </td>
                                <td class="aaa">      """+ inPila + """ </td>
                                </tr>
                                </tfoot>
                                </table>     
                                <br>  
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Entrada:    </td>
                                <td class="aaa">      """+ char + """  </td>
                                </tr>
                                </tfoot>
                                </table>                                         
                        """                     
                                
                    else: 
                        find = False
                        for regla in reglas: 
                            if regla[0] == char: 
                                inPila = ""
                                for elemen in pila.copy(): 
                                    inPila += elemen                                   
                                pila.pop(0)
                                temp = []
                                temp.extend(regla)
                                temp.extend(pila)
                                pila = temp.copy()
                                transicion = "λ,"+ pilaTop+";"+ str("".join(regla))
                                svg = True
                                dot = Digraph('html',format='svg')            
                                if svg: 
                                    dot.graph_attr['rankdir'] = 'LR'
                                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                                    dot.edge('i','p',label= '< λ;λ;#>')
                                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                                    tipo3 = " "
                                    for elemen in self.terminales: 
                                        tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                                    dot.edge('q:n','q:n',label= '< ' + transicion+ ' >',fontcolor='red')
                                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                                    dot.edge('q','f',label= '<λ;λ;#>')     
                                mensaje += """"<hr width="200%" size=5000 color="black">
                                            <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                                
                                  """ + dot.pipe().decode('utf-8') +"""
                                    <table id="mitabla">
                                        <tfoot class="pie">
                                        <tr>
                                        <td class="ccc"> Pila:      </td>
                                        <td class="aaa">      """+ inPila + """ </td>
                                        </tr>
                                        </tfoot>
                                        </table>     
                                        <br>  
                                    <table id="mitabla">
                                        <tfoot class="pie">
                                        <tr>
                                        <td class="ccc"> Entrada:    </td>
                                        <td class="aaa">      """+ char + """  </td>
                                        </tr>
                                        </tfoot>
                                        </table>                                         
                                """                                                                                                                            

                                find = True

                        if not find: 
                            for regla in reglas:
                                if regla[0] in self.noTerminales: 
                                    inPila = ""
                                    for elemen in pila.copy(): 
                                        inPila += elemen                                 
                                    pila.pop(0)
                                    temp = []
                                    temp.extend(regla)
                                    temp.extend(pila)
                                    pila = temp.copy()
                                    transicion = "λ,"+ pilaTop+";"+ str("".join(regla))
                                    dot = Digraph('html',format='svg')
                                    svg = True
                                    if svg: 
                                        dot.graph_attr['rankdir'] = 'LR'
                                        dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                                        dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                                        dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                                        dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                                        dot.edge('i','p',label= '< λ;λ;#>')
                                        dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                                        tipo3 = " "
                                        for elemen in self.terminales: 
                                            tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                                        dot.edge('q:n','q:n',label= '< ' + transicion+ ' >',fontcolor='red')
                                        dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                                        dot.edge('q','f',label= '<λ;λ;#>')                                            

                                    mensaje += """"<hr width="200%" size=5000 color="black">
                                                <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                                    
                                                        """ + dot.pipe().decode('utf-8')     +"""
                                        <table id="mitabla">
                                            <tfoot class="pie">
                                            <tr>
                                            <td class="ccc"> Pila:      </td>
                                            <td class="aaa">      """+ inPila + """ </td>
                                            </tr>
                                            </tfoot>
                                            </table>     
                                            <br>  
                                        <table id="mitabla">
                                            <tfoot class="pie">
                                            <tr>
                                            <td class="ccc"> Entrada:    </td>
                                            <td class="aaa">      """+ char + """  </td>
                                            </tr>
                                            </tfoot>
                                            </table>                                         
                                    """                                                                                                                        
                                    find = True

                        if not find: 
                            print("Error sintactico")
                            seAcepta = False
                            ERROR = "Error sintactico en la escritura de gramatica"
                            break

                elif pilaTop in self.terminales: 
                    if pilaTop == char: 
                        inPila = ""
                        for elemen in pila.copy(): 
                            inPila += elemen                          
                        pila.pop(0)
                        transicion = char+","+ pilaTop+";λ"
                        svg = True
                        dot = Digraph('html',format='svg') 
                        if svg: 
                            dot.graph_attr['rankdir'] = 'LR'
                            dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                            dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                            dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                            dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                            dot.edge('i','p',label= '< λ;λ;#>')
                            dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                            produccionesP = ""
                            for elemen in self.producciones:  
                                produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'   
                            dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                            dot.edge('q:s','q:s',label= '< ' + transicion+ ' >',fontcolor='red')
                            dot.edge('q','f',label= '<λ;λ;#>')                               
                        mensaje += """"<hr width="200%" size=5000 color="black">
                                       <h1 align="center">Iteración """+str(iteracion)+""": </h1>
                        
                         """ + dot.pipe().decode('utf-8')  +"""
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Pila:      </td>
                                <td class="aaa">      """+ inPila + """ </td>
                                </tr>
                                </tfoot>
                                </table>     
                                <br>  
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Entrada:    </td>
                                <td class="aaa">      """+ char + """  </td>
                                </tr>
                                </tfoot>
                                </table>                                         
                        """                    
                        cont += 1
                    else: 
                        print("Pila top: ",pilaTop)
                        print("char: ",char)
                        print("Error no encontrado")
                        seAcepta = False 
                        ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                        # ERROR += concatenarError
                        print("Error, ",ERROR)
                        break


                elif pilaTop =="#" and char =="#":
                    inPila = ""
                    for elemen in pila.copy(): 
                        inPila += elemen                     
                    pila.pop(0) 
                    estaodoActual = estado 
                    estado = "f"
                    estoadoNext = estado
                    transicion = "("+estaodoActual+",λ,"+ pilaTop+";"+estoadoNext+",λ)" 
                    svg = True
                    dot = Digraph('html',format='svg') 
                    if svg:  
                        dot.graph_attr['rankdir'] = 'LR'
                        dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                        dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                        dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                        dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                        dot.edge('i','p',label= '< λ;λ;#>')
                        dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                        produccionesP = ""
                        for elemen in self.producciones:  
                            produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                        tipo3 = " "
                        for elemen in self.terminales: 
                            tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                        dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                        dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                        dot.edge('q','f',label= '<λ;λ;#>',fontcolor='red')                                                  
                    mensaje += """"<hr width="200%" size=5000 color="black">
                                    <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                    
                        """ + dot.pipe().decode('utf-8') +"""
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Pila:      </td>
                                <td class="aaa">      """+ inPila + """ </td>
                                </tr>
                                </tfoot>
                                </table>     
                                <br>  
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Entrada:    </td>
                                <td class="aaa">      """+ char + """  </td>
                                </tr>
                                </tfoot>
                                </table>                                         
                        """                   
                
                else: 
                    print("Error en, ",char," pos: ",cont," no encontrado")
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" no encontrado"
                    seAcepta = False 
                    break                                          
                iteracion += 1 
            
            elif estado == "f": 
                cont +=1
                if cont == tamaño_entrada: 
                    svg = True
                    dot = Digraph('html',format='svg') 
                    if svg:  
                        dot.graph_attr['rankdir'] = 'LR'
                        dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                        dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                        dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                        dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='yellow')
                        dot.edge('i','p',label= '< λ;λ;#>')
                        dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                        produccionesP = ""
                        for elemen in self.producciones:  
                            produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                        tipo3 = " "
                        for elemen in self.terminales: 
                            tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                        dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                        dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                        dot.edge('q','f',label= '<λ;λ;#>')                                                
                    mensaje += """"<hr width="200%" size=5000 color="black">
                                    <h1 align="center"> Iteración """+str(iteracion)+""": </h1>
                    
                        """ + dot.pipe().decode('utf-8')  +"""
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Pila:      </td>
                        <td class="aaa">      """+ inPila + """ </td>
                        </tr>
                        </tfoot>
                        </table>     
                        <br>  
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Entrada:    </td>
                        <td class="aaa">      """+ char + """  </td>
                        </tr>
                        </tfoot>
                        </table>                                         
                   """                
                else: 
                    print("Error pila queda: ",pila)
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" PILA"
                    seAcepta = False
                break

        if seAcepta: 
            print("Se acepta: ")
            mensaje +=""" <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                    ¡La cadena ingresada es válida!</p>"""
        else: 
            print("No se acepta ")
            mensaje +=""" <p widht="200%" style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                    ¡La cadena ingresada ¡NO! es válida! POR: <br>"""+ERROR+""" .</p>"""
        mensaje += """                      
                </form>
                </div>
                </div>
                </div>
                </body>
                </html>  
            """ 
        f.write(mensaje)
        f.close()    
        webbrowser.open_new_tab(nombreW)         
  
    def listas(self): 
        duply = self.producciones.copy()
        contador = 0
        listaTemporal = []
        diccionarioTemporal = {}
        comparar = ""
        inicio = True
        while len(duply)>0:
            if inicio: 
                if len(duply[contador][1]) == 1: 
                    temp = []
                    temp.append(duply[contador][1])
                    listaTemporal.append(temp.copy())
                    temp.clear()
                else: 
                    listaTemporal.append(duply[contador][1].split(" ")) 
                comparar = duply[contador][0]
                duply.pop(contador)
                inicio = False
                if len(duply) == 0: 
                    dt = {comparar:listaTemporal.copy()}
                    diccionarioTemporal.update(dt)
                    listaTemporal.clear()
            else: 
                if contador == len(duply): 
                    dt = {comparar:listaTemporal.copy()}
                    diccionarioTemporal.update(dt)
                    contador = 0
                    listaTemporal.clear()
                    inicio = True  
                elif duply[contador][0] == comparar: 
                    # formato += "\n " + tabulacion + duply[contador][1]
                    if len(duply[contador][1]) == 1: 
                        temp = []
                        temp.append(duply[contador][1])
                        listaTemporal.append(temp.copy())
                        temp.clear()
                    else: 
                        listaTemporal.append(duply[contador][1].split(" ")) 
                    duply.pop(contador)  
                    if len(duply) == 0: 
                        dt = {comparar:listaTemporal.copy()}
                        diccionarioTemporal.update(dt)
                        listaTemporal.clear()
                else:                     
                    contador +=1
                    if contador ==  len(duply): 
                        dt = {comparar:listaTemporal.copy()}
                        diccionarioTemporal.update(dt)
                        listaTemporal.clear()
                        contador = 0
                        inicio = True
        self.transicionPila = diccionarioTemporal.copy()   
        
    def hayOtraRuta(self, historialT):
            count = 1
            if len(historialT) > 0:
                for hT in reversed(historialT):
                    if hT[6] == True:
                        return True, count
                    else:
                        count += 1
            return False, 0

    def generaTablas2(self,entrad): 
        seAcepta = True
        global ERROR 
        estaodoActual = ""
        estoadoNext = ""
        tabla = []#[[iteracion,pila,entrada,[Transiciones]]]
        entrada = str(entrad) + "#"
        tamaño_entrada = len(entrada)
        pila = []
        mejor_recorrido = []    #  cont, [tabla]
        camino = []             #
        newSearch = False       #
        contPrev = 0        #
        iteracion = 0    
        cont = 0   
        estado = "i"
        import webbrowser
        self.listas()       
                
        while (cont < tamaño_entrada): 
            char = entrada[cont]
            if estado == "i": 
                cm = [char, pila.copy(), "λ", ["λ"], cont, 0, False, "i", "p"]        #----
                camino.append(cm.copy())                                               #----
                pila.append("#")
                estadoA = estado
                estado = "p"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ pila[0] + ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(" ")
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())
                temp.clear()
                apila = "#"
                iteracion += 1 

            elif estado == "p":
                cm = [char, pila.copy(), "λ", [self.So], cont, 0, False, "p", "q"]        #----
                camino.append(cm.copy())                                               #----
                inPila = ""
                for elemen in pila: 
                    inPila += elemen
                temp = []
                temp.extend(str(self.So))
                temp.extend(pila)
                pila = temp.copy() 
                estadoA = estado                       
                estado = "q"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ self.So+ ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(str(inPila))
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())                
                temp.clear()
                iteracion += 1 
            elif estado == "q":
                pilaTop = pila[0]
                if pilaTop in self.noTerminales and char in self.terminales:                     
                    reglas = self.transicionPila[pilaTop]
                    if len(reglas)==1: 
                        otraRuta, pasosAtras = self.hayOtraRuta(camino)
                        if reglas[0][0] == char or reglas[0][0] in self.noTerminales: # sera reglas[0] o reglas[0][0] ??
                            cm = [char, pila.copy(), pilaTop, reglas[0].copy(), cont, 0, False, "q", "q"]        #----
                            camino.append(cm.copy())                                               #----
                            # self.muestraLista(camino)
                            inPila = ""
                            for elemen in pila.copy(): 
                                inPila += elemen                           
                            pila.pop(0)
                            temp = []
                            temp.extend(reglas[0])
                            temp.extend(pila)
                            pila = temp.copy()
                            # mejor_recorrido.append(pila.copy())                                   #----
                            transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(reglas[0]))+ ")" 
                            temp1 = []    
                            temp1.append(str(iteracion))
                            temp1.append(str(inPila))
                            temp1.append(str(char))
                            temp1.append(transicion)
                            tabla.append(temp1.copy())  
                        elif otraRuta:
                            if len(mejor_recorrido) == 0:
                                mejor_recorrido = [cont, camino.copy()]
                            else:
                                if mejor_recorrido[0] < cont:
                                    # len(mejor_recorrido[1]) <= len(camino) and
                                    mejor_recorrido = [cont, camino.copy()]
                            #Regresa hasta el punto mas cercano alterno
                            #Resetar Pila
                            pila = camino[len(camino)-pasosAtras][1]
                            #Resetar Cont
                            cont = camino[len(camino)-pasosAtras][4]
                            #Obtener contador de transición
                            contPrev = camino[len(camino)-pasosAtras][5]
                            #Resetar Camino
                            tamanio = len(camino)
                            for i in range(1,pasosAtras+1):
                                camino.pop(tamanio-i)
                            newSearch = True
                        else:
                            seAcepta = False
                            ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                            break
                    else: 
                        find = False
                        countTr = 0
                        limitTr = len(reglas)
                        if newSearch:
                            countTr = contPrev + 1
                            newSearch = False
                            # if char == "z":
                            #     print("nueva Búsqueda")
                            #     self.muestraLista(camino)
                        while countTr < limitTr:
                            regla = reglas[countTr]
                            if regla[0] == char or regla[0] in self.noTerminales:
                                cm = []
                                if countTr == limitTr-1:
                                    cm = [char, pila.copy(), pilaTop, regla.copy(), cont, countTr, False, "q", "q"]        #----
                                else:
                                    cm = [char, pila.copy(), pilaTop, regla.copy(), cont, countTr, True, "q", "q"]        #----
                                camino.append(cm.copy())                                               #----
                                # if char == "z":
                                #     self.muestraLista(camino)
                                for elemen in pila.copy(): 
                                    inPila += elemen                                 
                                pila.pop(0)
                                temp = []
                                temp.extend(regla)
                                temp.extend(pila)
                                pila = temp.copy()
                                transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(regla))+ ")" 
                                temp1 = []    
                                temp1.append(str(iteracion))
                                temp1.append(str(inPila))
                                temp1.append(str(char))
                                temp1.append(transicion)
                                tabla.append(temp1.copy())  
                                temp1.clear()                              
                                find = True
                            if find:
                                break
                            countTr += 1
                        if not find: 
                            otraRuta, pasosAtras = self.hayOtraRuta(camino)
                            if otraRuta:
                                if len(mejor_recorrido) == 0:
                                    mejor_recorrido = [cont, camino.copy()]
                                else:
                                    if mejor_recorrido[0] < cont:
                                        mejor_recorrido = [cont, camino.copy()]
                                #Regresa hasta el punto mas cercano alterno
                                #Resetar Pila
                                pila = camino[len(camino)-pasosAtras][1]
                                #Resetar Cont
                                cont = camino[len(camino)-pasosAtras][4]
                                #Obtener contador de transición
                                contPrev = camino[len(camino)-pasosAtras][5]
                                #Resetar Camino
                                tamanio = len(camino)
                                for i in range(1,pasosAtras+1):
                                    camino.pop(tamanio-i)
                                newSearch = True
                            else:
                                seAcepta = False
                                ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                                break

                elif pilaTop in self.terminales: 
                    if pilaTop == char:
                        cm = [char, pila.copy(), pilaTop, ["λ"], cont, 0, False, "q", "q"]        #----
                        camino.append(cm.copy())                                               #----
                        # self.muestraLista(camino)
                        for elemen in pila.copy(): 
                            inPila += elemen                          
                        pila.pop(0)
                        transicion = "("+estado+"," +char+","+ pilaTop+";"+estado+",λ)" 
                        temp1 = []    
                        temp1.append(str(iteracion))
                        temp1.append(str(inPila))
                        temp1.append(str(char))
                        temp1.append(transicion)
                        tabla.append(temp1.copy())  
                        temp1.clear()         
                        cont += 1
                    else:
                        otraRuta, pasosAtras = self.hayOtraRuta(camino)
                        if otraRuta:
                            if len(mejor_recorrido) == 0:
                                mejor_recorrido = [cont, camino.copy()]
                            else:
                                if mejor_recorrido[0] < cont:
                                    mejor_recorrido = [cont, camino.copy()]
                            #Regresa hasta el punto mas cercano alterno
                            #Resetar Pila
                            pila = camino[len(camino)-pasosAtras][1]
                            #Resetar Cont
                            cont = camino[len(camino)-pasosAtras][4]
                            #Obtener contador de transición
                            contPrev = camino[len(camino)-pasosAtras][5]
                            #Resetar Camino
                            tamanio = len(camino)
                            for i in range(1,pasosAtras+1):
                                camino.pop(tamanio-i)
                            newSearch = True
                        else:
                            seAcepta = False 
                            ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                            # ERROR += concatenarError
                            break 

                elif pilaTop =="#" and char =="#":
                    cm = [char, pila.copy(), pilaTop, ["λ"], cont, 0, False, "q", "f"]        #----
                    camino.append(cm.copy())                                               #---- 
                    # self.muestraLista(camino)
                    inPila = ""
                    for elemen in pila.copy(): 
                        inPila += elemen                     
                    pila.pop(0) 
                    estaodoActual = estado 
                    estado = "f"
                    estoadoNext = estado
                    transicion = "("+estaodoActual+",λ,"+ pilaTop+";"+estoadoNext+",λ)" 
                    temp1 = []    
                    temp1.append(str(iteracion))
                    temp1.append(str(inPila))
                    temp1.append(str("λ"))
                    temp1.append(transicion)
                    tabla.append(temp1.copy())  
                    temp1.clear()                       
                else: 
                    otraRuta, pasosAtras = self.hayOtraRuta(camino)
                    if otraRuta:
                        if len(mejor_recorrido) == 0:
                            mejor_recorrido = [cont, camino.copy()]
                        else:
                            if mejor_recorrido[0] < cont:
                                mejor_recorrido = [cont, camino.copy()]
                        #Regresa hasta el punto mas cercano alterno
                        #Resetar Pila
                        pila = camino[len(camino)-pasosAtras][1]
                        #Resetar Cont
                        cont = camino[len(camino)-pasosAtras][4]
                        #Obtener contador de transición
                        contPrev = camino[len(camino)-pasosAtras][5]
                        #Resetar Camino
                        tamanio = len(camino)
                        for i in range(1,pasosAtras+1):
                            camino.pop(tamanio-i)
                        newSearch = True
                    else:
                        ERROR = "Error en, "+char+" pos: "+str(cont)+" no encontrado"
                        seAcepta = False
                        for table in tabla: 
                            print(" | ".join(table))                    
                        break                                                
                iteracion += 1 
            elif estado == "f": 
                cont +=1
                if cont == tamaño_entrada: 
                    cm = [" ", pila.copy(), pilaTop, "λ", cont, 0, False, "f", "f"] 
                    camino.append(cm.copy())                    
                    temp1 = []    
                    temp1.append(str(iteracion))
                    temp1.append(str("λ"))
                    temp1.append(str("λ"))
                    temp1.append(str("f"))
                    tabla.append(temp1.copy())  
                    temp1.clear()                          
                else: 
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" PILA"
                    seAcepta = False
                break
        
        if seAcepta: 
            print("Se acepta ")
            self.generarTHtml(camino,"",entrada)

        else: 
            print("No se acepta")
            if mejor_recorrido[1] >0: 
                self.generarTHtml(mejor_recorrido[1],ERROR,entrada)
            else: 
                self.generarTHtml(camino,ERROR,entrada)
                
    def generaRecorrido2(self,entrad): 
        seAcepta = True
        global ERROR 
        estaodoActual = ""
        estoadoNext = ""
        tabla = []#[[iteracion,pila,entrada,[Transiciones]]]
        entrada = str(entrad) + "#"
        tamaño_entrada = len(entrada)
        pila = []
        mejor_recorrido = []    #  cont, [tabla]
        camino = []             #
        newSearch = False       #
        contPrev = 0        #
        iteracion = 0    
        cont = 0   
        estado = "i"
        import webbrowser
        self.listas()       
                
        while (cont < tamaño_entrada): 
            char = entrada[cont]
            if estado == "i": 
                cm = [char, pila.copy(), "λ", ["λ"], cont, 0, False, "i", "p"]        #----
                camino.append(cm.copy())                                               #----
                pila.append("#")
                estadoA = estado
                estado = "p"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ pila[0] + ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(" ")
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())
                temp.clear()
                apila = "#"
                iteracion += 1 

            elif estado == "p":
                cm = [char, pila.copy(), "λ", [self.So], cont, 0, False, "p", "q"]        #----
                camino.append(cm.copy())                                               #----
                inPila = ""
                for elemen in pila: 
                    inPila += elemen
                temp = []
                temp.extend(str(self.So))
                temp.extend(pila)
                pila = temp.copy() 
                estadoA = estado                       
                estado = "q"
                estadoNext = estado
                transicion = "("+estadoA+",λ,λ;"+estadoNext+","+ self.So+ ")"
                temp = []
                temp.append(str(iteracion))
                temp.append(str(inPila))
                temp.append(str(char))
                temp.append(transicion)
                tabla.append(temp.copy())                
                temp.clear()
                iteracion += 1 
            elif estado == "q":
                pilaTop = pila[0]
                if pilaTop in self.noTerminales and char in self.terminales:                     
                    reglas = self.transicionPila[pilaTop]
                    if len(reglas)==1: 
                        otraRuta, pasosAtras = self.hayOtraRuta(camino)
                        if reglas[0][0] == char or reglas[0][0] in self.noTerminales: # sera reglas[0] o reglas[0][0] ??
                            cm = [char, pila.copy(), pilaTop, reglas[0].copy(), cont, 0, False, "q", "q"]        #----
                            camino.append(cm.copy())                                               #----
                            # self.muestraLista(camino)
                            inPila = ""
                            for elemen in pila.copy(): 
                                inPila += elemen                           
                            pila.pop(0)
                            temp = []
                            temp.extend(reglas[0])
                            temp.extend(pila)
                            pila = temp.copy()
                            # mejor_recorrido.append(pila.copy())                                   #----
                            transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(reglas[0]))+ ")" 
                            temp1 = []    
                            temp1.append(str(iteracion))
                            temp1.append(str(inPila))
                            temp1.append(str(char))
                            temp1.append(transicion)
                            tabla.append(temp1.copy())  
                        elif otraRuta:
                            if len(mejor_recorrido) == 0:
                                mejor_recorrido = [cont, camino.copy()]
                            else:
                                if mejor_recorrido[0] < cont:
                                    # len(mejor_recorrido[1]) <= len(camino) and
                                    mejor_recorrido = [cont, camino.copy()]
                            #Regresa hasta el punto mas cercano alterno
                            #Resetar Pila
                            pila = camino[len(camino)-pasosAtras][1]
                            #Resetar Cont
                            cont = camino[len(camino)-pasosAtras][4]
                            #Obtener contador de transición
                            contPrev = camino[len(camino)-pasosAtras][5]
                            #Resetar Camino
                            tamanio = len(camino)
                            for i in range(1,pasosAtras+1):
                                camino.pop(tamanio-i)
                            newSearch = True
                        else:
                            # print("Error sintactico")
                            seAcepta = False
                            ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                            break
                    else: 
                        find = False
                        countTr = 0
                        limitTr = len(reglas)
                        if newSearch:
                            countTr = contPrev + 1
                            newSearch = False
                            # if char == "z":
                            #     print("nueva Búsqueda")
                            #     self.muestraLista(camino)
                        while countTr < limitTr:
                            regla = reglas[countTr]
                            if regla[0] == char or regla[0] in self.noTerminales:
                                cm = []
                                if countTr == limitTr-1:
                                    cm = [char, pila.copy(), pilaTop, regla.copy(), cont, countTr, False, "q", "q"]        #----
                                else:
                                    cm = [char, pila.copy(), pilaTop, regla.copy(), cont, countTr, True, "q", "q"]        #----
                                camino.append(cm.copy())                                               #----
                                # if char == "z":
                                #     self.muestraLista(camino)
                                for elemen in pila.copy(): 
                                    inPila += elemen                                 
                                pila.pop(0)
                                temp = []
                                temp.extend(regla)
                                temp.extend(pila)
                                pila = temp.copy()
                                transicion = "("+estado+",λ,"+ pilaTop+";"+estado+","+ str("".join(regla))+ ")" 
                                temp1 = []    
                                temp1.append(str(iteracion))
                                temp1.append(str(inPila))
                                temp1.append(str(char))
                                temp1.append(transicion)
                                tabla.append(temp1.copy())  
                                temp1.clear()                              
                                find = True
                            if find:
                                break
                            countTr += 1
                        if not find: 
                            otraRuta, pasosAtras = self.hayOtraRuta(camino)
                            if otraRuta:
                                if len(mejor_recorrido) == 0:
                                    mejor_recorrido = [cont, camino.copy()]
                                else:
                                    if mejor_recorrido[0] < cont:
                                        mejor_recorrido = [cont, camino.copy()]
                                #Regresa hasta el punto mas cercano alterno
                                #Resetar Pila
                                pila = camino[len(camino)-pasosAtras][1]
                                #Resetar Cont
                                cont = camino[len(camino)-pasosAtras][4]
                                #Obtener contador de transición
                                contPrev = camino[len(camino)-pasosAtras][5]
                                #Resetar Camino
                                tamanio = len(camino)
                                for i in range(1,pasosAtras+1):
                                    camino.pop(tamanio-i)
                                newSearch = True
                            else:
                                # print("Error sintactico")
                                seAcepta = False
                                ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                                break

                elif pilaTop in self.terminales: 
                    if pilaTop == char:
                        cm = [char, pila.copy(), pilaTop, ["λ"], cont, 0, False, "q", "q"]        #----
                        camino.append(cm.copy())                                               #----
                        # self.muestraLista(camino)
                        for elemen in pila.copy(): 
                            inPila += elemen                          
                        pila.pop(0)
                        transicion = "("+estado+"," +char+","+ pilaTop+";"+estado+",λ)" 
                        temp1 = []    
                        temp1.append(str(iteracion))
                        temp1.append(str(inPila))
                        temp1.append(str(char))
                        temp1.append(transicion)
                        tabla.append(temp1.copy())  
                        temp1.clear()         
                        cont += 1
                    else:
                        otraRuta, pasosAtras = self.hayOtraRuta(camino)
                        if otraRuta:
                            if len(mejor_recorrido) == 0:
                                mejor_recorrido = [cont, camino.copy()]
                            else:
                                if mejor_recorrido[0] < cont:
                                    mejor_recorrido = [cont, camino.copy()]
                            #Regresa hasta el punto mas cercano alterno
                            #Resetar Pila
                            pila = camino[len(camino)-pasosAtras][1]
                            #Resetar Cont
                            cont = camino[len(camino)-pasosAtras][4]
                            #Obtener contador de transición
                            contPrev = camino[len(camino)-pasosAtras][5]
                            #Resetar Camino
                            tamanio = len(camino)
                            for i in range(1,pasosAtras+1):
                                camino.pop(tamanio-i)
                            newSearch = True
                        else:
                            # print("Pila top: ",pilaTop)
                            # print("char: ",char)
                            # print("Error no encontrado")
                            seAcepta = False 
                            ERROR = "LO QUE SE ESTA LEYENDO: "+char+" NO ES IGUAL A LA CIMA DE LA PILA: " + pilaTop + " SE ESPERABA: "+pilaTop +" EN POS: " +str(cont)
                            # ERROR += concatenarError
                            # print("Error, ",ERROR)
                            # print("Tabla")
                            # for table in tabla: 
                            #     print(" | ".join(table))
                            break 

                elif pilaTop =="#" and char =="#":
                    cm = [char, pila.copy(), pilaTop, ["λ"], cont, 0, False, "q", "f"]        #----
                    camino.append(cm.copy())                                               #---- 
                    # self.muestraLista(camino)
                    inPila = ""
                    for elemen in pila.copy(): 
                        inPila += elemen                     
                    pila.pop(0) 
                    estaodoActual = estado 
                    estado = "f"
                    estoadoNext = estado
                    transicion = "("+estaodoActual+",λ,"+ pilaTop+";"+estoadoNext+",λ)" 
                    temp1 = []    
                    temp1.append(str(iteracion))
                    temp1.append(str(inPila))
                    temp1.append(str("λ"))
                    temp1.append(transicion)
                    tabla.append(temp1.copy())  
                    temp1.clear()                       
                else: 
                    otraRuta, pasosAtras = self.hayOtraRuta(camino)
                    if otraRuta:
                        if len(mejor_recorrido) == 0:
                            mejor_recorrido = [cont, camino.copy()]
                        else:
                            if mejor_recorrido[0] < cont:
                                mejor_recorrido = [cont, camino.copy()]
                        #Regresa hasta el punto mas cercano alterno
                        #Resetar Pila
                        pila = camino[len(camino)-pasosAtras][1]
                        #Resetar Cont
                        cont = camino[len(camino)-pasosAtras][4]
                        #Obtener contador de transición
                        contPrev = camino[len(camino)-pasosAtras][5]
                        #Resetar Camino
                        tamanio = len(camino)
                        for i in range(1,pasosAtras+1):
                            camino.pop(tamanio-i)
                        newSearch = True
                    else:
                        # print("Error en, ",char," pos: ",cont," no encontrado")
                        ERROR = "Error en, "+char+" pos: "+str(cont)+" no encontrado"
                        seAcepta = False
                        for table in tabla: 
                            print(" | ".join(table))                    
                        break                                                
                iteracion += 1 
            elif estado == "f": 
                cont +=1
                if cont == tamaño_entrada: 
                    temp1 = []    
                    cm = [" ", pila.copy(), pilaTop, "λ", cont, 0, False, "f", "f"] 
                    camino.append(cm.copy())
                    temp1.append(str(iteracion))
                    temp1.append(str("λ"))
                    temp1.append(str("λ"))
                    temp1.append(str("f"))
                    tabla.append(temp1.copy())  
                    temp1.clear()                          
                else: 
                    # print("Error pila queda: ",pila)
                    ERROR = "Error en, "+char+" pos: "+str(cont)+" PILA"
                    seAcepta = False
                break
        
        if seAcepta: 
            print("Se acepta " )
            self.generarRHtml(camino,"")

        else: 
            print("No se acepta ")
            if mejor_recorrido[0] >0: 
                self.generarRHtml(mejor_recorrido[1],ERROR)
            else: 
                self.generarRHtml(camino,ERROR)
                
    def generarTHtml(self,l,error,entrada):
        import webbrowser
        nombreW = self.nombre +"Prueba.html"
        f = open(nombreW,mode="w", encoding="utf-8")
        mensaje = """
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                    <link href="estilosTablas.css" rel="stylesheet" >
                    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                    <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
                    <title>Aplicacion de Prueba</title>
                    </head>
                    <body>
                    <div class="sidenav">
                    <div class="login-main-text">
                        <h1>"""+self.nombre + """<br> </h1>
                        <h1> Cadena: """+entrada+ """</h1>
                    </div>
                </div>
                <div class="main">
                    <div class="col-md-6 col-sm-12">
                        <div class="login-form">
                        <h1>Tabla </h1>
                        <form>
        """        
        mensaje +=   """ 
            <table id="customers">
                        <tr>
                            <th>Iteracion</th>
                            <th>Pila <br><-- </th>
                            <th>Entrada</th>
                            <th>Transiciones</th>
                        </tr>                
        """
                    
        contador = 0
        for c in l:
            entrada_t = c[0]
            pila_t = " ".join(c[1])
            estS_t = c[7]
            ntS_t = c[2]
            estL_t = c[8]
            trn_t = " ".join(c[3])
            if estS_t == "i" or estS_t == "p":
                transicion = ""
                transicion += estS_t+ ", λ,"+ ntS_t+ ";"+ estL_t+ ","+ trn_t
                mensaje +=   """ 
                    <tr>
                    <td>"""+str(contador)+""" </td>
                    <td>"""+str(pila_t)+""" </td>
                    <td>"""+str(entrada_t)+""" </td>
                    <td>"""+str(transicion)+""" </td>
                    </tr>
                """            
            elif estS_t == "q":
                if entrada_t == ntS_t:
                    transicion = ""
                    transicion +=  estS_t+ ","+ ntS_t+ ","+ ntS_t+ ";"+ estL_t+ ","+ trn_t
                    mensaje +=   """ 
                        <tr>
                        <td>"""+str(contador)+""" </td>
                        <td>"""+str(pila_t)+""" </td>
                        <td>"""+str(entrada_t)+""" </td>
                        <td>"""+str(transicion)+""" </td>
                        </tr>
                    """            
                else:
                    transicion = ""
                    transicion +=  estS_t+ ", λ,"+ ntS_t+ ";"+ estL_t+ ","+ trn_t
                    mensaje +=   """ 
                        <tr>
                        <td>"""+str(contador)+""" </td>
                        <td>"""+str(pila_t)+""" </td>
                        <td>"""+str(entrada_t)+""" </td>
                        <td>"""+str(transicion)+""" </td>
                        </tr>
                    """ 

            elif estS_t == "f": 
                transicion = ""
                transicion +=  estS_t+ ", λ,"+ntS_t+ ";"+ estL_t+ ","+ trn_t
                mensaje +=   """ 
                    <tr>
                    <td>"""+str(contador)+""" </td>
                    <td>"""+str("λ")+""" </td>
                    <td>"""+str("λ")+""" </td>
                    <td>"""+str("f")+""" </td>
                    </tr>
                """            
            else:
                transicion = ""
                transicion +=  estS_t+ ", λ,"+ntS_t+ ";"+ estL_t+ ","+ trn_t
                mensaje +=   """ 
                    <tr>
                    <td>"""+str(contador)+""" </td>
                    <td>"""+str(pila_t)+""" </td>
                    <td>"""+str(entrada_t)+""" </td>
                    <td>"""+str(transicion)+""" </td>
                    </tr>
                """            
            contador+=1

        mensaje +=   """ 
            </table>
            """   
        if len(error) >0: 
            mensaje +=""" 
                <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                        LA CADENA NO ES ACEPTADA POR: <br>"""+error+""" .</p>"""        
        else: 
            mensaje +=""" <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                        LA CADENA ES ACEPTADA.</p>"""        

        mensaje += """                      
                    </form>
                    </div>
                    </div>
                    </div>
                    </body>
                    </html>  
                """ 

        f.write(mensaje)
        f.close()    
        webbrowser.open_new_tab(nombreW)       
    
    def generarRHtml(self, l,error):
        import webbrowser
        nombreW = self.nombre +"Recorrido.html"
        f = open(nombreW,mode="w", encoding="utf-8")
        mensaje = """
                <!DOCTYPE html>
                <html lang="en">
                    <head>
                    <link href="estiloR.css" rel="stylesheet" >
                    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
                    <script src="https://code.jquery.com/jquery-1.11.1.min.js"></script>
                    <title>Aplicacion de Prueba</title>
                    </head>
                    <body>
                    <div class="sidenav">
                    <div class="login-main-text">
                        <h1>"""+self.nombre + """<br> </h1>
                    </div>
                </div>
                <div class="main">
                    <div class="col-md-6 col-sm-12">
                        <div class="login-form">
                        <h1>Tabla </h1>
                        <form>
        """        
                    
        contador = 0
        for c in l:
            entrada_t = c[0]
            pila_t = " ".join(c[1])
            estS_t = c[7]
            ntS_t = c[2]
            estL_t = c[8]
            trn_t = " ".join(c[3])
            if estS_t == "i" :
                transicion = ""
                transicion += estS_t+ ", λ,"+ ntS_t+ ";"+ estL_t+ ","+ trn_t
                svg = True
                dot = Digraph('html',format='svg')
                if svg: 
                    dot.graph_attr['rankdir'] = 'LR'
                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='yellow' )
                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                    dot.edge('i','p',label= '< λ;λ;#>',fontcolor='red')
                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                    produccionesP = ""
                    for elemen in self.producciones:  
                        produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                    tipo3 = " "
                    for elemen in self.terminales: 
                        tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                    dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                    dot.edge('q','f',label= '<λ;λ;#>')                             
                mensaje += """"<hr width="200%" size=5000 color="black">
                 <h1 align="center"> Iteración """+str(contador)+""": </h1>  
                                 
                 """ + dot.pipe().decode('utf-8') +"""
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Pila:      </td>
                        <td class="aaa">      vacia </td>
                        </tr>
                        </tfoot>
                        </table>     
                        <br>  
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Entrada:    </td>
                        <td class="aaa">      """+ entrada_t + """  </td>
                        </tr>
                        </tfoot>
                        </table>                                         
                   """                                
      
            elif  estS_t == "p":
                svg = True
                dot = Digraph('html',format='svg')
                if svg: 
                    dot.graph_attr['rankdir'] = 'LR'
                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='yellow')
                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                    dot.edge('i','p',label= '< λ;λ;#>',style='filled', fillcolor='yellow')
                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >',fontcolor='red')   
                    produccionesP = ""
                    for elemen in self.producciones:  
                        produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                    tipo3 = " "
                    for elemen in self.terminales: 
                        tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                    dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                    dot.edge('q','f',label= '<λ;λ;#>')                             
                mensaje += """"<hr width="200%" size=5000 color="black">
                 <h1 align="center"> Iteración """+str(contador)+""": </h1>  
                                 
                 """ + dot.pipe().decode('utf-8') +"""
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Pila:      </td>
                        <td class="aaa">      """+ pila_t + """  </td>
                        </tr>
                        </tfoot>
                        </table>     
                        <br>  
                       <table id="mitabla">
                        <tfoot class="pie">
                        <tr>
                        <td class="ccc"> Entrada:    </td>
                        <td class="aaa">      """+ entrada_t + """  </td>
                        </tr>
                        </tfoot>
                        </table>                                         
                   """                                
                      

            elif estS_t == "q":
                if entrada_t == ntS_t:
                    if entrada_t == "#": 
                        svg = True
                        dot = Digraph('html',format='svg') 
                        if svg:  
                            dot.graph_attr['rankdir'] = 'LR'
                            dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                            dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                            dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                            dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                            dot.edge('i','p',label= '< λ;λ;#>')
                            dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                            produccionesP = ""
                            for elemen in self.producciones:  
                                produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                            tipo3 = " "
                            for elemen in self.terminales: 
                                tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                            dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                            dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                            dot.edge('q','f',label= '<λ;λ;#>',fontcolor='red')                                                  
                        mensaje += """"<hr width="200%" size=5000 color="black">
                                        <h1 align="center"> Iteración """+str(contador)+""": </h1>
                        
                            """ + dot.pipe().decode('utf-8') +"""
                                <table id="mitabla">
                                    <tfoot class="pie">
                                    <tr>
                                    <td class="ccc"> Pila:      </td>
                                    <td class="aaa">      """+ pila_t + """ </td>
                                    </tr>
                                    </tfoot>
                                    </table>     
                                    <br>  
                                <table id="mitabla">
                                    <tfoot class="pie">
                                    <tr>
                                    <td class="ccc"> Entrada:    </td>
                                    <td class="aaa">      """+ entrada_t + """  </td>
                                    </tr>
                                    </tfoot>
                                    </table>                                         
                            """                   
                                        
                    else: 
                        transicion = ""
                        transicion += ntS_t+ ","+ ntS_t+ ";"+ "λ"
                        if pila_t[0] in self.noTerminales: 
                            tipo = 3
                        elif pila_t[0] in self.terminales: 
                            tipo = 2
                        svg = True
                        dot = Digraph('html',format='svg') 
                        if svg: 
                            dot.graph_attr['rankdir'] = 'LR'
                            dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                            dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                            dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                            dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                            dot.edge('i','p',label= '< λ;λ;#>')
                            dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                            produccionesP = ""
                            for elemen in self.producciones:  
                                produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'   
                            dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                            dot.edge('q:s','q:s',label= '< ' + transicion+ ' >',fontcolor='red')
                            dot.edge('q','f',label= '<λ;λ;#>')                               
                        mensaje += """"<hr width="200%" size=5000 color="black">
                                        <h1 align="center">Iteración """+str(contador)+""": </h1>
                        
                            """ + dot.pipe().decode('utf-8')  +"""
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Pila:      </td>
                                <td class="aaa">      """+ pila_t + """ </td>
                                </tr>
                                </tfoot>
                                </table>     
                                <br>  
                            <table id="mitabla">
                                <tfoot class="pie">
                                <tr>
                                <td class="ccc"> Entrada:    </td>
                                <td class="aaa">      """+ entrada_t + """  </td>
                                </tr>
                                </tfoot>
                                </table>                                         
                        """                                
                else:
                    transicion = ""
                    transicion +=   "λ,"+ ntS_t+ ";"+ trn_t              
                    dot = Digraph('html',format='svg')
                    svg = True
                    if svg: 
                        dot.graph_attr['rankdir'] = 'LR'
                        dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                        dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                        dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='yellow')
                        dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='lightgray')
                        dot.edge('i','p',label= '< λ;λ;#>')
                        dot.edge('p','q',label= '< λ;λ;' +self.So+' >')  
                        tipo3 ="" 
                        for elemen in self.terminales: 
                            tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                        dot.edge('q:n','q:n',label= '< ' + transicion+ ' >',fontcolor='red')
                        dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                        dot.edge('q','f',label= '<λ;λ;#>')    
                    mensaje += """"<hr width="200%" size=5000 color="black">
                                    <h1 align="center"> Iteración """+str(contador)+""": </h1>
                            
                            """ + dot.pipe().decode('utf-8')       +"""
                        <table id="mitabla">
                            <tfoot class="pie">
                            <tr>
                            <td class="ccc"> Pila:      </td>
                            <td class="aaa">      """+ pila_t + """ </td>
                            </tr>
                            </tfoot>
                            </table>     
                            <br>  
                        <table id="mitabla">
                            <tfoot class="pie">
                            <tr>
                            <td class="ccc"> Entrada:    </td>
                            <td class="aaa">      """+ entrada_t + """  </td>
                            </tr>
                            </tfoot>
                            </table>                                         
                    """               

                
            elif estS_t == "f":
                svg = True
                dot = Digraph('html',format='svg') 
                if svg:  
                    dot.graph_attr['rankdir'] = 'LR'
                    dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                    dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                    dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                    dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='yellow')
                    dot.edge('i','p',label= '< λ;λ;#>')
                    dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                    produccionesP = ""
                    for elemen in self.producciones:  
                        produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                    tipo3 = " "
                    for elemen in self.terminales: 
                        tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                    dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                    dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                    dot.edge('q','f',label= '<λ;λ;#> ')                                                
                mensaje += """"<hr width="200%" size=5000 color="black">
                                <h1 align="center"> Iteración """+str(contador)+""": </h1>
                
                    """ + dot.pipe().decode('utf-8')  +"""
                    <table id="mitabla">
                    <tfoot class="pie">
                    <tr>
                    <td class="ccc"> Pila:      </td>
                    <td class="aaa">      """+ pila_t + """ </td>
                    </tr>
                    </tfoot>
                    </table>     
                    <br>  
                    <table id="mitabla">
                    <tfoot class="pie">
                    <tr>
                    <td class="ccc"> Entrada:    </td>
                    <td class="aaa">      """+ entrada_t + """  </td>
                    </tr>
                    </tfoot>
                    </table>                                         
                """   
                transicion = ""
                transicion +=  estS_t+ ", λ,"+ntS_t+ ";"+ estL_t+ ","+ trn_t
       
            contador+=1
   
        if len(error) >0: 
            mensaje +=""" 
                <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                        LA CADENA NO ES ACEPTADA POR: <br>"""+error+""" .</p>"""        
        else: 

            svg = True
            dot = Digraph('html',format='svg') 
            if svg:  
                dot.graph_attr['rankdir'] = 'LR'
                dot.node('i',label='i', shape='circle',style='filled', fillcolor='lightgray' )
                dot.node('p',label='p', shape='circle',style='filled', fillcolor='lightgray')
                dot.node('q',label='q',shape='circle',height='1',widht='1',style='filled', fillcolor='lightgray')
                dot.node('f',label='f', shape='doublecircle',style='filled', fillcolor='yellow')
                dot.edge('i','p',label= '< λ;λ;#>')
                dot.edge('p','q',label= '< λ;λ;' +self.So+' >')   
                produccionesP = ""
                for elemen in self.producciones:  
                    produccionesP += 'λ;' + elemen[0]+';'+elemen[1].replace(" ","") + '<BR/>'
                tipo3 = " "
                for elemen in self.terminales: 
                    tipo3 += "- "+elemen + ","+elemen+","+"λ <BR/>"    
                dot.edge('q:n','q:n',label= '< ' + produccionesP+ ' >')
                dot.edge('q:s','q:s',label= '< ' + tipo3+ ' >')
                dot.edge('q','f',label= '<λ;λ;#> ')                                                
            mensaje += """"<hr width="200%" size=5000 color="black">
                            <h1 align="center"> Iteración """+str(contador)+""": </h1>
            
                """ + dot.pipe().decode('utf-8')  +"""
                <table id="mitabla">
                <tfoot class="pie">
                <tr>
                <td class="ccc"> Pila:      </td>
                <td class="aaa">      """+ pila_t + """ </td>
                </tr>
                </tfoot>
                </table>     
                <br>  
                <table id="mitabla">
                <tfoot class="pie">
                <tr>
                <td class="ccc"> Entrada:    </td>
                <td class="aaa">      """+ entrada_t + """  </td>
                </tr>
                </tfoot>
                </table>                                         
            """   

            mensaje +=""" <p style="background: #222222; color: white; font-weight: bold; padding: 15px; border-left: 8px solid #ff0080; border-top-right-radius: 8px; border-bottom-right-radius: 8px;">
                        LA CADENA ES ACEPTADA.</p>"""        

        mensaje += """                      
                    </form>
                    </div>
                    </div>
                    </div>
                    </body>
                    </html>  
                """ 

        f.write(mensaje)
        f.close()    
        webbrowser.open_new_tab(nombreW)       

