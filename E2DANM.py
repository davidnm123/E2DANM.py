import os 
from bs4 import BeautifulSoup as bs
try: 
    import webbrowser 
except ImportError: 
    os.system('pip install webbrowser') 
    print('Installing webbrowser...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
try: 
    import sys 
except ImportError: 
    os.system('pip install sys') 
    print('Installing sys...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
try: 
    import requests 
except ImportError: 
    os.system('pip install requests') 
    print('Installing requests...') 
    print('Ejecuta de nuevo tu script...') 
    exit()
try: 
    from bs4 import BeautifulSoup as bs 
except ImportError: 
    os.system('pip install BeautifulSoup') 
    print('Installing BeautifulSoup...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

# DAVID ALEJANDRO NAVARRO MENDOZA
# El código de arriba sirve más que nada para checar si está instalado un módulo,
# y si está instalado lo va correr bien pero si un módulo no está instalado lo que va a hacer
# es que va a ocurrir un excpeción y se va a empezar a instalar el módulo para despúes cerrarse y tengas que volver a ejecutar el programa
print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
# En esta última parte del código se va a buscar en la página de la UANL las noticias y nos van a pedir de que página a que página queremos buscar
# y una vez que ingresemos eso se va a buscar la página si hya erroes como el "200" va a aparecer como página no enciontrada pero si está bien la página se va a buscar perfectamente.
