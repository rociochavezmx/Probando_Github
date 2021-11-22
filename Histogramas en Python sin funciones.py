#Indicamos el directorio en el que vamos a trabajar
import os
os.chdir('C:/Users/rocio/Escritorio2/Pavillion-Rocio/Cursos impartidos Presenciales/Programacion I MCD/Bases de Datos a Analizar/')

#Importamos los paquetes que vamos a necesitar 
import pandas as pd #Contiene funciones que nos ayudan en el análisis de datos
import matplotlib.pyplot as plt #Nota: Fue necesario instalar matplotlib 3.4.3 con conda install matplotlib=3.4.3
                                #y comentar la linea 4 del archivo _classic_test_patch.mplstyle

#Leemos el archivo a analizar
atletas = pd.read_csv('categorias de corredores.csv', index_col=0) #Con index_col=0 le indicamos que las filas tienen un nombre

#Creamos el histograma de la variable Tiempo
plt.figure(1)
plt.hist(atletas['Tiempo'], 15, color="yellow", ec="black")
plt.title("Histograma Tiempo")
plt.savefig("Histograma.jpg")





