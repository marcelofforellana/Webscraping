# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:50:52 2020

@author: marce
"""

import random
from time import sleep
from selenium import webdriver
import pandas as pd

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome('./chromedriver.exe') 

# Voy a la pagina que requiero
driver.get('https://www.latercera.com/categoria/nacional/')


# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural

news = driver.find_elements_by_xpath('//article[@class="card | border-bottom float"]')

url=list()
title=list()
summary=list()
patron=list()

# Recorro cada uno de los anuncios que he encontrado
for new in news:
   
    # extraigo la url
    link=new.find_element_by_xpath('.//a')
    url.append(link)
    #print (link)
    # Por cada anuncio hallo el titulo
    titulo = new.find_element_by_xpath('.//h3[@class=""]').text
    title.append(titulo)
   # print (titulo)
   
    # Por cada anuncio hallo la descripcion
    descripcion = new.find_element_by_xpath('.//div[@class="deck | isText"]').text
    summary.append(descripcion)
   # print (descripcion)
#%%
   
# Creacion de dataframe
table=pd.DataFrame({'url': url, 'titulo':title, 'resumen':summary,"patron":0})
table.head()
    
#%%

#Para buscar texto o algun patron de texto por ejemplo Coronavirus.

busqueda=["Paso a Paso"] #Se le pueden agregar mas patrones

for i in range(len(table["resumen"])):
    count=0
    for palabra in busqueda:
        if palabra in table["resumen"][i]:
            count+=1
        else:
            continue 
    if count==len(busqueda):
        table["patron"][i]=1
    else:
        continue
    
target= table[table["patron"]==1] #Me quedo solamente conlas que tienen el patron 
#%%

# Aqui deberia haber un boton que pasara a la siguiente pagina  UWU

boton = driver.find_element_by_xpath('')
for i in range(3): # Voy a darle click en cargar mas 3 veces
    try:
        # le doy click
        boton.click()
        # espero que cargue la informacion dinamica
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element_by_xpath('')
    except:
        # si hay algun error, rompo el lazo.
        break