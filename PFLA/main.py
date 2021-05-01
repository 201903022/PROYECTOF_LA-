from tkinter import filedialog as FileDialog
from gramaticas import Gramatica
from nodo import gramaticas
from gramaticasE import GramaticaE
gramaticasL = []
gramaticasS = gramaticas()
gramaticasE = [] 
def test():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    #print (fichero)
    return fichero

def pedirOpcion ():
  correcto = False
  opcion = 0
  while (not correcto):
    try:
     opcion = int(input( "Menu: \n 1)Cargar Archivo: \n 2)Informacion General \n 3)Generar autómata de pila equivalente: \n 4)Reporte en tabla: \n 5)Reporte en Recorrido: \n 6) Gramaticas no aceptadas \n 7) Salir \n-->"))
     correcto = True
    except ValueError:
      print('Error, introduce un numero entero')
  return opcion

def Menu(): 
    global gramaticasL
    opcion = 0
    salir = False
    while not salir: 
        opcion = pedirOpcion()
        if opcion == 1: 
            #leer archvivo
            ruta = test()
            prueba(ruta)
        elif opcion == 2: 
            id = nombreOpciones()
            for grm in gramaticasL: 
                if grm.getID() == id:
                    grm.informacionGeneral()
                    break
                else: 
                    print("No se encontro la gramatica")
        elif opcion == 3: 
            
            id = nombreOpciones()
            for grm in gramaticasL: 
                if grm.getID() == id:
                    grm.pilaE()
                    break
                else: 
                    pass
        elif opcion == 4: 
        
            id = nombreOpciones()
            cadena = str(input("Ingrese la cadena a Evaluar: \n --->"))
            find = False
            for grm in gramaticasL: 
                if grm.getID() == id:
                    print("1 - Evaluar GLC simple\n2 - Evaluar GLC con ambigüedad")
                    opc = input(" Selecciona una opción: ")
                    if opc == "1":
                        grm.generaTablas(cadena.strip())
                        pass
                    elif opc == "2":
                        grm.generaTablas2(cadena.strip())
                    else:
                        print("Selección inválida")
                    find = True
                    break
            if not find: 
                print("No se encontro la gramatica")            
                
        elif opcion == 5: 
            id = nombreOpciones()
            cadena = str(input("Ingrese la cadena a Evaluar: \n --->"))
            find = False
            for grm in gramaticasL: 
                if grm.getID() == id:
                    print("1 - Evaluar GLC simple\n2 - Evaluar GLC con ambigüedad")
                    opc = input(" Selecciona una opción: ")
                    if opc == "1":
                        grm.generRecorridoImagenes(cadena.strip())
                        pass
                    elif opc == "2":
                        grm.generaRecorrido2(cadena.strip())
                    else:
                        print("Selección inválida")
                    find = True
                    break
            if not find: 
                print("No se encontro la gramatica")  
        elif opcion == 6: 
            if len(gramaticasE)>0: 
                web = True
                if web: 
                    import webbrowser
                    f = open("Regulares.html",mode="w", encoding="utf-8")
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
                            <p >GRMATICAS Regulares</p>
                        </div>
                        </div>
                        <div class="main">
                        <div class="col-md-6 col-sm-12">
                            <div class="login-form">
                            <h1>Mostrando</h1>
                            <form>
                        """
                    for grmR in gramaticasE: 
                        mensaje +=""" 
                                <div class="form-group">
                                    <label> NOMBRE:  </label>
                                    <input id = "username"type="text" class="form-control" value =  """ + str(grmR.getNombre())+  """ onkeydown="return false" >  
                                </div>   
                                <div class="form-group">
                                    <label> Terminales:  </label> 
                                    <input id = "username"type="text" class="form-control" value =  {""" + str((",".join(grmR.get_Teminales())) + "}")+  """  onkeydown="return false" >                                          
                                </div>                                 
                                <div class="form-group">
                                    <label> Error:  </label>
                                    <input id = "username"type="text" class="form-control" value =  """ + str(grmR.getError())+  """ onkeydown="return false" >  
                                </div>  
                                <br>
                                <br> 
                        """ 
              
                    mensaje += """  
                        <h1>Representacion Grafica SVG</h1>                
                        </form>
                        </div>
                        </div>
                        </div>
                        </body>
                        </html>  
                    """ 
                    f.write(mensaje)
                    f.close()    
                    webbrowser.open_new_tab("Regulares.html")              

            else: 
                print("Todas son de tipo 2")   

        elif opcion == 7: 
            salir = True        

def prueba(ruta): 
    archivo = open(ruta)
    indicadorLinea = 1
    Nombre = ""
    global terminales
    global noTerminales
    global gramaticasL
    So = ""
    producciones = []
    temp = []
    no_gramatica = 1
    for linea1 in archivo.readlines(): 
        linea = linea1.rstrip()
        chart = linea[0]
        if chart == "*": 
            no_tipo2 = True
            save = True
            regular = True

            for elemen in producciones: 
                if len(elemen[1]) ==1:
                    if len(elemen) == 1: 
                        #a
                        if elemen in terminales: 
                            regular = True
                        else: 
                            regular = False
                            break 
                else: 
                    pro = elemen[1].split(" ")  
                    if len(pro) == 2: 
                        # a A ; pro -> ['a','A']
                        #aA 
                        if pro[0] in terminales: #pro[0] = a  pro[1] = A 
                            if pro[0] in terminales and pro[1] in noTerminales: 
                                regular = True
                            else : 
                                regular = False
                                break
                        #Aa 
                        elif pro[0] in noTerminales: 
                            if pro[0] in noTerminales and pro[1] in  terminales: 
                                regular = True
                            else : 
                                regular = False
                                break
                    elif len(pro) >2: 
                        regular = False
                        break

            if not regular:                 
                import copy
                id = generaID()
                # print("Producciones",producciones)
                produccionesS = producciones.copy()
                # noTerminales.append("#")
                # print("No Terminales: ",noTerminales)
                terminalesS = terminales.copy()
                noTerminalesS = noTerminales.copy()
                gramaticasL.append(copy.deepcopy(Gramatica(id,Nombre,noTerminalesS,terminalesS,So,produccionesS)))
                no_gramatica +=1
            else: 
                gramaticasE.append(copy.deepcopy(GramaticaE(id,Nombre,noTerminales.copy(),terminales.copy(),So,producciones.copy(),"Es regular")))


            indicadorLinea = 1
            Nombre = ""
            terminales.clear()
            noTerminales.clear()
            producciones.clear()
            So = ""
            print("Almacenadas")
        else: 
            if indicadorLinea == 1: 
                # concatenacion = ""
                Nombre += linea.strip() 
                # print("Nombre ",Nombre)
                # indicadorLinea +=1 
                indicadorLinea +=1

            elif indicadorLinea == 2:            
                y = linea.split(";")
                noTerminales = y[0].split(",")
                terminales = y[1].split(",")
                # print("noTerminales ",noTerminales)
                So += y[2]
                indicadorLinea +=1

            elif indicadorLinea >2: 
                producciones.append(linea.split("->"))
                indicadorLinea +=1        

def nombreOpciones(): 
    print("*****Gramaticas****")
    formulario = ""
    for grm in gramaticasL: 
        formulario += str(grm.getID())+" "+grm.getNombre() + " \n"
    formulario += " \n -->"
    gramatica = int(input(formulario))
    return gramatica

def generaID(): 
    id = 1 
    if len(gramaticasL) == 0: 
        id = 1 
        return id
    else: 
        pos = len(gramaticasL)-1
        id = gramaticasL[pos].getID() + 1
        return id

def regular(): 
    terminales = []
    noTerminales = []
    producciones = []
    regular = True
    error = ""
    for elemen in producciones: 
        if len(elemen) >0:
            if len(elemen) == 1: 
                #a
                if elemen in terminales: 
                    regular = True
                else: 
                    regular = False
                    break 
            elif len(elemen) == 2: 
                print("Mayor 2")
                pro = elemen.split(" ")  
                # a A ; pro -> ['a','A']
                #aA 
                if pro[0] in terminales: #pro[0] = a  pro[1] = A 
                    if pro[0] in terminales and pro[1] in noTerminales: 
                        regular = True
                    else : 
                        regular = False
                        break
                #Aa 
                if pro[0] in noTerminales: 
                    if pro[0] in noTerminales and pro[1] in  terminales: 
                        regular = True
                    else : 
                        regular = False
                        break
            elif len(elemen) >2: 
                print("No es regular, entonces es libre de contexto")
                regular = False
                break
        
Menu()
    