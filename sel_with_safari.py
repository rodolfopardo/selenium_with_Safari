#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:10:10 2019

@author: rodolfopardo
"""
#Importo las librerias 

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



#Funcion para comenzar con Google Chrome y busca la etiqueta

tit_portada = ""
tit_home = ""

def browser(x):
    driver = webdriver.Safari()
    return driver

def titulos_portada(*args):
    driver.get(url)
    time.sleep(2)
    tit_portada = driver.find_elements_by_class_name('poster-title')
    time.sleep(2)
    return tit_portada

def titulos_home(*args):
    driver.get(url)
    time.sleep(2)
    tit_home = driver.find_elements_by_class_name('abstract-title')
    time.sleep(2)
    return tit_home


titulos_portada(url, driver)
titulos_home(url, driver)

#Guardo las variables 

tit_portada = titulos_portada(tit_portada)
tit_home = titulos_home(tit_home)

#List Comprehension

tit_portada = [i.text for i in tit_portada]
tit_home = [i.text for i in tit_home]

