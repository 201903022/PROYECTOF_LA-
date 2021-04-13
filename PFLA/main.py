from tkinter import filedialog as FileDialog
from gramaticas import Gramatica
from nodo import gramaticas
gramaticasL = []
afd = []
gramaticasS = gramaticas()
def test():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero")
    #print (fichero)
    return fichero

def pedirOpcion ():
  correcto = False
  opcion = 0
  while (not correcto):
    try:
     opcion = int(input( "Menu: \n 1) Cargar Archivo: \n 2)Desplegar listas ordenadas \n 3) Desplegar búsquedas: \n 4) Desplegar todas: \n5) Desplegar todos los archivos: \n 6) Salir \n-->"))
     correcto = True
    except ValueError:
      print('Error, introduce un numero entero')
  return opcion

def Menu(): 
    opcion = 0
    salir = False
    while not salir: 
        opcion = pedirOpcion()
        if opcion == 1: 
            #leer archvivo
            ruta = test()
            prueba(ruta)
        elif opcion == 2: 
            a = "Mostrar informacion general"
        elif opcion == 3: 
            a = "ingresar cadena: "
        
def leerLine(lineaE,cont_lineas): 
    global gramaticas
    linea = str(lineaE)
    print(linea)
    tamañoEntrada = len(linea)
    cont = 0
    tmp = []
    if cont_lineas == 1: 
        # concatenacion = ""
        while(cont<tamañoEntrada):
            chart = linea[cont]
            charti = ord(chart)
            cont += 1
        print("nombre")
    
    elif cont_lineas == 2: 
        # concatenacion = ""
        terminales = []
        noTerminales = []
        So = ""
        estado = 0
        while(cont<tamañoEntrada):
            chart = linea[cont]
            charti = ord(chart)
            if estado == 0: 
                if chart.isupper(): 
                    noTerminales.append(chart)
                    cont +=1 
                elif chart=="," or charti==32: 
                    cont +=1  
                elif chart == ";" :
                    print("Terminales")
                    estado == 1
           
            elif estado == 1: 
                if chart.isupper(): 
                    terminales.append(chart)
                    cont +=1 
                elif chart=="," or charti==32: 
                    cont +=1 
                elif chart == ";":
                    print("Terminales")
                cont +=1  
           
            elif estado == 2: 

                if charti ==32: 
                    cont+1
                elif chart.isupper(): 
                    So+=chart
                elif chart == "\n": 
                    print("Fin")
       
    elif cont_lineas >2: 
        
        print("producciones")

def prueba(ruta): 
    archivo = open(ruta)
    indicadorLinea = 1
    Nombre = ""
    global terminales
    global noTerminales
    # noTerminales = []
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
            for item in producciones: 

                if item[0] in noTerminales :
                    print("si")
                    if len(item[1])>1: 
                        print("mayor que 1: ",item[1].split(" "))
                    else: 
                        if item[1] in noTerminales: 
                            no_tipo2 = True
                        elif item[1] in terminales: 
                            no_tipo2 = False
                            break
                else: 
                    print("que paso master xD")
            if save: 
                temp.append(Gramatica(Nombre,noTerminales,terminales,So,producciones))
                for grm in temp: 
                    if grm.getNombre() == Nombre:
                        grm.informacionGeneral(Nombre) 
                        break
                no_gramatica +=1
            else: 
                print("")
            Nombre = ""
            terminales.clear()
            noTerminales.clear()
            producciones.clear()
            So = ""
            indicadorLinea == 1
        else: 
            if indicadorLinea == 1: 
                # concatenacion = ""
                Nombre += linea.strip() 
                # indicadorLinea +=1 

            elif indicadorLinea == 2: 
                tamañoEntrada = len(linea)
                cont = 0
                estado = 0                
                y = linea.split(";")
                x = y[0].split(",")
                terminales = y[0].split(",")
                x1 = y[1].split(",")
                noTerminales = y[1].split(",")
                print("noTerminales ",noTerminales)
                So += y[2]
                print("X: ",So)
                while(cont<tamañoEntrada):
                    chart = linea[cont]
                    charti = ord(chart)

                    if estado == 0: 
                        if chart.isupper(): 
                            noTerminales.append(chart)
                            cont +=1 
                        elif chart=="," or charti==32: 
                            cont +=1  
                        elif chart == ";" :
                            estado =1 
                            cont += 1               
                    elif estado == 1: 

                        if chart !=",": 
                            terminales.append(chart)
                            cont +=1 
                        else: 
                            if chart=="," or charti==32: 
                                cont +=1 
                            elif chart == ";":
                                estado = 2 
                                cont +=1  
                
                    elif estado == 2: 
                        if charti ==32: 
                            cont+1
                        elif chart !=",": 
                            a=chart
                            cont+=1
                        elif chart == "\n": 
                            print("Fin")
            
            elif indicadorLinea >2: 
                producciones.append(linea.split("->"))
        indicadorLinea +=1        

Menu()
    