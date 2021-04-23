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
     opcion = int(input( "Menu: \n 1)Cargar Archivo: \n 2)Informacion General \n 3)Generar autómata de pila equivalente: \n 4)Reporte Recorrido: \n 5)Reporte en tabla: \n 6) Salir \n-->"))
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
            entrad = "aaaaaazba"
            for grm in gramaticasL: 
                if grm.getID() == id:
                    grm.informacionGeneral()
                    # grm.generaTablas(entrad)
                    grm.generRecorridoImagenes(entrad)
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
                    print("No se encontro la gramatica")
        elif opcion == 4: 
            id = nombreOpciones()
            cadena = str(input("Ingrese la cadena a Evaluar: \n --->"))
            for grm in gramaticasL: 
                if grm.getID() == id:
                    grm.generaTablas(cadena.strip())
                    break
                else: 
                    print("No se encontro la gramatica")
        elif opcion == 5: 
            id = nombreOpciones()
            cadena = str(input("Ingrese la cadena a Evaluar: \n --->"))
            for grm in gramaticasL: 
                if grm.getID() == id:
                    grm.generRecorridoImagenes(cadena.strip())
                    break
                else: 
                    print("No se encontro la gramatica")
        
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
            if save: 
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
                print("")
            indicadorLinea = 1
            Nombre = ""
            terminales.clear()
            noTerminales.clear()
            producciones.clear()
            So = ""
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
    