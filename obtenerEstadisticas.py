###################################################################################
#version 1.0.0																	  #
#author Erika Sarai Rosas Quezada												  #	
#Script: Para obtener estadisticas de las 10 empresas 				     		  #
###################################################################################

#----------------------------------------------------------------------------------#
import nltk
import sklearn
from xml.dom import minidom  #libreria para leer archivos xml"
import csv
import xml.etree.cElementTree as ET
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import collections
from statistics import mean
from statistics import pstdev
import numpy as np
import join

#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
#########################Declaracion de funciones ##################################

#----------------------Leer csv----------------------------------------------------#
def leerCSV (archivoCSV):
	#leer el archivo csv
	datos=pd.read_csv(archivoCSV,header=0)
	return datos 
#----------------------Obtener numero de publicaciones por empresa-----------------#
def numeroDePublicacionesTotales(datos):
	
    listaParaTotaldePublicaciones.append(datos['nombre'][0])#Agregar Nombre
    listaParaTotaldePublicaciones.append(len(datos)) #Agregar Total de publicaciones
    listaTotalDePublicaciones.append(len(datos))
    print("---------------",datos['nombre'][0],"------------------------------------")
    return len(datos)
#----------------------Crear grafica del total de publicacines por empresa---------#
def graficoDeTotalDeEmpresas():
	
	#Descripcion
	o=0
	print("Total de publicaciones por empresa\n")
	while (len(listaParaTotaldePublicaciones)>o):
		print(listaParaTotaldePublicaciones[o],"=",listaParaTotaldePublicaciones[o+1])
		o=o+2 
	
	data = {listaParaTotaldePublicaciones[0]:listaParaTotaldePublicaciones[1],
            listaParaTotaldePublicaciones[2]:listaParaTotaldePublicaciones[3],
            listaParaTotaldePublicaciones[4]:listaParaTotaldePublicaciones[5],
            listaParaTotaldePublicaciones[6]:listaParaTotaldePublicaciones[7],
            listaParaTotaldePublicaciones[8]:listaParaTotaldePublicaciones[9],
            listaParaTotaldePublicaciones[10]:listaParaTotaldePublicaciones[11],
            listaParaTotaldePublicaciones[12]:listaParaTotaldePublicaciones[13],
            listaParaTotaldePublicaciones[14]:listaParaTotaldePublicaciones[15],
            listaParaTotaldePublicaciones[16]:listaParaTotaldePublicaciones[17],
            listaParaTotaldePublicaciones[18]:listaParaTotaldePublicaciones[19],
            listaParaTotaldePublicaciones[20]:listaParaTotaldePublicaciones[21],
            listaParaTotaldePublicaciones[22]:listaParaTotaldePublicaciones[23],
            listaParaTotaldePublicaciones[24]:listaParaTotaldePublicaciones[25],
            listaParaTotaldePublicaciones[26]:listaParaTotaldePublicaciones[27],
            listaParaTotaldePublicaciones[28]:listaParaTotaldePublicaciones[29],
            listaParaTotaldePublicaciones[30]:listaParaTotaldePublicaciones[31],
            listaParaTotaldePublicaciones[32]:listaParaTotaldePublicaciones[33],
            listaParaTotaldePublicaciones[34]:listaParaTotaldePublicaciones[35],
            listaParaTotaldePublicaciones[36]:listaParaTotaldePublicaciones[37],
            listaParaTotaldePublicaciones[38]:listaParaTotaldePublicaciones[39],
            listaParaTotaldePublicaciones[40]:listaParaTotaldePublicaciones[41],
            listaParaTotaldePublicaciones[42]:listaParaTotaldePublicaciones[43],
            listaParaTotaldePublicaciones[44]:listaParaTotaldePublicaciones[45],
            listaParaTotaldePublicaciones[46]:listaParaTotaldePublicaciones[47]}

	group_data = list(data.values())
	group_names = list(data.keys())
	group_mean = np.mean(group_data)
	fig, ax = plt.subplots()
	ax.barh(group_names, group_data)
	labels = ax.get_xticklabels()
	plt.style.use('fivethirtyeight')
	plt.setp(labels, rotation=100, horizontalalignment='right')
	plt.tick_params(axis='both', which='major', labelsize=8)
	ax.barh(group_names, group_data)
	plt.show()
#--------------------Obtener numero promedio de publicaciones de cada año ---------#
def numeroPromedioDePublicacionesPorAno(empresa):
	listaAnos=[]
	numeroPorAño=[]
	##Obtener lista años
	listaAnos=list(empresa['AnoP'])
	##Obtener numero de publicaciones por año
	numeroPorAño.append(listaAnos.count(2018))
	numeroPorAño.append(listaAnos.count(2017))
	numeroPorAño.append(listaAnos.count(2016))
	##Obtener promedio 
	print ("Promedio de publicaciones al año", mean(numeroPorAño)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(numeroPorAño)) 
	##Agregar a lista de empresas
	listaParaPromedioDePublicacionesAlano.append(mean(numeroPorAño))
	
	return numeroPorAño
#---------------------Obtener numero promedio de caracteres por texto -------------#
def numeroPromedioDeCaracteresPorTexto(empresa):
	listaTexto=[]
	listaNumeroDeCaracteres=[0]
	p=0
	##Obtener texto 
	listaTexto=list(empresa['texto'])
	##Recorrer lista texto para obtener total de caracteres
	while(len(listaTexto)>p):
		listaNumeroDeCaracteres.append(len(listaTexto[p]))
		p=p+1;
	##Obtener promedio 
	print ("Promedio de caracteres por publicacion", mean(listaNumeroDeCaracteres)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaNumeroDeCaracteres))
	
	return listaNumeroDeCaracteres
#----------------------Obtener numero promedio de palabras por publicacion --------#
def numeroPromedioDePalabrasPorTexto(empresa):
	listaTexto=[]
	listaNumeroDePalabras=[]
	listaPublicacion=[]
	p=0
	##Obtener texto 
	listaTexto=list(empresa['texto'])
	##Recorrer lista texto para obtener total de caracteres
	while(len(listaTexto)>p):
		listaPublicacion=listaTexto[p].split()
		listaNumeroDePalabras.append(len(listaPublicacion))
		listaPublicacion=[]
		p=p+1;
	##Obtener promedio 
	print ("Promedio de palabras por publicacion", mean(listaNumeroDePalabras)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaNumeroDePalabras))
	
	return listaNumeroDePalabras
#----------------------Obtener numero promedio de Emojis---------------------------#
def numeroPromedioDeEmojisPorTexto(empresa):
	listaEmojis=[]
	listaEmojis=list(empresa['emojis'])
	##Obtener promedio 
	print ("Promedio de emojis por publicacion", mean(listaEmojis)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaEmojis))
	
	return listaEmojis
#----------------------Obtener numero promedio de Hashtag---------------------------#
def numeroPromedioDeHashtagPorTexto(empresa):
	listaHashtag=[]
	listaHashtag=list(empresa['hashtag'])
	##Obtener promedio 
	print ("Promedio de Hashtag por publicacion", mean(listaHashtag)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaHashtag))
	return listaHashtag
#----------------------Obtener numero promedio de link---------------------------#
def numeroPromedioDeLinkPorTexto(empresa):
	listaLink=[]
	listaLink=list(empresa['linkTotales'])
	##Obtener promedio 
	print ("Promedio de Link por publicacion", mean(listaLink)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaLink))
	return listaLink
#----------------------Obtener numero promedio de link imagenes--------------------#
def numeroPromedioDeLinkImages(empresa):
	listaLinkImg=[]
	listaLinkImg=list(empresa['linkImg'])
	##Obtener promedio 
	print ("Promedio de Link img por publicacion", mean(listaLinkImg)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaLinkImg))
	
	return listaLinkImg
#----------------------Obtener numero promedio de link videos---------------------#
def numeroPromedioDeLinkVideos(empresa):
	listaLinkVideos=[]
	listaLinkVideos=list(empresa['linkVid'])
	##Obtener promedio 
	print ("Promedio de Link videos por publicacion", mean(listaLinkVideos)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaLinkVideos))
	return listaLinkVideos
	
#----------------------Obtener numero promedio de link videos---------------------#
def numeroPromedioDeLinkAlb(empresa):
	listaLinkAlb=[]
	listaLinkAlb=list(empresa['linkAlb'])
	##Obtener promedio 
	print ("Promedio de Link album por publicacion", mean(listaLinkAlb)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaLinkAlb))
	return listaLinkAlb
#----------------------Obtener numero promedio de link otros-----------------------#
def numeroPromedioDeLinkOtros(empresa):
	listaLinkOtro=[]
	listaLinkOtro=list(empresa['linkOtro'])
	##Obtener promedio 
	print ("Promedio de Link otros por publicacion", mean(listaLinkOtro)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaLinkOtro))
	return listaLinkOtro
#--------------------Obtener numero promedio de reacciones totales-----------------#
def numeroPromedioDeReaccionesPorPublicacion(empresa):
	listaReacciones=[]
	listaReacciones=list(empresa['reaccionesTotales'])
	##Obtener promedio 
	print ("Promedio de reacciones por publicacion", mean(listaReacciones)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReacciones))
	##Obtener reacciones totales 
	f=0
	global totalDeReaccionesDeLaEmpresa
	
	while(len(listaReacciones)>f):
		totalDeReaccionesDeLaEmpresa=totalDeReaccionesDeLaEmpresa+listaReacciones[f]
		f=f+1
	return listaReacciones
#--------------------Obtener numero promedio de reacciones <me gusta>--------------#
def numeroPromedioDeReaccionesMeGustaPorPublicacion(empresa):
	listaReaccionesMeGusta=[]
	listaReaccionesMeGusta=list(empresa['Me_gusta'])
	totalMeGusta=0
	
	##Obtener promedio 
	print ("Promedio de reacciones me gusta por publicacion", mean(listaReaccionesMeGusta)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMeGusta))
	
	##Obtener numero de todos los me gusta por paginas 
	a=0
	while(len(listaReaccionesMeGusta)>a):
			totalMeGusta=totalMeGusta+listaReaccionesMeGusta[a]
			a=a+1
	##Guardar los totales de empresa	
	listaParaGuardarNumeroDeReacciones.append("Me_gusta")
	listaParaGuardarNumeroDeReacciones.append(totalMeGusta)
	## Sumar al total de todas las empresa
	global totalDeMeGustaDeTodasLasEmpresas
	totalDeMeGustaDeTodasLasEmpresas=totalDeMeGustaDeTodasLasEmpresas+totalMeGusta
	
	return listaReaccionesMeGusta
#--------------------Obtener numero promedio de reacciones <me asombra>--------------#
def numeroPromedioDeReaccionesMeAsombraPorPublicacion(empresa):
	listaReaccionesMe_asombra=[]
	listaReaccionesMe_asombra=list(empresa['Me_asombra'])
	totalDeMeAsombra=0
	##Obtener promedio 
	print ("Promedio de reacciones me asombra por publicacion", mean(listaReaccionesMe_asombra)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMe_asombra))
	
	##Obtener numero total de me asombra 
	a=0
	while(len(listaReaccionesMe_asombra)>a):
			totalDeMeAsombra=totalDeMeAsombra+listaReaccionesMe_asombra[a]
			a=a+1
	##Guardar reaccion		
	listaParaGuardarNumeroDeReacciones.append("Me_asombra")
	listaParaGuardarNumeroDeReacciones.append(totalDeMeAsombra)
	##Guardar en todas las empresas
	global totalDeMe_asombraDeTodasLasEmpresas
	totalDeMe_asombraDeTodasLasEmpresas=totalDeMe_asombraDeTodasLasEmpresas+totalDeMeAsombra
	
	return listaReaccionesMe_asombra
#--------------------Obtener numero promedio de reacciones <me divierte>--------------#
def numeroPromedioDeReaccionesMeDiviertePorPublicacion(empresa):
	listaReaccionesMe_divierte=[]
	listaReaccionesMe_divierte=list(empresa['Me_divierte'])
	totalDeMeDivierte=0
	##Obtener promedio 
	print ("Promedio de reacciones me divierte por publicacion", mean(listaReaccionesMe_divierte)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMe_divierte))
	
	##Obtener numero total de me diviete
	a=0
	while(len(listaReaccionesMe_divierte)>a):
		totalDeMeDivierte=totalDeMeDivierte+listaReaccionesMe_divierte[a]
		a=a+1
	##Guardar reacciones
	listaParaGuardarNumeroDeReacciones.append("Me_divierte")
	listaParaGuardarNumeroDeReacciones.append(totalDeMeDivierte)
	##Guardar en todas las empresas
	global totalDeMe_divierteDeTodasLasEmpresas
	totalDeMe_divierteDeTodasLasEmpresas=totalDeMe_divierteDeTodasLasEmpresas+totalDeMeDivierte	
	
	return listaReaccionesMe_divierte
	
#--------------------Obtener numero promedio de reacciones <me enoja>--------------#
def numeroPromedioDeReaccionesMeEnojaPorPublicacion(empresa):
	listaReaccionesMe_enoja=[]
	listaReaccionesMe_enoja=list(empresa['Me_enoja'])
	totalDeMeEnoja=0
	##Obtener promedio 
	print ("Promedio de reacciones me enoja por publicacion", mean(listaReaccionesMe_enoja)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMe_enoja))
	
	##Obtener numero de total de enoja
	a=0
	while(len(listaReaccionesMe_enoja)>a):
		totalDeMeEnoja=totalDeMeEnoja+listaReaccionesMe_enoja[a]
		a=a+1
	##Guardar reacciones
	listaParaGuardarNumeroDeReacciones.append("Me_enoja")
	listaParaGuardarNumeroDeReacciones.append(totalDeMeEnoja)
	##Guardar en todas las empresas
	global totalDeMe_enojaDeTodasLasEmpresas
	totalDeMe_enojaDeTodasLasEmpresas=totalDeMe_enojaDeTodasLasEmpresas+totalDeMeEnoja
	
	
	return listaReaccionesMe_enoja
#--------------------Obtener numero promedio de reacciones <me encanta>--------------#
def numeroPromedioDeReaccionesMeEncantaPorPublicacion(empresa):
	listaReaccionesMe_encanta=[]
	listaReaccionesMe_encanta=list(empresa['Me_encanta'])
	totalDeMeEncanta=0
	##Obtener promedio 
	print ("Promedio de reacciones me encanta por publicacion", mean(listaReaccionesMe_encanta)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMe_encanta))
	
	##Obtener numero de total de me encanta
	a=0
	while(len(listaReaccionesMe_encanta)>a):
		totalDeMeEncanta=totalDeMeEncanta+listaReaccionesMe_encanta[a]
		a=a+1
	##Guardar reacciones
	listaParaGuardarNumeroDeReacciones.append("Me_encanta")
	listaParaGuardarNumeroDeReacciones.append(totalDeMeEncanta)
	##Guardar en todas las empresas
	global totalDeMe_encantaDeTodasLasEmpresas
	totalDeMe_encantaDeTodasLasEmpresas=totalDeMe_encantaDeTodasLasEmpresas+totalDeMeEncanta
	
	return listaReaccionesMe_encanta
#--------------------Obtener numero promedio de reacciones <me entristece>--------------#
def numeroPromedioDeReaccionesMeEntristecePorPublicacion(empresa):
	listaReaccionesMe_entristece=[]
	listaReaccionesMe_entristece=list(empresa['Me_entristece'])
	totalDeMeEntristece=0
	##Obtener promedio 
	print ("Promedio de reacciones me entristece por publicacion", mean(listaReaccionesMe_entristece)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesMe_entristece))
	
	##Obtener numero de total de me encanta
	a=0
	while(len(listaReaccionesMe_entristece)>a):
		totalDeMeEntristece=totalDeMeEntristece+listaReaccionesMe_entristece[a]
		a=a+1
	##Guardar reacciones
	listaParaGuardarNumeroDeReacciones.append("Me_entristece")
	listaParaGuardarNumeroDeReacciones.append(totalDeMeEntristece)
	##Guardar en todas las empresas
	global totalDeMe_entristeceDeTodasLasEmpresas
	totalDeMe_entristeceDeTodasLasEmpresas=totalDeMe_entristeceDeTodasLasEmpresas+totalDeMeEntristece
	
	return listaReaccionesMe_entristece
#--------------------Obtener numero promedio de veces compartidos-----------------------#
def numeroPromedioDeReaccionesVecesCompartidosPorPublicacion(empresa):
	listaReaccionesVecesCompartidos=[]
	listaReaccionesVecesCompartidos=list(empresa['veces_compartido'])
	totalDeVeces=0
	##Obtener promedio 
	print ("Promedio de compartidos por publicacion", mean(listaReaccionesVecesCompartidos)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesVecesCompartidos))
	
	##obtener numero de veces 
	a=0
	while(len(listaReaccionesVecesCompartidos)>a):
		totalDeVeces=totalDeVeces+listaReaccionesVecesCompartidos[a]
		a=a+1
	
	listaParaGuardarNumeroDeReacciones.append("Veces_Compartidos")
	listaParaGuardarNumeroDeReacciones.append(totalDeVeces)
	
	##Guardas en todos las veces
	global totalDeVecesCompartidos
	totalDeVecesCompartidos=totalDeVecesCompartidos+totalDeVeces
	
	
	return listaReaccionesVecesCompartidos
#--------------------Obtener numero promedio de comentarios------------------------------#
def numeroPromedioDeReaccionesComentariosPorPublicacion(empresa):
	listaReaccionesComentarios=[]
	listaReaccionesComentarios=list(empresa['Comentarios'])
	totalDeCome=0
	##Obtener promedio 
	print ("Promedio de comentarios  por publicacion", mean(listaReaccionesComentarios)) 
	##Obtener desviacion estandar
	print ("Desviacion estandar", pstdev(listaReaccionesComentarios))
	##obtener numero de comentarios 
	a=0
	while(len(listaReaccionesComentarios)>a):
		totalDeCome=totalDeCome+listaReaccionesComentarios[a]
		a=a+1
	
	listaParaGuardarNumeroDeReacciones.append("Comentarios")
	listaParaGuardarNumeroDeReacciones.append(totalDeCome)
	##Guardas en todos los comentarios
	global totalDeComentarios
	totalDeComentarios=totalDeComentarios+totalDeCome
	
	return listaReaccionesComentarios
#---------------------Graficar las reacciones de  las empresas ---------------------------#
def graficarReacciones(listaReacciones,titulo):
	
	data = {listaReacciones[0]:listaReacciones[1],
			listaReacciones[2]:listaReacciones[3],
			listaReacciones[4]:listaReacciones[5],
			listaReacciones[6]:listaReacciones[7],
			listaReacciones[8]:listaReacciones[9],
			listaReacciones[10]:listaReacciones[11]}
      
	group_data = list(data.values())
	group_names = list(data.keys())
	group_mean = np.mean(group_data)
	fig, ax = plt.subplots()
	ax.barh(group_names, group_data)
   # ax.set(xlim=[-10000, 140000], xlabel='Frecuencia', ylabel='Reacciones')
   # ax.title("Frecuencia de las reacciones con el boton me gusta")
	labels = ax.get_xticklabels()
	plt.style.use('fivethirtyeight')
	plt.setp(labels, rotation=45, horizontalalignment='right')
	plt.savefig(titulo+'.png')
    
	ax.barh(group_names, group_data)
#---------------------Graficar las reacciones sin me gusta ---------------------------#
def graficarReaccionesSinMeGusta(listaReacciones,titulo):
	
	data = {listaReacciones[2]:listaReacciones[3],
			listaReacciones[4]:listaReacciones[5],
			listaReacciones[6]:listaReacciones[7],
			listaReacciones[8]:listaReacciones[9],
			listaReacciones[10]:listaReacciones[11]}
      
	group_data = list(data.values())
	group_names = list(data.keys())
	group_mean = np.mean(group_data)
	fig, ax = plt.subplots()
	ax.barh(group_names, group_data)
   # ax.set(xlim=[-10000, 140000], xlabel='Frecuencia', ylabel='Reacciones')
   # ax.title("Frecuencia de las reacciones con el boton me gusta")
	labels = ax.get_xticklabels()
	plt.style.use('fivethirtyeight')
	plt.setp(labels, rotation=45, horizontalalignment='right')
	plt.savefig(titulo+'.png')
    
	ax.barh(group_names, group_data)

#----------------------Graficar los comentarios y compartidos ----------------------------#ç
def graficarVecesYComentarios(listaReacciones,titulo):
	data = {listaReacciones[12]:listaReacciones[13],
			listaReacciones[14]:listaReacciones[15]}
	
	group_data = list(data.values())
	group_names = list(data.keys())
	group_mean = np.mean(group_data)
	fig, ax = plt.subplots()
	ax.barh(group_names, group_data)
	# ax.set(xlim=[-10000, 140000], xlabel='Frecuencia', ylabel='Reacciones')
	#ax.title("Frecuencia de las reacciones con el boton me gusta")
	labels = ax.get_xticklabels()
	plt.style.use('fivethirtyeight')
	plt.setp(labels, rotation=45, horizontalalignment='right')
	plt.savefig(titulo+'.png')
	ax.barh(group_names, group_data)
#--------------------Graficar promedio de caracteres o palabras --------------------------#
def graficarPromedio(lista,titulo,x,y):
 #Graficar
#bins=range(1, r)
    plt.hist(lista,bins=100,edgecolor = 'black',  linewidth=1)
    plt.title(titulo)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True)
    plt.savefig(titulo+'.png')
    plt.show()
	
#--------------------Numero de publicaciones que contienen al menos alguna reaccion-------#
def numeroDePublicacionesQueContienenAlMenosReacciones(datos):
	listaReacciones=[]
	listaReacciones=list(datos['ListaReacciones'])
	s=0
	numeroDePublicacionesConReaccion=0
	#recorrer lista reacciones
	while(len(listaReacciones)>s):
		cadena=listaReacciones[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		#verificar que exitan las 6 reacciones 
		if(int(lista[0])!=0 or int(lista[1])!=0 or int(lista[2])!=0 or int(lista[3])!=0 or  int(lista[4])!=0 or int(lista[5])!=0 ):
			numeroDePublicacionesConReaccion=numeroDePublicacionesConReaccion+1
		
		
		s=s+1
		
	return numeroDePublicacionesConReaccion
#--------------------Numero de publicaciones que contiene las 6 reacciones --------------#
def numeroDePublicacionesQueContienenLas6Reacciones(datos):
	listaReacciones=[]
	listaReacciones=list(datos['ListaReacciones'])
	s=0
	numeroDePublicacionesConAl6aReaccion=0
	#recorrer lista reacciones
	while(len(listaReacciones)>s):
		cadena=listaReacciones[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		#verificar que exitan las 6 reacciones 
		if(int(lista[0])!=0 and int(lista[1])!=0 and int(lista[2])!=0 and int(lista[3])!=0 and int(lista[4])!=0 and int(lista[5])!=0 ):
			numeroDePublicacionesConAl6aReaccion=numeroDePublicacionesConAl6aReaccion+1
		
		s=s+1
	return numeroDePublicacionesConAl6aReaccion
#--------------------NUmero de publicaciones sin reacciones ------------------------------#
def numeroDePublicacionesSinReacciones(datos):
	listaReacciones=[]
	listaReacciones=list(datos['ListaReacciones'])
	s=0
	numeroDePublicacionesSinReaccion=0
	#recorrer lista reacciones
	while(len(listaReacciones)>s):
		cadena=listaReacciones[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		#verificar que exitan las 6 reacciones 
		if(int(lista[0]) == 0 and int(lista[1]) ==0 and int(lista[2])==0 and int(lista[3])==0 and int(lista[4])==0 and int(lista[5])==0 ):
			numeroDePublicacionesSinReaccion=numeroDePublicacionesSinReaccion+1
			print(lista)
		s=s+1
	
	return numeroDePublicacionesSinReaccion

#--------------------NUmero de publicaciones con solo la reaccion me gusta ---------------#
def numeroDePublicacionesSoloTienenLaReaccionMeGusta(datos):
	listaReacciones=[]
	listaReacciones=list(datos['ListaReacciones'])
	s=0
	numeroDePublicacionesConSoloMeGusta=0
	#recorrer lista reacciones
	while(len(listaReacciones)>s):
		cadena=listaReacciones[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		#verificar que exitan las 6 reacciones 
		if(int(lista[0])!=0 and int(lista[1])==0 and int(lista[2])==0 and int(lista[3])==0 and int(lista[4])==0 and int(lista[5])==0 ):
			numeroDePublicacionesConSoloMeGusta=numeroDePublicacionesConSoloMeGusta+1
		
		s=s+1
		
	return numeroDePublicacionesConSoloMeGusta
#-------------------Numero  de publicaciones que contienen comentarios y veces compartidos-#
def numeroDePublicacionesQueContienenComentariosYVecesCompartidos(datos):
	listaVyC=[]
	listaVyC=list(datos['ListaVyC'])
	s=0
	numeroDeCyV=0
	#recorrer lista reacciones
	while(len(listaVyC)>s):
		cadena=listaVyC[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		 
		if(int(lista[0])!=0 and int(lista[1])!=0):
			numeroDeCyV=numeroDeCyV+1
		
		s=s+1
	print("Contienen come y comp",numeroDeCyV)	
	return numeroDeCyV

#---------------------NUmero de publicaciones que contienen solo comentarios---------------#
def numeroDePublicacionesQueContienenSoloComentarios(datos):
	listaVyC=[]
	listaVyC=list(datos['ListaVyC'])
	s=0
	soloCom=0
	#recorrer lista reacciones
	while(len(listaVyC)>s):
		cadena=listaVyC[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		 
		if(int(lista[0]) ==0 and int(lista[1])!=0):
			soloCom=soloCom+1
		
		s=s+1
	print("Contienen comentarios ",soloCom)	
	return soloCom

#----------------Numero de publicaciones que coontienen solo veces compartidas------------#
def numeroDePublicacionesQueContienenSoloVeces(datos):
	listaVyC=[]
	listaVyC=list(datos['ListaVyC'])
	s=0
	soloVec=0
	#recorrer lista reacciones
	while(len(listaVyC)>s):
		cadena=listaVyC[s]
		#remplazar []
		reemplaza = "["
		cadena = cadena.replace(reemplaza,"")
		reemplaza = "]"
		cadena = cadena.replace(reemplaza,"")
		reemplaza = " "
		cadena = cadena.replace(reemplaza,"")
		lista= cadena.split(',')
		
		 
		if(int(lista[0]) !=0 and int(lista[1])==0):
			soloVec=soloVec+1
		
		s=s+1
	print("Contienen veces ",soloVec)	
	return soloVec
	
#--------------------Graficar las reacciones de todas las empresas------------------------#
#--------------------Crear csv de estadisiticas por empresa-------------------------------#
def crearCSVdeEstadisticas(diccionario,nombre):
	contador=0  
	
	with open(nombre+'.csv', 'a', newline='') as csvfile:
		fieldnames=["id","Empresa",
		"TotalDePublicaciones",
		"TotalDePublicacionesSinTexto",
		"TotalDePublicacionesConTexto",
		"PromedioDePublicacionesAlAno",
		"DesviacionEstandarDePublicacionesAlAno",
		"PromedioDeCaracteres",
		"DesviacionEstandarPromedioDeCaracteres",
		"PromedioDePalabras",
		"DesvicionEstandarPalabras",
		"PromedioEmojis",
		"DesvicionEstandarEmojis",
		"PromedioHashtag",
		"DesviacionEstandarHashtag",
		"PromedioLinks",
		"DesviacionEstandarLinks",
		"PromedioLinkImg",
		"DesviacionEstandarLinkImg",
		"PromedioLinkVideo",
		"DesviacionEstandarLinkVideo",
		"PromedioLinkAlbum",
		"DesvicionEstandarAlbum",
		"PromedioLinkOtros",
		"DesvicionEstandarLinkOtros", 
		"PromedioDeReacciones",
		"DesviacionEstandarDeReacciones",
		"PromedioDeReaccionesMeGusta",
		"DesviacionEstandarDeReaccionesMeGusta",
		"PromedioDeReaccionesMeAsombra", 
		"DesviacionEstandarDeReaccionesMeAsombra",
		"PromedioDeReaccionesMeDivierte", 
		"DesviacionEstandarDeReaccionesMeDivierte",
		"PromedioDeReaccionesMeEnoja",
		"DesviacionEstandarDeReaccionesMeEnoja",
		"PromedioDeReaccionesEncanta",
		"DesviacionEstandaDeReaccionesMeEncanta",
		"PromedioDeReaccionesMeEntristece",
		"DesviacionEstandarDeReaccionesMeEntristece",
		"ConAlMenosUnaReaccion",
		"SinReacciones",
		"Con6Reacciones",
		"ConSoloMeGusta",
		"PromedioDeVecesCompartidos",
		"DesviacionEstandarDeVecesCompartidos",
		"PromedioDeComentarios",
		"DesviacionEstandarDeComentarios",
		"ConComentariosYVecesCom", 
		"SoloComentarios",
		"SoloVecesCompartidos",
		"TotalDeReacciones",
		"TotalDeMeGusta",
		"TotalDeMeAsombra",
		"TotalDeMeDivierte",
		"TotalDeMeEnoja",
		"TotalDeMeEncanta",
		"TotalDeMeEntristece"]
	##Graficar las reacciones de la empresa]
		 
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for key in diccionario:
			writer.writerow({'id':key,
			'Empresa':diccionario[key]["Empresa"],
			'TotalDePublicaciones':diccionario[key]["TotalDePublicaciones"],
			'TotalDePublicacionesSinTexto':diccionario[key]["TotalDePublicacionesSinTexto"],
			'TotalDePublicacionesConTexto':diccionario[key]["TotalDePublicacionesConTexto"],
			'PromedioDePublicacionesAlAno':diccionario[key]["PromedioDePublicacionesAlAno"],
			'DesviacionEstandarDePublicacionesAlAno':diccionario[key]["DesviacionEstandarDePublicacionesAlAno"],
			'PromedioDeCaracteres':diccionario[key]["PromedioDeCaracteres"],
			'DesviacionEstandarPromedioDeCaracteres':diccionario[key]["DesviacionEstandarPromedioDeCaracteres"],
			'PromedioDePalabras':diccionario[key]["PromedioDePalabras"],
			'DesvicionEstandarPalabras':diccionario[key]["DesvicionEstandarPalabras"],
			'PromedioEmojis':diccionario[key]["PromedioEmojis"],
			'DesvicionEstandarEmojis':diccionario[key]["DesvicionEstandarEmojis"],
			'PromedioHashtag':diccionario[key]["PromedioHashtag"],
			'DesviacionEstandarHashtag':diccionario[key]["DesviacionEstandarHashtag"],
			'PromedioLinks':diccionario[key]["PromedioLinks"],
			'DesviacionEstandarLinks':diccionario[key]["DesviacionEstandarLinks"],
			'PromedioLinkImg':diccionario[key]["PromedioLinkImg"],
			'DesviacionEstandarLinkImg':diccionario[key]["DesviacionEstandarLinkImg"],
			'PromedioLinkVideo':diccionario[key]["PromedioLinkVideo"],
			'DesviacionEstandarLinkVideo':diccionario[key]["DesviacionEstandarLinkVideo"],
			'PromedioLinkAlbum':diccionario[key]["PromedioLinkAlbum"],
			'DesvicionEstandarAlbum':diccionario[key]["DesvicionEstandarAlbum"],
			'PromedioLinkOtros':diccionario[key]["PromedioLinkOtros"],
			'DesvicionEstandarLinkOtros':diccionario[key]["DesvicionEstandarLinkOtros"],
			'PromedioDeReacciones':diccionario[key]["PromedioDeReacciones"],
			'DesviacionEstandarDeReacciones':diccionario[key]["DesviacionEstandarDeReacciones"],
			'PromedioDeReaccionesMeGusta':diccionario[key]["PromedioDeReaccionesMeGusta"],
			'DesviacionEstandarDeReaccionesMeGusta':diccionario[key]["DesviacionEstandarDeReaccionesMeGusta"],
			'PromedioDeReaccionesMeAsombra':diccionario[key]["PromedioDeReaccionesMeAsombra"], 
			'DesviacionEstandarDeReaccionesMeAsombra':diccionario[key]["DesviacionEstandarDeReaccionesMeAsombra"],
			'PromedioDeReaccionesMeDivierte':diccionario[key]["PromedioDeReaccionesMeDivierte"],
			'DesviacionEstandarDeReaccionesMeDivierte':diccionario[key]["DesviacionEstandarDeReaccionesMeDivierte"],
			'PromedioDeReaccionesMeEnoja':diccionario[key]["PromedioDeReaccionesMeEnoja"],
			'DesviacionEstandarDeReaccionesMeEnoja':diccionario[key]["DesviacionEstandarDeReaccionesMeEnoja"],
			'PromedioDeReaccionesEncanta':diccionario[key]["PromedioDeReaccionesEncanta"],
			'DesviacionEstandaDeReaccionesMeEncanta':diccionario[key]["DesviacionEstandaDeReaccionesMeEncanta"],
			'PromedioDeReaccionesMeEntristece':diccionario[key]["PromedioDeReaccionesMeEntristece"],
			'DesviacionEstandarDeReaccionesMeEntristece':diccionario[key]["DesviacionEstandarDeReaccionesMeEntristece"],
			'ConAlMenosUnaReaccion':diccionario[key]["ConAlMenosUnaReaccion"],
			'SinReacciones':diccionario[key]["SinReacciones"],
			'Con6Reacciones':diccionario[key]["Con6Reacciones"],
			'ConSoloMeGusta':diccionario[key]["ConSoloMeGusta"],
			'PromedioDeVecesCompartidos':diccionario[key]["PromedioDeVecesCompartidos"],
			'DesviacionEstandarDeVecesCompartidos':diccionario[key]["DesviacionEstandarDeVecesCompartidos"],
			'PromedioDeComentarios':diccionario[key]["PromedioDeComentarios"],
			'DesviacionEstandarDeComentarios':diccionario[key]["DesviacionEstandarDeComentarios"],
			'ConComentariosYVecesCom':diccionario[key]["ConComentariosYVecesCom"],
			'SoloComentarios':diccionario[key]["SoloComentarios"],
			'SoloVecesCompartidos':diccionario[key]["SoloVecesCompartidos"],
			"TotalDeReacciones":diccionario[key]["TotalDeReacciones"],
			"TotalDeMeGusta":diccionario[key]["TotalDeMeGusta"],
			"TotalDeMeAsombra":diccionario[key]["TotalDeMeAsombra"],
			"TotalDeMeDivierte":diccionario[key]["TotalDeMeDivierte"],
			"TotalDeMeEnoja":diccionario[key]["TotalDeMeEnoja"],
			"TotalDeMeEncanta":diccionario[key]["TotalDeMeEncanta"],
			"TotalDeMeEntristece":diccionario[key]["TotalDeMeEntristece"]})
			
#---------------------------Obtener el numero total de publicaciones sin texto  ---------#
def numeroDePublicacionesSinTextoLista(datos):
	if(len(datos)>0):
		NumeroDePublicacionesSinTexto.append(datos['nombre'][0])#Agregar Nombre
		NumeroDePublicacionesSinTexto.append(len(datos)) #Agregar Total de publicaciones
		return len(datos)
	else:
		return 0

#----------------------Main--------------------------------------------------------#
	##Declaracion  de varaibles 
listaParaTotaldePublicaciones=[]
listaParaPromedioDePublicacionesAlano=[]
listaParaTotaldeCaracteres=[]
listaParaTotaldePalabras=[]
listaParaTotalDeEmojis=[]
listaParaTotalDeHashtag=[]
listaParaTotalDeLink=[]
listaParaTotalDeLinkImages=[]
listaParaTotalDeLinkVideos=[]
listaParaTotalDeLinkAlb=[]
listaParaTotalDeLinkOtro=[]
listaParaTotalDeReacciones=[]
listaParaTotalDeReaccionesMeGusta=[]
listaParaTotalDeReaccionesMe_asombra=[]
listaParaTotalDeReaccionesMe_divierte=[]
listaParaTotalDeReaccionesMe_enoja=[]
listaParaTotalDeReaccionesMe_encanta=[]
listaParaTotalDeReaccionesMe_entristece=[]
listaParaTotalDeVeces_compartido=[]
listaParaTotalDeComentarios=[]
listaParaGuardarNumeroDeReacciones=[]
listaTotalDePublicaciones=[]

totalParaGuadarNumeroDePublicacionesCon6Reacciones=[]
totalParaGuardarNumeroDePublicacionesConAlMenosUnaReaccion=[]
totalParaGuardarNumeroDePublicacionesSinReacciones=[]
totalParaGuardarNumeroDePublicacionesConSoloMeGusta=[]
totalParaGuardarNumeroDePublicacionesConCyV=[]
totalParaGuardarNumeroDePublicacionesConSoloComentarios=[]
totalParaGuardarNumeroDePublicacionesConSoloCompartidos=[]

totalDeMeGustaDeTodasLasEmpresas=0
totalDeMe_asombraDeTodasLasEmpresas=0
totalDeMe_divierteDeTodasLasEmpresas=0
totalDeMe_enojaDeTodasLasEmpresas=0
totalDeMe_encantaDeTodasLasEmpresas=0
totalDeMe_entristeceDeTodasLasEmpresas=0
totalDeComentarios=0
totalDeVecesCompartidos=0
totalDeReaccionesDeLaEmpresa=0
DiccionarioDeEstadisticas=dict()
listaAnos=[]
listaCaracteres=[]
listaPalabras=[]
listaEmojis=[]
listaHashtag=[]
listaLink=[]
listaLinkImg=[]
listaLinkVideos=[]
listaLinklinkAlb=[]
listaLinkOtro=[]
listaTotalDeReacciones=[]
listaVeces_compartido=[]
listaComentarios=[]
listaDeDatosSinTexto=[]
NumeroDePublicacionesSinTexto=[] #lista para graficar
numeroDeSinTexto=0 #dir
numeroDePublicacionesConYSinTexto=0 #dir 
numeroTotalSinTexto=0 #total de todas las publicaciones sin texto
totalDeTotalesDePublicaciones=0
publicacionesTotales=0
#veces_compartido,Comentarios
##Obtener numero de publicaciones sin texto 
##Recorrer las empresas que no contienen texto
##Leer los csv de las empresas que no contienen texto

listaDeDatosSinTexto=['Alejandra Barrales_SinTexto.csv','Alfredo Del Mazo Maza_SinTexto.csv','Andrés Manuel López Obrador_SinTexto.csv',
'Claudia Sheinbaum_SinTexto.csv','Delfina Gómez Álvarez_SinTexto.csv','Enrique Pena Nieto_SinTexto.csv',
                     'Gerardo Fernández Noroña_SinTexto.csv','Jaime Rodriguez Calderon_SinTexto.csv',
                     'José Antonio Meade_SinTexto.csv','Manuel Velasco Coello_SinTexto.csv',
                      'Mariana Boy_SinTexto.csv','Martha Erika Alonso_SinTexto.csv','Rafael Moreno Valle_SinTexto.csv',
                      'Ricardo Anaya Cortés_SinTexto.csv','Clash Royale ES_SinTexto.csv','Canon Mexicana_SinTexto.csv','Muy Interesante Mexico_SinTexto.csv','Cinépolis_SinTexto.csv',
                      'Discovery Channel España_SinTexto.csv','National Geographic_SinTexto.csv','Fisher-Price_SinTexto.csv',
                      'Xbox México_SinTexto.csv','Nikon_SinTexto.csv','Lacoste_SinTexto.csv'
                     ]
listaDeDatos=['Alejandra Barrales.csv','Alfredo Del Mazo Maza.csv','Andrés Manuel López Obrador.csv',
             'Claudia Sheinbaum.csv','Delfina Gómez Álvarez.csv','Enrique Pena Nieto.csv','Gerardo Fernández Noroña.csv',
             'Jaime Rodriguez Calderon.csv','José Antonio Meade.csv','Manuel Velasco Coello.csv',
              'Mariana Boy.csv','Martha Erika Alonso.csv','Rafael Moreno Valle.csv',
              'Ricardo Anaya Cortés.csv','Clash Royale ES.csv','Canon Mexicana.csv','Muy Interesante Mexico.csv','Cinépolis.csv',
              'Discovery Channel España.csv','National Geographic.csv','Fisher-Price.csv',
              'Xbox México.csv','Nikon.csv','Lacoste.csv'
             ]

i=0
	##Obtener estadisticas por cada empresa
while (len(listaDeDatos)>i):
	
	##Leer csv
	datos=leerCSV(listaDeDatos[i])
	datos1=leerCSV(listaDeDatosSinTexto[i])
	##Obtener publicaciones sin texto 
	numeroDeSinTexto=0
	numeroDeSinTexto=numeroDePublicacionesSinTextoLista(datos1)
	numeroTotalSinTexto=numeroTotalSinTexto+numeroDeSinTexto
##obtener total de publicaciones con texto 
	publicacionesTotales=publicacionesTotales+numeroDePublicacionesTotales(datos)
	##Obtener publicaciones totales (con y sin texto )
	numeroDePublicacionesConYSinTexto=0
	numeroDePublicacionesConYSinTexto=numeroDeSinTexto+len(datos)
	totalDeTotalesDePublicaciones=totalDeTotalesDePublicaciones+numeroDePublicacionesConYSinTexto #gene
	##<fechaPublicacion>
	##Obtener el promedio de publicaciones por año 
	listaAnos=[]
	listaAnos=numeroPromedioDePublicacionesPorAno(datos)
	##<Texto>
	##Obtener numero promedio de caracteres por texto 
	listaCaracteres=[]
	listaCaracteres=numeroPromedioDeCaracteresPorTexto(datos)
	listaParaTotaldeCaracteres=listaParaTotaldeCaracteres+listaCaracteres
	#graficarPromedio(listaCaracteres,"Caracteres por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	#print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    ##Obtener numero promedio de palabras por texto 
	listaPalabras=[]
	listaPalabras=numeroPromedioDePalabrasPorTexto(datos)
	listaParaTotaldePalabras=listaParaTotaldePalabras+listaPalabras
	
	#graficarPromedio(listaPalabras,"Palabras por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones",max(listaPalabras))
	
	##Obtener numero promedio de emojis
	listaEmojis=[]
	listaEmojis=numeroPromedioDeEmojisPorTexto(datos)
	listaParaTotalDeEmojis=listaParaTotalDeEmojis+listaEmojis
	#graficarPromedio(listaEmojis,"Emojis por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##Obtener numero promedio de hashtag
	listaHashtag=[]
	listaHashtag=numeroPromedioDeHashtagPorTexto(datos)
	listaParaTotalDeHashtag=listaParaTotalDeHashtag+listaHashtag
	#graficarPromedio(listaHashtag,"Hashtag por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	    
	##<Link>
	##Obtener numero promedio de links
	listaLink=[]
	listaLink=numeroPromedioDeLinkPorTexto(datos)
	listaParaTotalDeLink=listaParaTotalDeLink+listaLink
	#graficarPromedio(listaLink,"Links por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##Obtener numero promedio de link a imagenes 
	listaLinkImg=[]
	listaLinkImg=numeroPromedioDeLinkImages(datos)
	listaParaTotalDeLinkImages=listaParaTotalDeLinkImages+listaLinkImg
	#graficarPromedio(listaLinkImg,"Links a imagenes por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	##Obtener numero promedio de link a videos
	listaLinkVideos=[]
	listaLinkVideos=numeroPromedioDeLinkVideos(datos)
	listaParaTotalDeLinkVideos=listaParaTotalDeLinkVideos+listaLinkVideos
	#graficarPromedio(listaLinkVideos,"Links a videos por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Obtener  numero promedio de link a album
	listaLinklinkAlb=[]
	listaLinklinkAlb=numeroPromedioDeLinkAlb(datos)
	listaParaTotalDeLinkAlb=listaParaTotalDeLinkAlb+listaLinklinkAlb
	#graficarPromedio(listaLinklinkAlb,"Links a albums por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Obtener numero promedio de link a otros 
	listaLinkOtro=[]
	listaLinkOtro=numeroPromedioDeLinkOtros(datos)
	listaParaTotalDeLinkOtro=listaParaTotalDeLinkOtro+listaLinkOtro
	#graficarPromedio(listaLinkOtro,"Links a otros por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##<Reacciones>
	#Numero promedio de todas las reacciones
	listaTotalDeReacciones=[]
	listaTotalDeReacciones=numeroPromedioDeReaccionesPorPublicacion(datos)
	listaParaTotalDeReacciones=listaParaTotalDeReacciones+listaTotalDeReacciones
	#graficarPromedio(listaTotalDeReacciones,"Reacciones por publicacion de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones me gusta 
	listaTotalDeReaccionesMeGusta=[]
	listaTotalDeReaccionesMeGusta=numeroPromedioDeReaccionesMeGustaPorPublicacion(datos)
	listaParaTotalDeReaccionesMeGusta=listaParaTotalDeReaccionesMeGusta+listaTotalDeReaccionesMeGusta
	#graficarPromedio(listaTotalDeReaccionesMeGusta,"Reacciones ME gusta de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones me asombra
	listaTotalDeReaccionesMe_asombra=[]
	listaTotalDeReaccionesMe_asombra=numeroPromedioDeReaccionesMeAsombraPorPublicacion(datos)
	listaParaTotalDeReaccionesMe_asombra=listaParaTotalDeReaccionesMe_asombra+listaTotalDeReaccionesMe_asombra
	#graficarPromedio(listaTotalDeReaccionesMe_asombra,"Reacciones ME asombra de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones me divierte
	listaTotalDeReaccionesMe_divierte=[]
	listaTotalDeReaccionesMe_divierte=numeroPromedioDeReaccionesMeDiviertePorPublicacion(datos)
	listaParaTotalDeReaccionesMe_divierte=listaParaTotalDeReaccionesMe_divierte+listaTotalDeReaccionesMe_divierte
	#graficarPromedio(listaTotalDeReaccionesMe_divierte,"Reacciones ME divierte de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones  me enoja
	listaTotalDeReaccionesMe_enoja=[]
	listaTotalDeReaccionesMe_enoja=numeroPromedioDeReaccionesMeEnojaPorPublicacion(datos)
	listaParaTotalDeReaccionesMe_enoja=listaParaTotalDeReaccionesMe_enoja+listaTotalDeReaccionesMe_enoja
	#graficarPromedio(listaTotalDeReaccionesMe_enoja,"Reacciones ME enoja de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones me encanta 
	listaTotalDeReaccionesMe_encanta=[]
	listaTotalDeReaccionesMe_encanta=numeroPromedioDeReaccionesMeEncantaPorPublicacion(datos)
	listaParaTotalDeReaccionesMe_encanta=listaParaTotalDeReaccionesMe_encanta+listaTotalDeReaccionesMe_encanta
	#graficarPromedio(listaTotalDeReaccionesMe_encanta,"Reacciones ME encanta de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	#Numero promedio de todas las reacciones me entristece
	listaTotalDeReaccionesMe_entristece=[]
	listaTotalDeReaccionesMe_entristece=numeroPromedioDeReaccionesMeEntristecePorPublicacion(datos)
	listaParaTotalDeReaccionesMe_entristece=listaParaTotalDeReaccionesMe_entristece+listaTotalDeReaccionesMe_entristece
	#graficarPromedio(listaTotalDeReaccionesMe_entristece,"Reacciones ME entristece de"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##Numero de publicaciones que al menos contienen alguna reaccion ya sea me gusta , me asombra, me divierte, me entristece, me asombra etc
	conReaccion=0
	conReaccion=numeroDePublicacionesQueContienenAlMenosReacciones(datos)
	totalParaGuardarNumeroDePublicacionesConAlMenosUnaReaccion.append(conReaccion)
	## Numero de publicaciones que contienen las 6 reacciones 
	seisReacciones=0
	seisReacciones=numeroDePublicacionesQueContienenLas6Reacciones(datos)
	totalParaGuadarNumeroDePublicacionesCon6Reacciones.append(seisReacciones)
	##Numero de reacciones que contienen solo las reaccion me gusta 
	soloMeGusta=0
	soloMeGusta=numeroDePublicacionesSoloTienenLaReaccionMeGusta(datos)
	totalParaGuardarNumeroDePublicacionesConSoloMeGusta.append(soloMeGusta)
	##Numero de publicaciones que no contienen reacciones
	sinReacciones=0
	sinReacciones=numeroDePublicacionesSinReacciones(datos)
	totalParaGuardarNumeroDePublicacionesSinReacciones.append(sinReacciones)
	
	##-<Comentarios >Y <VecesCompartidos>
	##Numero promedio de comentarios
	listaComentarios=[]
	listaComentarios=numeroPromedioDeReaccionesComentariosPorPublicacion(datos)
	listaParaTotalDeComentarios=listaParaTotalDeComentarios+listaComentarios
	#graficarPromedio(listaComentarios,"Frecuencia de Comentarios por publicaciòn"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##Numero promedio de veces compartidos
	listaVeces_compartido=[]
	listaVeces_compartido=numeroPromedioDeReaccionesVecesCompartidosPorPublicacion(datos)
	listaParaTotalDeVeces_compartido=listaParaTotalDeVeces_compartido+listaVeces_compartido
	#graficarPromedio(listaVeces_compartido,"Frecuencia de Veces Compartidos por publicaciòn"+" "+datos['nombre'][0],"Longitud","Publicaciones")
	
	##Numero  de publicaciones que contienen comentarios y veces compartidos
	conVyC=0
	conVyC=numeroDePublicacionesQueContienenComentariosYVecesCompartidos(datos)
	totalParaGuardarNumeroDePublicacionesConCyV.append(conVyC)

	##NUmero de publicaciones que contienen solo comentarios 
	conComen=0
	conComen=numeroDePublicacionesQueContienenSoloComentarios(datos)
	totalParaGuardarNumeroDePublicacionesConSoloComentarios.append(conComen)

	##Numero de publicaciones que coontienen solo veces compartidas
	conVeces=0
	conVeces=numeroDePublicacionesQueContienenSoloVeces(datos)
	totalParaGuardarNumeroDePublicacionesConSoloCompartidos.append(conVeces)
	##CrearDiccionarioParaGuardarEstadisticas
	id=i
	##Guardar valores en diccionario
	DiccionarioDeEstadisticas[id]={"Empresa":datos['nombre'][0],
	"TotalDePublicaciones":numeroDePublicacionesConYSinTexto,
	"TotalDePublicacionesSinTexto":numeroDeSinTexto,
	"TotalDePublicacionesConTexto":len(datos),
	"PromedioDePublicacionesAlAno":mean(listaAnos),"DesviacionEstandarDePublicacionesAlAno":pstdev(listaAnos),"PromedioDeCaracteres":mean(listaCaracteres),"DesviacionEstandarPromedioDeCaracteres":pstdev(listaCaracteres),"PromedioDePalabras":mean(listaPalabras),"DesvicionEstandarPalabras":pstdev(listaPalabras),"PromedioEmojis":mean(listaEmojis),"DesvicionEstandarEmojis":pstdev(listaEmojis),"PromedioHashtag":mean(listaHashtag),"DesviacionEstandarHashtag":pstdev(listaHashtag),"PromedioLinks":mean(listaLink),"DesviacionEstandarLinks":pstdev(listaLink),"PromedioLinkImg":mean(listaLinkImg),"DesviacionEstandarLinkImg":pstdev(listaLinkImg),"PromedioLinkVideo":mean(listaLinkVideos),"DesviacionEstandarLinkVideo":pstdev(listaLinkVideos),"PromedioLinkAlbum":mean(listaLinklinkAlb),"DesvicionEstandarAlbum":pstdev(listaLinklinkAlb),"PromedioLinkOtros":mean(listaLinkOtro),"DesvicionEstandarLinkOtros":pstdev(listaLinkOtro),"PromedioDeReacciones":mean(listaTotalDeReacciones),"DesviacionEstandarDeReacciones":pstdev(listaTotalDeReacciones),"PromedioDeReaccionesMeGusta":mean(listaTotalDeReaccionesMeGusta),"DesviacionEstandarDeReaccionesMeGusta":pstdev(listaTotalDeReaccionesMeGusta),"PromedioDeReaccionesMeAsombra":mean(listaTotalDeReaccionesMe_asombra), "DesviacionEstandarDeReaccionesMeAsombra":pstdev(listaTotalDeReaccionesMe_asombra),"PromedioDeReaccionesMeDivierte":mean(listaTotalDeReaccionesMe_divierte),"DesviacionEstandarDeReaccionesMeDivierte":pstdev(listaTotalDeReaccionesMe_divierte),"PromedioDeReaccionesMeEnoja":mean(listaTotalDeReaccionesMe_enoja),"DesviacionEstandarDeReaccionesMeEnoja":pstdev(listaTotalDeReaccionesMe_enoja),"PromedioDeReaccionesEncanta":mean(listaTotalDeReaccionesMe_encanta),"DesviacionEstandaDeReaccionesMeEncanta":pstdev(listaTotalDeReaccionesMe_encanta),"PromedioDeReaccionesMeEntristece":mean(listaTotalDeReaccionesMe_entristece),"DesviacionEstandarDeReaccionesMeEntristece":pstdev(listaTotalDeReaccionesMe_entristece),"ConAlMenosUnaReaccion":conReaccion,"SinReacciones":sinReacciones,"Con6Reacciones":seisReacciones,"ConSoloMeGusta":soloMeGusta,"PromedioDeVecesCompartidos":mean(listaVeces_compartido),"DesviacionEstandarDeVecesCompartidos":pstdev(listaVeces_compartido),"PromedioDeComentarios":mean(listaComentarios),"DesviacionEstandarDeComentarios":pstdev(listaComentarios),"ConComentariosYVecesCom":conVyC, "SoloComentarios":conComen, "SoloVecesCompartidos":conVeces,
	"TotalDeReacciones":totalDeReaccionesDeLaEmpresa,
	"TotalDeMeGusta":listaParaGuardarNumeroDeReacciones[1],
	"TotalDeMeAsombra":listaParaGuardarNumeroDeReacciones[3],
	"TotalDeMeDivierte":listaParaGuardarNumeroDeReacciones[5],
	"TotalDeMeEnoja":listaParaGuardarNumeroDeReacciones[7],
	"TotalDeMeEncanta":listaParaGuardarNumeroDeReacciones[9],
	"TotalDeMeEntristece":listaParaGuardarNumeroDeReacciones[11]}
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")##Graficar las reacciones de la empresa
	#graficarReacciones(listaParaGuardarNumeroDeReacciones,"Reacciones"+" "+datos['nombre'][0])
    
	#graficarVecesYComentarios(listaParaGuardarNumeroDeReacciones,"Comentarios y Veces Compartidos "+" "+datos['nombre'][0])
    
	totalDeReaccionesDeLaEmpresa=0
	listaParaGuardarNumeroDeReacciones=[]
	print("-------------------------------------------------------------")
	i=i+1
#Mostrar resultados de estaditicas
#####Estadisticas de todas las empresas 
## 1ª Graficar total de publicaciones
#graficoDeTotalDeEmpresas()
##Publicaciones totales 
print(publicacionesTotales)
## Promedio y desvicion estandar del total de publicaciones 
print("Promedio de publicaciones por empresa:" ,mean(listaTotalDePublicaciones))
print("Desviacion estandar:",pstdev(listaTotalDePublicaciones))

##Promedio de publicaciones al año
print("Promedio de publicaciones al año:", mean(listaParaPromedioDePublicacionesAlano))
print("Desviacion estandar:",pstdev(listaParaPromedioDePublicacionesAlano))
##Promedio de caracteres por publicacion 
print("Promedio de caracteres por publicacion:",mean(listaParaTotaldeCaracteres))
print("Desviacion estandar:",pstdev(listaParaTotaldeCaracteres))

#graficarPromedio(listaParaTotaldeCaracteres,"Caracteres por publicacion" ,"No.Caracteres","Publicaciones",1700)

##Promedio de palabras por publicacion 
print("Promedio de palabras por publicacion:",mean(listaParaTotaldePalabras))
print("Desviacion estandar:",pstdev(listaParaTotaldePalabras))
#graficarPromedio(listaParaTotaldePalabras,"Palabras por publicacion" ,"No.Palabras","Publicaciones",170)

#graficarPromedio(listaPalabras,"Caracteres por publicacion" ,"No.Caracteres","Publicaciones",250)
##Promedio de emojis por publicacion 
print("Promedio de emojis por publicacion :",mean(listaParaTotalDeEmojis))
print("Desviacion estandar:",pstdev(listaParaTotalDeEmojis))
##eliminar los valores 0 de la lista de links a video
m=0
while(m<len(listaParaTotalDeEmojis)):
    if(listaParaTotalDeEmojis[m]==0):
        #eliminar 
        listaParaTotalDeEmojis.pop(m)
    else:
        m=m+1
graficarPromedio(listaParaTotalDeEmojis,"Emojis por publicacion" ,"No.Emojis","Publicaciones")
##Promedio de hashtag por publicacion 
print("Promedio de hashtag por publicacion :",mean(listaParaTotalDeHashtag))
print("Desviacion estandar:",pstdev(listaParaTotalDeHashtag))
##eliminar los valores 0 de la lista de links a video
m=0
while(m<len(listaParaTotalDeHashtag)):
    if(listaParaTotalDeHashtag[m]==0):
        #eliminar 
        listaParaTotalDeHashtag.pop(m)
    else:
        m=m+1


graficarPromedio(listaParaTotalDeHashtag,"Hashtags por publicacion" ,"No.Hashtags","Publicaciones")    
##Promedio de link por publicacion 
print("Promedio de link por publicacion :",mean(listaParaTotalDeLink))
print("Desviacion estandar:",pstdev(listaParaTotalDeLink))
graficarPromedio(listaParaTotalDeLink,"Links por publicacion" ,"No.Links","Publicaciones") 
##Promedio de  link a imagenes 
print("Promedio de link a imagenes  por publicacion :",mean(listaParaTotalDeLinkImages))
print("Desviacion estandar:",pstdev(listaParaTotalDeLinkImages))
m=0
while(m<len(listaParaTotalDeLinkImages)):
    if(listaParaTotalDeLinkImages[m]==0):
        #eliminar 
        listaParaTotalDeLinkImages.pop(m)
    else:
        m=m+1
graficarPromedio(listaParaTotalDeLinkImages,"Imagenes por publicaciòn","No.Imagenes","Publicaciones")
##Promedio de link a video 
print("Promedio de link a video  por publicacion :",mean(listaParaTotalDeLinkVideos))
print("Desviacion estandar:",pstdev(listaParaTotalDeLinkVideos))
m=0
while(m<len(listaParaTotalDeLinkVideos)):
    if(listaParaTotalDeLinkVideos[m]==0):
        #eliminar 
        listaParaTotalDeLinkVideos.pop(m)
    else:
        m=m+1
#print(listaParaTotalDeLinkVideos)
graficarPromedio(listaParaTotalDeLinkVideos,"Videos por publicaciòn","No.Videos","Publicaciones")
##Promedio de link a album
print("Promedio de link a album  por publicacion :",mean(listaParaTotalDeLinkAlb))
print("Desviacion estandar:",pstdev(listaParaTotalDeLinkAlb))
m=0
while(m<len(listaParaTotalDeLinkAlb)):
    if(listaParaTotalDeLinkAlb[m]==0):
        #eliminar 
        listaParaTotalDeLinkAlb.pop(m)
    else:
        m=m+1
graficarPromedio(listaParaTotalDeLinkAlb,"Album por publicaciòn","No.Album","Publicaciones")
##Promedio de link a otros
print("Promedio de link a otros  por publicacion :",mean(listaParaTotalDeLinkOtro))
print("Desviacion estandar:",pstdev(listaParaTotalDeLinkOtro))
m=0
while(m<len(listaParaTotalDeLinkOtro)):
    if(listaParaTotalDeLinkOtro[m]==0):
        #eliminar 
        listaParaTotalDeLinkOtro.pop(m)
    else:
        m=m+1
graficarPromedio(listaParaTotalDeLinkOtro,"Links a otros por publicaciòn","No.Links a otro","Publicaciones")
##Promedio de las reacciones que tienen una empresa por publicacion 
print("Promedio de las reacciones que tienen una empresa por publicacion :",mean(listaParaTotalDeReacciones))
print("Desviacion estandar:",pstdev(listaParaTotalDeReacciones))
##Total de reacciones de todas las empresas 
totalDeReaccionesDeTodasLasEmpresas=0
d=0

##total de reacciones 
while (len(listaParaTotalDeReacciones)>d):
	totalDeReaccionesDeTodasLasEmpresas=totalDeReaccionesDeTodasLasEmpresas+listaParaTotalDeReacciones[d]
	d=d+1
	
print("Total de reacciones de todas las empresas:",totalDeReaccionesDeTodasLasEmpresas)
#graficarPromedio(listaParaTotalDeReacciones,"Reacciones por publicacion","reacciones","Publicaciones")
##Promedio de me gusta por publicacion 
print("Promedio de las reacciones  me gusta por publicacion :",mean(listaParaTotalDeReaccionesMeGusta))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMeGusta))
##Total de me gusta
listaReaccionesDeEmpresas=[]
print("Total de reacciones me gusta",totalDeMeGustaDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_gusta")
listaReaccionesDeEmpresas.append(totalDeMeGustaDeTodasLasEmpresas)


##Promedio de me asombra por publicacion 
print("Promedio de las reacciones  me asombra por publicacion :",mean(listaParaTotalDeReaccionesMe_asombra))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMe_asombra))


##Total de me asombra
print("Total de reacciones me asombra",totalDeMe_asombraDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_asombra")
listaReaccionesDeEmpresas.append(totalDeMe_asombraDeTodasLasEmpresas)

##Promedio de me diviete por publicacion 
print("Promedio de las reacciones  me divierte por publicacion :",mean(listaParaTotalDeReaccionesMe_divierte))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMe_divierte))
#graficarPromedio(listaParaTotalDeReaccionesMe_divierte,"Promedio de reacciones me divierte por publicacion","reaccion","Publicaciones")
##Total de me divierte
print("Total de reacciones me divierte",totalDeMe_divierteDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_divierte")
listaReaccionesDeEmpresas.append(totalDeMe_divierteDeTodasLasEmpresas)

##Promedio de me enoja por publicacion 
print("Promedio de las reacciones  me enoja por publicacion :",mean(listaParaTotalDeReaccionesMe_enoja))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMe_enoja))
##Total de me enoja
print("Total de reacciones me enoja",totalDeMe_enojaDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_enoja")
listaReaccionesDeEmpresas.append(totalDeMe_enojaDeTodasLasEmpresas)

##Promedio de me encanta por publicacion 
print("Promedio de las reacciones  me encanta por publicacion :",mean(listaParaTotalDeReaccionesMe_encanta))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMe_encanta))
##Total de me encanta
print("Total de reacciones me enoja",totalDeMe_encantaDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_encanta")
listaReaccionesDeEmpresas.append(totalDeMe_encantaDeTodasLasEmpresas)

##Promedio de me entriste por publicacion 
print("Promedio de las reacciones  me entristece por publicacion :",mean(listaParaTotalDeReaccionesMe_entristece))
print("Desviacion estandar:",pstdev(listaParaTotalDeReaccionesMe_entristece))
##Total de me entristece
print("Total de reacciones me entistece",totalDeMe_entristeceDeTodasLasEmpresas)
listaReaccionesDeEmpresas.append("Me_entristece")
listaReaccionesDeEmpresas.append(totalDeMe_entristeceDeTodasLasEmpresas)

##Graficar reacciones de empresas
print(listaReaccionesDeEmpresas)
graficarReacciones(listaReaccionesDeEmpresas,"Reacciones")

##Total de publicaciones al menos una reacciones 
d=0
totalDePublicacionConAlMenosUnaRea=0
while(len(totalParaGuardarNumeroDePublicacionesConAlMenosUnaReaccion)>d):
	totalDePublicacionConAlMenosUnaRea=totalDePublicacionConAlMenosUnaRea+totalParaGuardarNumeroDePublicacionesConAlMenosUnaReaccion[d]
	d=d+1
print("Total de publicaciones que contienen al menos una reaccion:",totalDePublicacionConAlMenosUnaRea)
## Total de publicaciones con las 6 reacciones
d=0
totalDePublicacionCon6Rea=0
while(len(totalParaGuadarNumeroDePublicacionesCon6Reacciones)>d):
	totalDePublicacionCon6Rea=totalDePublicacionCon6Rea+totalParaGuadarNumeroDePublicacionesCon6Reacciones[d]
	d=d+1
print("Total de publicaciones que contienen las 6 reacciones:",totalDePublicacionCon6Rea)

## Total de publicaciones con  solo la reaccion me gusta 
d=0
totalDePublicacionConMeGusta=0
while(len(totalParaGuardarNumeroDePublicacionesConSoloMeGusta)>d):
	totalDePublicacionConMeGusta=totalDePublicacionConMeGusta+totalParaGuardarNumeroDePublicacionesConSoloMeGusta[d]
	d=d+1
print("Total de publicaciones con solo me gusta:",totalDePublicacionConMeGusta)

## Total de publicaciones  sin reacciones 

d=0
totalDePublicacionSinRea=0
while(len(totalParaGuardarNumeroDePublicacionesSinReacciones)>d):
	totalDePublicacionSinRea=totalDePublicacionSinRea+totalParaGuardarNumeroDePublicacionesSinReacciones[d]
	d=d+1
print("Total de publicaciones que no contienen reacciones:",totalDePublicacionSinRea)

##<Comentarios y compartidos>

##Promedio de comentario por publicacion 
print("Promedio de las comentario por publicacion :",mean(listaParaTotalDeComentarios))
print("Desviacion estandar:",pstdev(listaParaTotalDeComentarios))
##Total de comentarios
print("Total de reacciones me comentarios",totalDeComentarios)
listaReaccionesDeEmpresas.append("Comentarios")
listaReaccionesDeEmpresas.append(totalDeComentarios)

##Promedio de vecesCompartidos por publicacion 
print("Promedio de las compartidos por publicacion :",mean(listaParaTotalDeVeces_compartido))
print("Desviacion estandar:",pstdev(listaParaTotalDeVeces_compartido))
##Total de comentarios
print("Total de reacciones me compartidos",totalDeVecesCompartidos)
listaReaccionesDeEmpresas.append("Veces Comparidos")
listaReaccionesDeEmpresas.append(totalDeVecesCompartidos)

##Graficar veces compartidos y comentarios
#graficarVecesYComentarios(listaReaccionesDeEmpresas)

##Obtener total de comentarios y veces compartidos
d=0
totalDeComentariosYv=0
while(len(totalParaGuardarNumeroDePublicacionesConCyV)>d):
	totalDeComentariosYv=totalDeComentariosYv+totalParaGuardarNumeroDePublicacionesConCyV[d]
	d=d+1
print("Total de publicaciones con comentarios y veces compartidos:",totalDeComentariosYv)

##Obtener total de comentarios 
d=0
totalDeComentariosF=0
while(len(totalParaGuardarNumeroDePublicacionesConSoloComentarios)>d):
	totalDeComentariosF=totalDeComentariosF+totalParaGuardarNumeroDePublicacionesConSoloComentarios[d]
	d=d+1
print("Total de publicaciones con solo comentarios :",totalDeComentariosF)

##Obtener total de veces compartidos 
d=0
totalDeVecesCompartidosF=0
while(len(totalParaGuardarNumeroDePublicacionesConSoloCompartidos)>d):
	totalDeVecesCompartidosF=totalDeVecesCompartidosF+totalParaGuardarNumeroDePublicacionesConSoloCompartidos[d]
	d=d+1
print("Total de publicaciones con solo comentarios :",totalDeVecesCompartidosF)


##Crear csv de estadisticas de empresas
#print(totalDeMeGustaDeTodasLasEmpresas,"\n",totalDeMe_asombraDeTodasLasEmpresas,"\n",totalDeMe_divierteDeTodasLasEmpresas,"\n",totalDeMe_enojaDeTodasLasEmpresas,"\n",totalDeMe_encantaDeTodasLasEmpresas,"\n",totalDeMe_entristeceDeTodasLasEmpresas)
crearCSVdeEstadisticas(DiccionarioDeEstadisticas,'Estadisticas')



##Crear csv de estadisticas de todas las empresas

with open("PublicacionesDeTodasLasEmpresas"+'.csv', 'a', newline='') as csvfile:
	fieldnames=["TotalDePublicaciones",
	"TotalDePublicacionesSinTexto",
	"TotalDePublicacionesConTexto",
	"PromedioDePublicacionesPorEmpresa",
	"DesviacioEstandarDePublicacionesPorEmpresa",
	"PromedioDePublicacionesAlAno",
	"DesviacionEstandarDePublicacionesAlAno",
	"PromedioDeCaracteres",
	"DesviacionEstandarPromedioDeCaracteres",
	"PromedioDePalabras",
	"DesvicionEstandarPalabras",
	"PromedioEmojis",
	"DesvicionEstandarEmojis",
	"PromedioHashtag",
	"DesviacionEstandarHashtag",
	"PromedioLinks",
	"DesviacionEstandarLinks",
	"PromedioLinkImg",
	"DesviacionEstandarLinkImg",
	"PromedioLinkVideo",
	"DesviacionEstandarLinkVideo",
	"PromedioLinkAlbum",
	"DesvicionEstandarAlbum",
	"PromedioLinkOtros",
	"DesvicionEstandarLinkOtros", 
	"PromedioDeReacciones",
	"DesviacionEstandarDeReacciones",
	"PromedioDeReaccionesMeGusta",
	"DesviacionEstandarDeReaccionesMeGusta",
	"PromedioDeReaccionesMeAsombra", 
	"DesviacionEstandarDeReaccionesMeAsombra",
	"PromedioDeReaccionesMeDivierte", 
	"DesviacionEstandarDeReaccionesMeDivierte",
	"PromedioDeReaccionesMeEnoja",
	"DesviacionEstandarDeReaccionesMeEnoja",
	"PromedioDeReaccionesEncanta",
	"DesviacionEstandaDeReaccionesMeEncanta",
	"PromedioDeReaccionesMeEntristece",
	"DesviacionEstandarDeReaccionesMeEntristece",
	"ConAlMenosUnaReaccion",
	"SinReacciones",
	"Con6Reacciones",
	"ConSoloMeGusta",
	"PromedioDeVecesCompartidos",
	"DesviacionEstandarDeVecesCompartidos",
	"PromedioDeComentarios",
	"DesviacionEstandarDeComentarios",
	"ConComentariosYVecesCom", 
	"SoloComentarios",
	"SoloVecesCompartidos",
	"TotalDeReacciones",
	"TotalDeMeGusta",
	"TotalDeMeAsombra",
	"TotalDeMeDivierte",
	"TotalDeMeEnoja",
	"TotalDeMeEncanta",
	"TotalDeMeEntristece"]
	##Graficar las reacciones de la empresa]
		 
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({"TotalDePublicaciones":totalDeTotalesDePublicaciones,
			"TotalDePublicacionesSinTexto":numeroTotalSinTexto,
			'TotalDePublicacionesConTexto':publicacionesTotales,
			'PromedioDePublicacionesPorEmpresa':mean(listaTotalDePublicaciones),
			'DesviacioEstandarDePublicacionesPorEmpresa':pstdev(listaTotalDePublicaciones),
			'PromedioDePublicacionesAlAno':mean(listaParaPromedioDePublicacionesAlano),
			'DesviacionEstandarDePublicacionesAlAno':pstdev(listaParaPromedioDePublicacionesAlano),
			'PromedioDeCaracteres':mean(listaParaTotaldeCaracteres),
			'DesviacionEstandarPromedioDeCaracteres':pstdev(listaParaTotaldeCaracteres),
			'PromedioDePalabras':mean(listaParaTotaldePalabras),
			'DesvicionEstandarPalabras':pstdev(listaParaTotaldePalabras),
			'PromedioEmojis':mean(listaParaTotalDeEmojis),
			'DesvicionEstandarEmojis':pstdev(listaParaTotalDeEmojis),
			'PromedioHashtag':mean(listaParaTotalDeHashtag),
			'DesviacionEstandarHashtag':pstdev(listaParaTotalDeHashtag),
			'PromedioLinks':mean(listaParaTotalDeLink),
			'DesviacionEstandarLinks':pstdev(listaParaTotalDeLink),
			'PromedioLinkImg':mean(listaParaTotalDeLinkImages),
			'DesviacionEstandarLinkImg':pstdev(listaParaTotalDeLinkImages),
			'PromedioLinkVideo':mean(listaParaTotalDeLinkVideos),
			'DesviacionEstandarLinkVideo':pstdev(listaParaTotalDeLinkVideos),
			'PromedioLinkAlbum':mean(listaParaTotalDeLinkAlb),
			'DesvicionEstandarAlbum':pstdev(listaParaTotalDeLinkAlb),
			'PromedioLinkOtros':mean(listaParaTotalDeLinkOtro),
			'DesvicionEstandarLinkOtros':pstdev(listaParaTotalDeLinkOtro),
			'PromedioDeReacciones':mean(listaParaTotalDeReacciones),
			'DesviacionEstandarDeReacciones':pstdev(listaParaTotalDeReacciones),
			'PromedioDeReaccionesMeGusta':mean(listaParaTotalDeReaccionesMeGusta),
			'DesviacionEstandarDeReaccionesMeGusta':pstdev(listaParaTotalDeReaccionesMeGusta),
			'PromedioDeReaccionesMeAsombra':mean(listaParaTotalDeReaccionesMe_asombra), 
			'DesviacionEstandarDeReaccionesMeAsombra':pstdev(listaParaTotalDeReaccionesMe_asombra),
			'PromedioDeReaccionesMeDivierte':mean(listaParaTotalDeReaccionesMe_divierte),
			'DesviacionEstandarDeReaccionesMeDivierte':pstdev(listaParaTotalDeReaccionesMe_divierte),
			'PromedioDeReaccionesMeEnoja':mean(listaParaTotalDeReaccionesMe_enoja),
			'DesviacionEstandarDeReaccionesMeEnoja':pstdev(listaParaTotalDeReaccionesMe_enoja),
			'PromedioDeReaccionesEncanta':mean(listaParaTotalDeReaccionesMe_encanta),
			'DesviacionEstandaDeReaccionesMeEncanta':pstdev(listaParaTotalDeReaccionesMe_encanta),
			'PromedioDeReaccionesMeEntristece':mean(listaParaTotalDeReaccionesMe_entristece),
			'DesviacionEstandarDeReaccionesMeEntristece':pstdev(listaParaTotalDeReaccionesMe_entristece),
			'ConAlMenosUnaReaccion':totalDePublicacionConAlMenosUnaRea,
			'SinReacciones':totalDePublicacionSinRea,
			'Con6Reacciones':totalDePublicacionCon6Rea,
			'ConSoloMeGusta':totalDePublicacionConMeGusta,
			'PromedioDeVecesCompartidos':mean(listaParaTotalDeVeces_compartido),
			'DesviacionEstandarDeVecesCompartidos':pstdev(listaParaTotalDeVeces_compartido),
			'PromedioDeComentarios':mean(listaParaTotalDeComentarios),
			'DesviacionEstandarDeComentarios':pstdev(listaParaTotalDeComentarios),
			'ConComentariosYVecesCom':totalDeComentariosYv,
			'SoloComentarios':totalDeComentariosF,
			'SoloVecesCompartidos':totalDeVecesCompartidosF,
			'TotalDeReacciones':totalDeReaccionesDeTodasLasEmpresas,
			'TotalDeMeGusta':listaReaccionesDeEmpresas[1],
			'TotalDeMeAsombra':listaReaccionesDeEmpresas[3],
			'TotalDeMeDivierte':listaReaccionesDeEmpresas[5],
			'TotalDeMeEnoja':listaReaccionesDeEmpresas[7],
			'TotalDeMeEncanta':listaReaccionesDeEmpresas[9],
			'TotalDeMeEntristece':listaReaccionesDeEmpresas[11]})

